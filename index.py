import json
from time import sleep

class SimpleAI:
    def __init__(self):
        self.memory_file = "memory.json"  # File where we store memory
        self.memory = self.load_memory()  # Load memory on startup

    def load_memory(self):
        """Load memory from file if it exists."""
        try:
            with open(self.memory_file, "r") as file:
                return json.load(file)  # Load dictionary from file
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return empty memory if file is missing or empty

    def save_memory(self):
        """Save current memory to file."""
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)  # Save as JSON

    def learn(self, question, answer):
        """Learn a new question-answer pair."""
        self.memory[question.lower()] = answer  # Store in dictionary
        self.save_memory()  # Save to file

    def respond(self, question):
        """Respond based on learned memory."""
        return self.memory.get(question.lower(), "No answer found.")

# Testing AI
ai = SimpleAI()

while True:
    user_input = input("Ask something (type 'stop' to stop the AI): ")

    if user_input.lower() == "stop":
        try: # Try to save memory before shutting down
            print("\n[INFO] Saving memory...\n")
            ai.save_memory() # Save memory to file
            sleep(3)
            print("[INFO] Memory saved successfully.\n") # Notify user
            print("[INFO] Shutting down AI...\n") # Shutting down AI
            sleep(3)
            print("[INFO] AI has been shut down.\n")
            print("[INFO] Clearing chat...")
            print("\n\n\n\n\n\n")
            print("[INFO] Chat has been cleared.\n")
            print("[INFO] Stopping program.\n")
        except Exception as e:
            print("\n[ERROR] Error saving memory: ", e + "\n") # Notify user if error occurs
        break

    response = ai.respond(user_input)
    
    if response == "No answer found.":
        new_answer = input("AI: I don't know the answer yet :( Can you tell me?")
        ai.learn(user_input, new_answer)
        print("AI: Thank you! I learned a new answer.")
    else:
        print("AI:", response)