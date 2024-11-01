
height = int(input())
width = int(height*2 - 1)

leaves = -1
for i in range(height):
    leaves += 2
    empty = (width - leaves)//2
    
    
    print(" "*empty, "#"*leaves, " "*empty)

print(" "*(width//2), "#")
