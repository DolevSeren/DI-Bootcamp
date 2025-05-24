from anagram_checker import AnagramChecker


checker = AnagramChecker()
print("Welcome to the Anagram Checker!")
while True:
    user_word = input("Type a word or 'exit' to quit:\n")

    if user_word.lower() == "exit":
        break
    if len(user_word.split()) > 1:
        print("Error: please enter only one word")
        continue

    if not user_word.isalpha():
        print("Error: your word ,must include only letters!")
        continue

    user_word = user_word.strip()

    anagram = checker.get_anagrams_word(user_word)


    print("Anagrams: ", anagram)












