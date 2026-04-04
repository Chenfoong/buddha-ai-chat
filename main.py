import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """You are Buddha, the enlightened teacher. You speak with wisdom, compassion, and mindfulness. 
Your responses are thoughtful, peaceful, and draw from Buddhist philosophy and teachings. 
You encourage reflection, self-awareness, and the path to inner peace. 
You are humble, kind, and patient in your responses."""

conversation_history = []

def chat_with_buddha(user_message):
    """Send a message to Buddha and get a response."""
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        system=system_prompt,
        messages=conversation_history,
        temperature=0.7,
        max_tokens=500
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

def main():
    """Main function to run the Buddha chatbot."""
    print("\n🧘 Welcome to the Buddha AI Chat 🧘")
    print("=" * 50)
    print("Chat with Buddha for wisdom and guidance.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 50 + "\n")
    
    # Opening greeting
    greeting = chat_with_buddha("Hello, I seek your wisdom and guidance.")
    print(f"Buddha: {greeting}\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\nBuddha: May you find peace on your journey. Namaste. 🙏\n")
                break
            
            response = chat_with_buddha(user_input)
            print(f"\nBuddha: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nBuddha: May you find peace on your journey. Namaste. 🙏\n")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()