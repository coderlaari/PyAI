import json
from time import sleep
import pyttsx3


AUTHORIZED_USER = "admin"
PIN_CODE = "1234"

class SmartAI:
    def __init__(self):
        self.memory_file = "memory.json"
        self.memory = self.load_memory()
        self.engine = pyttsx3.init()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)

    def speak(self, text):
        if text != "I dont know the answer.":
            self.engine.say(text)
            self.engine.runAndWait()

    def learn(self, question, answer, user, pin):
        if user == AUTHORIZED_USER and pin == PIN_CODE:
            self.memory[question.lower()] = answer
            self.save_memory()
            print("AI: I have learned a new answer.")
            self.speak("I have learned a new answer.")
        else:
            print("Wrong username or PIN code! You cannot teach AI.")
            self.speak("Wrong username or PIN code! You cannot teach AI.")

    def respond(self, question):
        question = question.lower()
        if question in self.memory:
            response = self.memory[question]
        else:
            response = "I dont know the answer."

        print("AI:", response)
        return response

ai = SmartAI()

while True:
    user_input = input("Ask something (or type 'teach' to add a answer, 'stop' to exit): ")

    if user_input.lower() == "stop":
        print("[INFO] Saving memory...")
        ai.save_memory()
        sleep(3)
        print("[INFO] Memory saved successfully.")
        print("[INFO] Stopping AI...")
        sleep(3)
        print("[INFO] AI stopped.")
        print("[INFO] Exiting program...")
        print("[INFO] Program stopped.")
        break
    elif user_input.lower() == "teach":
        user = input("Username: ")
        pin = input("PIN-code: ")
        question = input("Type question: ")
        answer = input("Type answer: ")
        ai.learn(question, answer, user, pin)
    else:
        ai.respond(user_input)
