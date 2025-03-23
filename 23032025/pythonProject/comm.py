class Comm:
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def send_text(self):
        return print(f"Text message {self.text} has been send to {self.receiver}")

