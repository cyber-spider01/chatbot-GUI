import tkinter as tk
from tkinter import scrolledtext
import re

RULES = {
    r"\b(hi|hello|hey|greetings)\b": "Hello! How can I help you today?",
    r"\b(how are you|how's it going)\b": "I'm just a computer program, but I'm running smoothly! How can I assist?",
    r"\b(what is your name|who are you)\b": "I am a simple rule-based AI chatbot built with Python.",
    r"\b(hours|open|timing)\b": "We are open Monday through Friday from 9:00 AM to 6:00 PM.",
    r"\b(contact|email|phone|support)\b": "You can reach our team at support@example.com or call +1-800-555-0199.",
    r"\b(price|pricing|cost|fee)\b": "Our basic tier is free, and premium subscriptions start at $9.99/month.",
    r"\b(help|assist|menu)\b": "I can answer questions about: hours, pricing, contact info, or account support.",
    r"\b(bye|exit|quit|goodbye)\b": "Goodbye! Have a great day!"
}

DEFAULT_RESPONSE = "I'm sorry, I don't understand that yet. Type 'help' to see what I can answer."

def get_response(user_text):
    text = user_text.lower().strip()
    for pattern, answer in RULES.items():
        if re.search(pattern, text):
            return answer
    return DEFAULT_RESPONSE

def send_message(event=None):
    user_msg = user_entry.get().strip()
    if not user_msg:
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_msg}\n")
    user_entry.delete(0, tk.END)

    bot_reply = get_response(user_msg)
    chat_history.insert(tk.END, f"Bot: {bot_reply}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

root = tk.Tk()
root.title("Rule-Based Chatbot")
root.geometry("450x500")
root.resizable(False, False)

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 11))
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

user_entry = tk.Entry(input_frame, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
user_entry.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", width=8, command=send_message)
send_button.pack(side=tk.RIGHT)

chat_history.config(state=tk.NORMAL)
chat_history.insert(tk.END, "Bot: Hello! Ask me anything or type 'help'.\n\n")
chat_history.config(state=tk.DISABLED)

root.mainloop()