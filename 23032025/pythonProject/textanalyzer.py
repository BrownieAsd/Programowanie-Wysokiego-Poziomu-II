class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def char_counter(self):
        return print(f"amount of characters:{len(self.text)}")

    def word_counter(self):
        count = 0
        txt = self.text.split(" ")
        for word in txt:
            count += 1
        return print(f"amount of words:{count}")

    def unique_words(self):
        arr = []
        count = 0
        txt = self.text.split(" ")
        for word in txt:
            if word not in arr:
                arr.append(word)
                count += 1
        return print(f"amount of unique words:{count}")
