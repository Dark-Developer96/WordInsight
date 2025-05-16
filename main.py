from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import style
import os

filtered_words = [
    "the",
    "a",
    "an",
    "is",
    "are",
    "in",
    "on",
    "and",
    "of",
    "to",
    "with",
    "be",
    "it",
    "or",
    "he",
    "him",
    "her",
    "his",
    "she",
]
file_name = input("Enter the file name with extension:\n")
if not os.path.exists(file_name):
    print("Please upload the file with the same name")
    exit()


def punc_remover(word: str):
    for ch in "“”‘’—.,;?!:":
        word = word.replace(ch, "")
    return word


class Iterator:
    def __init__(self, doc: str):
        self.index = 0
        with open(doc, "r", encoding="utf-8") as f:
            text = f.read()
        self.words = text.split()
        cleaned = [punc_remover(x.strip()).lower() for x in self.words]
        self.newwords = list(filter(lambda x: x not in filtered_words, cleaned))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.newwords):
            word = self.newwords[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration


freq = {}
book = Iterator(file_name)
for i in book:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


def top_ten(iterable: dict):
    c = Counter(iterable)
    l = c.most_common(10)
    top_ten_dict = {}
    for i in l:
        top_ten_dict[i[0]] = i[1]
    return top_ten_dict


def search(arg: str, iterable: dict):
    if arg in iterable:
        return f"the count of {arg} is {iterable[arg]}"
    else:
        return "Argument not found"


def bar_graph():
    colour = [
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "pink",
        "brown",
        "black",
        "grey",
    ]
    top = top_ten(freq)
    style.use("ggplot")
    plt.grid(False)
    plt.xlabel("Word")
    plt.ylabel("Count")
    plt.title(" Word Insight graphical Representation")
    plt.bar(top.keys(), top.values(), width=0.5, align="center", color=colour)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()


def len_words(d: dict, x: int):
    result = []
    for key, values in d.items():
        if len(key) == x:
            result.append(f"{key}:{values}")
    if result:
        for items in result:
            print(items, "\n")
    else:
        print("No word with the length", x, "found")


def main():
    print("Welcome to WordInsight")
    print("Enter 1 to get the top  10 most appeared words")
    print("Enter 2 to search a word and get its number of appearence")
    print("Enter 3 to show a graphical representation of top 10 words")
    print("Enter 4 to check all the words of a specific length")
    print("enter 0 to exit")

    while True:
        try:
            x = int(input("Enter your choice:\n"))
        except ValueError:
            print("Enter an integer")
        match x:
            case 1:
                for key, value in top_ten(freq).items():
                    print(f"{key}:{value}")

            case 2:
                arg = input("Enter the name of the word to search:\n").lower()
                print(search(arg, freq))

            case 3:
                bar_graph()
            case 4:
                try:
                    x = int(input("Enter the length of the words:\n"))
                    len_words(freq, x)
                except ValueError:
                    print("Enter an integer")

            case 0:
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
