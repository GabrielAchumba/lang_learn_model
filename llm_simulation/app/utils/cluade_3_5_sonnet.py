import time
import requests
import concurrent.futures
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CLAUDE_API_KEY")

CLAUDE_API_URL = "https://api.anthropic.com/v1/completions"


headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

def generate_prompt_response(prompt: str, model: str = "claude-3.5-sonnet", max_tokens: int = 1000):
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }
    # Start time to measure E2E request latency
    start_time = time.time()
    
    # Send API request
    response = requests.post(CLAUDE_API_URL, headers=headers, json=payload)
    
    # Calculate End-to-End Request Latency
    e2e_latency = time.time() - start_time
    
    # Parse the response
    if response.status_code == 200:
        data = response.json()
        return data['completion'], e2e_latency, len(data['completion'].split()), len(data['completion'])
    else:
        return None, e2e_latency, 0, 0
    

def measure_performance(prompt: str, model: str = "claude-3.5-sonnet"):
    # Step 1: Measure Time to First Token (TTFT) and E2E latency
    start_time = time.time()  # Start time for E2E Latency

    # Send the request and capture TTFT
    response = requests.post(CLAUDE_API_URL, headers=headers, json={
        "model": model,
        "prompt": prompt,
        "max_tokens": 1000
    }, stream=True)  # Use streaming to track the first token response
    
    # Step 2: Capture Time to First Token (TTFT)
    ttft = time.time() - start_time  # Time to First Token

    # Step 3: Full response processing (End-to-End Latency)
    e2e_latency = time.time() - start_time

    # Step 4: Measure Tokens per Second (TPS)
    # Assuming response contains text tokens, we can calculate the number of tokens and time to generate all tokens
    tokens = response.json()['completion'].split()
    total_tokens = len(tokens)
    tps = total_tokens / e2e_latency  # Tokens per second

    return ttft, e2e_latency, tps

def measure_rps(prompt: str, num_requests: int):
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(measure_performance, prompt) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Process each result
    
    total_time = time.time() - start_time
    rps = num_requests / total_time
    return rps

# Example usage
prompt = "Explain the basics of French grammar."
ttft, e2e_latency, tps = measure_performance(prompt)
print(f"TTFT: {ttft:.2f} seconds")
print(f"E2E Latency: {e2e_latency:.2f} seconds")
print(f"Tokens per Second: {tps:.2f} TPS")

# Example usage for 10 requests
num_requests = 10
rps = measure_rps(prompt, num_requests)
print(f"Requests Per Second (RPS): {rps:.2f}")
