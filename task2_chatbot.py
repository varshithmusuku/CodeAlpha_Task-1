import tkinter as tk 
from tkinter import scrolledtext 
import nltk 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np 
 
# Download required NLTK data (runs once) 
nltk.download('punkt', quiet=True) 
 
# FAQ Data 
faqs = { 
    "What are your working hours?": "We are open from 9 AM to 5 PM, Monday to Friday.", 
    "How can I reset my password?": "You can reset your password by clicking 'Forgot Password' 
on the login page.", 
    "Do you offer refunds?": "Yes, we offer a 30-day money-back guarantee.", 
    "Where is your office located?": "Our main office is located in Hyderabad, India.", 
    "How can I contact support?": "You can email us at support@example.com." 
} 
 
questions = list(faqs.keys()) 
answers = list(faqs.values()) 
 
# Preprocessing and Vectorization 
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english') 
tfidf_matrix = vectorizer.fit_transform(questions) 
 
def get_response(user_query): 
    query_vec = vectorizer.transform([user_query]) 
    similarities = cosine_similarity(query_vec, tfidf_matrix) 
    best_match_idx = np.argmax(similarities) 
     
    # If the similarity is too low, it means we don't have a good answer 
    if similarities[0][best_match_idx] < 0.2: 
        return "I'm sorry, I don't understand the question. Please contact support." 
    return answers[best_match_idx] 
 
# UI Setup 
def send_message(event=None): 
    user_msg = user_input.get() 
    if not user_msg.strip(): return 
     
    chat_window.config(state=tk.NORMAL) 
    chat_window.insert(tk.END, "You: " + user_msg + "\n") 
bot_response = get_response(user_msg) 
chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n") 
chat_window.config(state=tk.DISABLED) 
chat_window.yview(tk.END) 
user_input.delete(0, tk.END) 
root = tk.Tk() 
root.title("FAQ Chatbot - Task 2") 
root.geometry("400x500") 
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD) 
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 
user_input = tk.Entry(root, font=("Arial", 12)) 
user_input.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, expand=True) 
user_input.bind("<Return>", send_message) 
send_btn = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white") 
send_btn.pack(padx=10, pady=10, side=tk.RIGHT) 
root.mainloop()
