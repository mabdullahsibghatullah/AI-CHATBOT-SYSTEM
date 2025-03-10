import openai
import tkinter as tk
from tkinter import scrolledtext

# Set up OpenAI client
client = openai.OpenAI(api_key="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")

# Conversation history to maintain context
conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]


# Function to send message and get AI response
def send_message():
    user_input = user_entry.get().strip()
    if user_input == "":
        return  # Ignore empty input

    chat_display.insert(tk.END, f"\nYou: {user_input}")
    user_entry.delete(0, tk.END)  # Clear input field

    # Add user message to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
        messages=conversation_history,
        max_tokens=200
    )

    ai_response = response.choices[0].message.content
    chat_display.insert(tk.END, f"\n🤖 AI: {ai_response}")

    # Add AI response to conversation history
    conversation_history.append({"role": "assistant", "content": ai_response})


# GUI Setup using Tkinter
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x500")

# Chat Display Area
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=58, height=20, font=("Arial", 12))
chat_display.pack(padx=10, pady=10)

# User Input Field
user_entry = tk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Allow Enter Key to Send Messages
root.bind("<Return>", lambda event: send_message())

# Run the GUI
root.mainloop()



