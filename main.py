
'''
programm  will encrypt with  my  encryption
'''
# Ask  for  value ...
print("Enter your name ")

value = input("")


def taskToEncrypt(value):
    ascii_values = []
    for character in value:
       ascii_values.append(ord(character))
    print(value, ' in ascii code --->', ascii_values)
    # Python program for implementation of Bubble Sort
    n = len(ascii_values)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if ascii_values[j] > ascii_values[j+1]:
                 ascii_values[j], ascii_values[j+1] = ascii_values[j+1], ascii_values[j]
    print("asci value bubble sorted --->", ascii_values)
    result = ""
    for g in ascii_values:
        result = result + chr(g)

    print("Bubble sorted"+" --- "+value+" ---> "+result)

taskToEncrypt(value)


