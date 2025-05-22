import os
import string
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


class Text:
    def __init__(self, text):
        self.text = text



    def word_frequency(self, word):
        words = self.text.split()
        if word:
            return words.count(word)
        else:
            return None

    def most_common_word(self):
        words_list = self.text.lower().split()
        word_counts = {}
        for word in words_list:
            if word in word_counts:
                word_counts[word] += 1

            else:
                word_counts[word] = 1

        most_common = max(word_counts, key=word_counts.get)
        return most_common

    def unique_words(self):
        new_word_list = self.text.split()
        unique = set(new_word_list)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return cls(content)

class TextModification(Text):
    def remove_punctuation(self):
        new_string = ""
        for char in self.text:
            if char not in string.punctuation:
                new_string += char
        return new_string

    def remove_stop_words(self):
        stop_words = ["a", "the", "is", "and", "in", "to", "of", "it", "that", "on"]
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        pattern = r"[^a-zA-Z0-9\s]"
        clean_text = re.sub(pattern, "", self.text)
        return clean_text



text1 = Text("hey there im dolev im not old hey")
print(text1.word_frequency("im"))
print(text1.most_common_word())
text2 = TextModification("dolev is my name im so tired i want to go to bad so much")
print(text2.remove_stop_words())
print(text2.remove_special_characters())








