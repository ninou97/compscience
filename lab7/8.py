
s = "Real Madrid-Barcelona 3:1"

score = s.split()[-1]
s = " ".join(s.split()[:-1])

team1, team2 = score.split(":")

if team1 > team2:
    print(s.split("-")[0])
elif team1 < team2:
    print(s.split("-")[1])
else:
    print("ничья")

