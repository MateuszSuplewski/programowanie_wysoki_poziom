from typing import List


class SimpleChatBot:
    def __init__(self, questions: List[str]) -> None:
        self.questions = questions
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self) -> None:
        if self.counter < len(self.questions):
            self.counter += 1
            return
        else:
            raise StopIteration


bot = SimpleChatBot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
for question in bot.questions:
    print(question)
    input()

while True:
    try:
        next(bot)
    except StopIteration:
        print("No more questions to ask!")
        break
