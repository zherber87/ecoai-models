import subprocess
import os

def run_model():
    model_path = "weights/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print("Model weight not found. Please download it from model.json.")
        return

    print("Launching TinyLlama...")
    subprocess.run([
        "./llama.cpp/main",  # Adjust this path based on how you load with llama.cpp
        "-m", model_path,
        "-p", "Hello, how can I help you?"
    ])

if __name__ == "__main__":
    run_model()
