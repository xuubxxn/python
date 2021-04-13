# N = int(input())

# count = N // 5
# N = N % 5

# count += N // 3
# N = N % 3

# if N != 0 :
#     print (-1)
# else : 
#     print(count)

# 5로 나누어 떨어지는 경우
# 5로 나누어 떨어지고 3으로 나누어 떨어지는 경우
# 3으로 나누어 떨어지는 경우
# 안되는 경우 -1

# N = int(input())

# if N % 5 == 0 :
#     print(N // 5)
# elif ((N % 5) % 3 == 0) :
#     print((N//5)+((N % 5)//3))
# elif N % 3 == 0 :
#     print(N // 3)
# else :
#     print(-1)

def algorithm (kilo) :
    n = kilo // 5
    for i in range (n, -1, -1):
        result = kilo - (5*i)
        if result % 3 == 0:
            return i + (result // 3)
    return -1

kilo = int(input())
print(algorithm(kilo))

