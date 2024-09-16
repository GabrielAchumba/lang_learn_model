import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

API_ENDPOINT = 'https://gemini-api-url.com/v1/generate'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Function to call the API and measure metrics
def call_gemini_api(prompt):
    data = {
        "model": "gemini-1.5flash",  # Replace with actual model name
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.7
    }

    # Measure Time to First Token (TTFT) and End-to-End Latency
    start_time = time.time()
    response = requests.post(API_ENDPOINT, json=data, headers=headers, stream=True)
    ttft = time.time() - start_time  # Time to First Token (when response starts)
    
    # Stream and read the response (this part depends on API streaming)
    tokens_received = 0
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            tokens_received += len(chunk.decode().split())  # Calculate token count

    e2e_latency = time.time() - start_time  # End-to-End Latency

    return {
        "response": response.json(),
        "ttft": ttft,
        "tokens_received": tokens_received,
        "e2e_latency": e2e_latency
    }

# Function to calculate Requests Per Second (RPS)
def measure_rps(prompt, num_requests=10):
    start_time = time.time()
    
    for _ in range(num_requests):
        call_gemini_api(prompt)
    
    total_time = time.time() - start_time
    rps = num_requests / total_time

    return rps

# Function to measure Tokens Per Second (TPS)
def calculate_tps(ttft, tokens_received):
    return tokens_received / ttft if ttft > 0 else 0

# Example Usage
if __name__ == "__main__":
    prompt = "Teach me the basics of French grammar."

    # Measure the performance
    metrics = call_gemini_api(prompt)
    
    ttft = metrics['ttft']
    tokens_received = metrics['tokens_received']
    e2e_latency = metrics['e2e_latency']

    print(f"Time to First Token: {ttft} seconds")
    print(f"Tokens Received: {tokens_received}")
    print(f"End-to-End Latency: {e2e_latency} seconds")
    
    tps = calculate_tps(ttft, tokens_received)
    print(f"Tokens Per Second: {tps} tokens/sec")
    
    rps = measure_rps(prompt)
    print(f"Requests Per Second: {rps} requests/sec")