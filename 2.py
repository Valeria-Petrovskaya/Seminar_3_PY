N = int(input("Введите количество элементов в массиве: "))
A = []
for i in range(N):
    A.append(int(input()))
X = int(input("Введите число, к которому нужно найти ближайший элемент в массиве: "))
closest = A[0]
for i in range(N):
    if abs(A[i] - X) < abs(closest - X):
        closest = A[i]
print("Самый близкий элемент к числу", closest)