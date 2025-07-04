# 🎬 AnimateItNow

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/yourusername/animateitnow)](LICENSE)
[![Manim](https://img.shields.io/badge/Manim-Community%20Edition-purple?logo=manim)](https://www.manim.community/)
[![GitHub Workflow](https://github.com/maheshpaulj/AnimateItNow/actions/workflows/test.yml/badge.svg)](https://github.com/maheshpaulj/AnimateItNow/actions)

**AnimateItNow** lets you turn natural language prompts into stunning **Manim** animations using LLMs via OpenRouter.

---

## 🚀 Features

- Generate Python scripts for Manim with just a prompt  
- Automatic class detection & rendering  
- Supports multiple OpenRouter models  
- Optional video rendering  
- CLI tool with `.env` support  

---

## 📦 Installation

```bash
git clone https://github.com/maheshpaulj/AnimateItNow
cd animateitnow
pip install -e .
````

> You can now run it using:

```bash
animateitnow "Show a bouncing ball" -q h
```

---

## ⚙️ Requirements

```bash
pip install -r requirements.txt
```

### System Dependencies

| Tool       | Description                          |
| ---------- | ------------------------------------ |
| **FFmpeg** | For video rendering (`manim`)        |
| **OpenGL** | For graphics backend (`manim`)       |
| **LaTeX**  | For math rendering (esp. on Windows) |

---

### ✅ Windows LaTeX Setup (Fix Common Errors)

1. Download & install [MiKTeX](https://miktex.org/download)
2. Enable **package-on-the-fly** installation
3. Open the MiKTeX and check for updates

```bash
mpm --update-db
```

✅ This solves most `latex not found` or `Failed to compile` issues when using Manim.

---

## 🔐 API Key Setup

AnimateItNow uses [OpenRouter.ai](https://openrouter.ai) models. To use it:

1. Get your key: [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. Create a `.env` file:

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Make sure you **never commit** your `.env` file!

---

## 📜 Usage

```bash
animateitnow "Show rotating Earth with axis labels" -o earth.py -q h
```

### CLI Flags

| Flag            | Description                                |
| --------------- | ------------------------------------------ |
| `--output, -o`  | Output file name (Python)                  |
| `--quality, -q` | Rendering quality: `l`, `m`, `h`, `p`, `k` |
| `--model, -m`   | Choose OpenRouter model                    |
| `--no-render`   | Generate code but don't render             |

---

## 🧠 Available Models

* `deepseek/deepseek-chat:free` (default)
* `mistralai/mistral-7b-instruct:free`
* `meta-llama/llama-3-70b-instruct`
* `anthropic/claude-3.5-sonnet`

---

## 🧪 Example

```bash
animateitnow "Visualize a sine wave using number plane"
```

---

## ✅ GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: Test CLI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e . && pip install manim python-dotenv
      - run: animateitnow "Draw a simple triangle" --no-render
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
```

---

## 🗂 .env Template

Create a file `.env`:

```env
# Rename to .env and paste your key
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📂 Project Structure

```
animateitnow/
├── animateitnow/
│   └── main.py        # CLI script logic
├── .env               # API key (not committed)
├── README.md
├── setup.py
├── requirements.txt
└── .github/
    └── workflows/
        └── test.yml
```

---

## 🧑‍💻 Contributing

Contributions welcome! Feel free to:

* Add GUI
* Add support for image export
* Improve prompt logic

---

## 📄 License

[MIT](/LICENSE)

---

## 🚧 Roadmap

* [ ] Add GUI with PyQt/Tkinter
* [ ] Support Web UI via Flask
* [ ] Add template prompt library

---

## ❤️ Inspired by

* [Manim Community Edition](https://www.manim.community/)
* [OpenRouter](https://openrouter.ai/)
