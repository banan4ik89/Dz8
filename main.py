class WordLength:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return len(word)
        else:
            raise StopIteration

words = ["home", "bananas", "python", "school"]
iterator = WordLength(words)

for length in iterator:
    print(length)
