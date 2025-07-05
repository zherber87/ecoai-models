# TinyLlama Chat Model

This is the TinyLlama 1.1B Chat model configured to run via `llama.cpp`.

## Features

- Lightweight (400MB+)
- Fast startup on CPU
- Supports chat-style prompts

## Instructions

1. Download the `Q4_K_M` GGUF file from HuggingFace (see `model.json`)
2. Place it into `weights/`
3. Run `main.py` to test

## Model Info

- **Quantization:** Q4_K_M
- **Framework:** llama.cpp
- **Context Size:** 2048
