
import openai, os
print("CREM Assistant Ready.")
while True:
    q = input("Ask about the system: ")
    if q.lower() in ['exit', 'quit']: break
    print("Thinking...")
    print(f"AI: [Mock Response] I would look at your code and explain: '{q}'")
