import os

class AnagramChecker:
    def __init__(self):
        home_dir = os.path.expanduser("~")
        downloads_path = os.path.join(home_dir, "Downloads")
        file_path = os.path.join(downloads_path, "sowpods.txt")

        with open(file_path, 'r', encoding='utf-8') as f:
            self.word_list = [line.strip() for line in f]

    def is_valid_word(self, word):
        return word.upper() in self.word_list

    def get_anagrams_word(self, word):
        word = word.upper()
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2) and word1 != word2


    