N = int(input("Введите количество элементов в массиве: "))
A = []
for i in range(N):
    A.append(int(input()))
X = int(input("Введите число, которое нужно найти в массиве: "))
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print("Число встречается", count, "раз")