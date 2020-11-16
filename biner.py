def binerkedesimal(n):
    pangkat = len(n) - 1
    desimal = 0
    for i in range(len(n)):
        biner = int(n[i])
        desimal2 = biner * (2**pangkat)
        desimal += desimal2
        pangkat -= 1
    return desimal

n = input("Biner = ")

print(binerkedesimal(n))
