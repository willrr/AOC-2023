

print("Enter question: ")
lines = []
x = ""  # The string is declared
for line in iter(input, x):
    lines.append(line)
    pass

# print(lines)

result = 0
for answer in lines:
    #print(answer)
    number = ""
    for letter in answer:
        #print(letter, end=' ')
        #print(letter.isnumeric())
        if letter.isnumeric():
            number += letter
    # print(len(number))
    if len(number) > 2:
        # print("here")
        for calc, num in enumerate(number):
            # print("num:", num)
            if calc == 0:
                number2 = num
            if calc == len(number) -1:
                number = number2 + num
    if len(number) == 1:
        number += number
    print(int(number))
    result += int(number)

print(result)