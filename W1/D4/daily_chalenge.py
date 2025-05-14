MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''


new_list = MATRIX_STR.strip().split("\n")
big_list = [list(row) for row in new_list]

message = ''
for col in range(len(big_list[0])):
    for row in big_list:
        message += row[col]

def replace_non_alpha_between_letters(text):
    result = []
    i = 0
    length = len(text)

    while i < length:
        if text[i].isalpha():
            result.append(text[i])
            i += 1
        else:
            start = i
            while i < length and not text[i].isalpha():
                i += 1
            if result and i < length and text[i].isalpha():
                result.append(' ')

    return ''.join(result)


decoded_message = replace_non_alpha_between_letters(message)
print(decoded_message)
