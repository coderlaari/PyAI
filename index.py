import json
import pyttsx3

# Ainoastaan tämä käyttäjä ja PIN voivat opettaa AI:ta
AUTHORIZED_USER = "admin"  # Vaihda haluamaksesi
PIN_CODE = "1234"  # Vaihda haluamaksesi

class SmartAI:
    def __init__(self):
        self.memory_file = "memory.json"
        self.memory = self.load_memory()
        self.engine = pyttsx3.init()  # Alustetaan äänimoottori

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
        """Lukee vastauksen ääneen vain, jos se ei ole 'En tiedä vastausta'"""
        if text != "En tiedä vastausta.":
            self.engine.say(text)
            self.engine.runAndWait()

    def learn(self, question, answer, user, pin):
        """Opettaa AI:lle uuden vastauksen vain, jos käyttäjänimi ja PIN ovat oikein"""
        if user == AUTHORIZED_USER and pin == PIN_CODE:
            self.memory[question.lower()] = answer
            self.save_memory()
            print("AI on oppinut uuden vastauksen!")
            self.speak("Olen oppinut uuden vastauksen.")
        else:
            print("Väärä käyttäjänimi tai PIN-koodi! Et voi opettaa AI:ta.")
            self.speak("Väärä käyttäjänimi tai PIN-koodi!")

    def respond(self, question):
        """Tarkistaa muistin ja vastaa, jos AI on oppinut vastauksen"""
        question = question.lower()
        if question in self.memory:
            response = self.memory[question]
        else:
            response = "En tiedä vastausta."  # Muokattu selkeämmäksi

        print("AI:", response)  # Tulostaa vastauksen aina
        self.speak(response)  # Puhuu vain, jos vastaus ei ole "En tiedä vastausta."
        return response

ai = SmartAI()

while True:
    user_input = input("Kysy jotain (tai kirjoita 'opeta' lisätäksesi vastauksen, 'lopeta' poistuaksesi): ")

    if user_input.lower() == "lopeta":
        break
    elif user_input.lower() == "opeta":
        user = input("Käyttäjänimi: ")
        pin = input("PIN-koodi: ")
        question = input("Kirjoita kysymys: ")
        answer = input("Kirjoita vastaus: ")
        ai.learn(question, answer, user, pin)
    else:
        ai.respond(user_input)
