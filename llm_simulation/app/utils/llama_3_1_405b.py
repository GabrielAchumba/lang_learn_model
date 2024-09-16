import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LLAMA_API_KEY")

API_URL = "https://api.llama3-model.com/v1/generate"


# Function to measure the metrics
def measure_llama_metrics(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama-3.1-405b",
        "prompt": prompt,
        "max_tokens": 1000,
    }
    
    # Measure Time to First Token (TTFT)
    start_time = time.time()
    
    try:
        # Send the request and capture the response
        response = requests.post(API_URL, json=data, headers=headers, stream=True)

        # Start processing response
        if response.status_code == 200:
            # Time to First Token
            first_token_time = time.time() - start_time
            print(f"Time to First Token (TTFT): {first_token_time:.2f} seconds")
            
            # Processing response
            token_count = 0
            start_latency_time = time.time()

            for chunk in response.iter_content(chunk_size=None):
                if chunk:
                    token_count += 1
                    # Simulate token-by-token processing
                    print(chunk.decode("utf-8"))

            # End-to-End Request Latency (E2E Latency)
            end_latency_time = time.time() - start_latency_time
            print(f"End-to-End Request Latency: {end_latency_time:.2f} seconds")

            # Tokens Per Second (TPS)
            if end_latency_time > 0:
                tokens_per_second = token_count / end_latency_time
                print(f"Tokens Per Second (TPS): {tokens_per_second:.2f} tokens/second")

            # Requests Per Second (RPS) - this is tricky unless making multiple requests
            end_time = time.time() - start_time
            print(f"Request took: {end_time:.2f} seconds")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error occurred: {e}")

# Example prompt for language learning
prompt = "Explain the basics of French grammar to a beginner."
measure_llama_metrics(prompt)