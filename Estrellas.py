#ESTRELLAS
i=1
j=9
while i <= 9 or j>=1:
    if i <= 9:
        print("*" * i)
        i=i+2
    if i==11 and j==9:
        print("-" * 8)
    if i>=11:
        print("*" * j)
        j=j-2