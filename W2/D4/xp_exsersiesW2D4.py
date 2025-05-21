# import os
# import random
#
# dir_path = os.path.dirname(os.path.realpath(__file__))
#
# # Step 1: get_words_from_file
# def get_words_from_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         words = content.split()  # מפצל לפי רווחים ושורות
#         return words
#
# # Step 2: get_random_sentence
# def get_random_sentence(length):
#     words = get_words_from_file(f"{dir_path}/words.txt")
#     if length > len(words):
#         raise ValueError("Not enough words in the file to create that sentence.")
#     selected_words = random.choices(words, k=length)  # מותר מילים חוזרות
#     sentence = " ".join(selected_words)
#     return sentence.lower()
#
# # Step 3: main
# def main():
#     print("This program creates a random sentence based on the number of words you choose (between 2 and 20).")
#     try:
#         user_input = input("Please enter a number between 2 and 20: ")
#         sentence_length = int(user_input)
#         if 2 <= sentence_length <= 20:
#             sentence = get_random_sentence(sentence_length)
#             print(f"\nYour random sentence:\n{sentence}")
#         else:
#             print("Error: Number must be between 2 and 20.")
#     except ValueError:
#         print("Error: Please enter a valid number.")
#
# # רק אם הקובץ הזה הוא הראשי, תריץ את main
# if __name__ == "__main__":
#     main()



####################################################################################################################
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
"""

new_dict = json.loads(sampleJson)
print(new_dict["company"]["employee"]["payable"]["salary"])
new_dict["company"]["employee"]["birth_date"] = "1996-26-11"
print(new_dict)

with open(f'{dir_path}/new_file.json', 'w', encoding='utf-8') as new_file:
    json.dump(new_dict, new_file, indent=3)
















