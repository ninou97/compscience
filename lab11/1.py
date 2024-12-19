alphabet = {}

words = [".,?!:",
         "ABC",
         "DEF",
         "GHI",
         "JKL",
         "MNO",
         "PQRS",
         "TUV",
         "WXYZ",
         " ",
         ]

for i, word in enumerate(words):
    for j, letter in enumerate(word):
        alphabet[letter] = str((i+1))*(j+1)

def convertToNumberCommands(s: str):
    s = s.upper()
    for l in s:
        print(alphabet[l], end="")
    print()

convertToNumberCommands("Hello, World!")