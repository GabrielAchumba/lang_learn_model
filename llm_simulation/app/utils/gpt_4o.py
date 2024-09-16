import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GPT_4o_API_KEY")

# Set up your OpenAI API key
openai.api_key = API_KEY

# Function to measure Time to First Token, Tokens Per Second, End to End Request Latency, and Requests Per Second
def measure_gpt4o_performance(prompt, num_requests=1):
    ttft_list = []
    tps_list = []
    e2e_latency_list = []
    
    for _ in range(num_requests):
        # Start overall request timing (for E2E latency)
        start_time = time.time()
        
        # Send request to OpenAI and time the first response (Time to First Token)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a helpful language tutor."},
                          {"role": "user", "content": prompt}],
                stream=True  # Stream to measure TTFT
            )
            
            first_token_time = None
            total_tokens = 0
            total_tokens_time = None

            for chunk in response:
                # Get the timestamp for the first token
                if first_token_time is None:
                    first_token_time = time.time()

                # Count tokens and get timestamp for the last token
                if 'choices' in chunk:
                    total_tokens += 1
                    total_tokens_time = time.time()

            # End-to-End latency
            e2e_latency = total_tokens_time - start_time if total_tokens_time else None
            e2e_latency_list.append(e2e_latency)

            # Time to First Token (TTFT)
            ttft = first_token_time - start_time if first_token_time else None
            ttft_list.append(ttft)

            # Tokens Per Second (TPS)
            if ttft is not None and total_tokens_time is not None:
                total_response_time = total_tokens_time - first_token_time
                tps = total_tokens / total_response_time if total_response_time > 0 else None
                tps_list.append(tps)

        except Exception as e:
            print(f"Error: {e}")
    
    # Calculate and return average metrics
    avg_ttft = sum(ttft_list) / len(ttft_list) if ttft_list else None
    avg_tps = sum(tps_list) / len(tps_list) if tps_list else None
    avg_e2e_latency = sum(e2e_latency_list) / len(e2e_latency_list) if e2e_latency_list else None
    rps = num_requests / sum(e2e_latency_list) if e2e_latency_list else None
    
    return {
        "avg_ttft": avg_ttft,
        "avg_tps": avg_tps,
        "avg_e2e_latency": avg_e2e_latency,
        "rps": rps
    }

# Example usage
prompt = "Explain how verb conjugation works in Spanish."
metrics = measure_gpt4o_performance(prompt, num_requests=5)
print(metrics)