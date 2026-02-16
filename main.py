class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class User:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def send(self, to, text):
        msg = Message(self.name, text)
        to.messages.append(msg)

    def inbox(self):
        for m in self.messages:
            print(f"{m.sender}: {m.text}")

def run():
    a = User("Ali")
    b = User("Vali")

    a.send(b, "Salom")
    b.send(a, "Qalesan")

    print("\nAli inbox:")
    a.inbox()

    print("\nVali inbox:")
    b.inbox()

run()
