
s = """4
QQA"""

# s = """4
# QQAQ"""

questions = 0
answers = 0
for c in s:
    if c == "Q":
        questions += 1
    if c == "A":
        answers += 1

if questions <= answers:
    print("+")
else:
    print("-")