# Buddha AI Chat 🧘

A command-line chatbot that lets you have philosophical conversations with an AI Buddha powered by OpenAI's GPT API.

## Features

- 💬 Multi-turn conversation with context awareness
- 🧘 Buddhist philosophy and wisdom responses
- 🤖 Powered by OpenAI GPT-3.5-turbo
- 🎯 Simple and intuitive command-line interface
- 🌿 Mindful and compassionate responses

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chenfoong/buddha-ai-chat.git
cd buddha-ai-chat
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

## Usage

Run the chatbot:
```bash
python main.py
```

Start typing your questions or thoughts, and Buddha will respond with wisdom and guidance. Type `exit` or `quit` to end the conversation.

## Example

```
🧘 Welcome to the Buddha AI Chat 🧘
==================================================
Chat with Buddha for wisdom and guidance.
Type 'exit' or 'quit' to end the conversation.
==================================================

Buddha: Namaste, dear seeker. I am here to guide you on your path to enlightenment...

You: What is the meaning of life?
Buddha: The meaning of life is found in the present moment...

You: exit
Buddha: May you find peace on your journey. Namaste. 🙏
```

## Configuration

You can customize the Buddha's personality by editing the `system_prompt` in `main.py`.

## Dependencies

- `openai` - OpenAI Python client library
- `python-dotenv` - Load environment variables from .env file

## License

MIT

## Contributing

Feel free to fork this project and submit pull requests with improvements!