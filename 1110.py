N = int(input())
result = N
count = 0
while True:
    N = (N % 10) * 10 + ((N // 10) + (N % 10)) % 10
    count += 1
    if N == result:
        break
print(count)

# N = int(input())
# result = N
# count = 0
# while True:
#     n1 = N // 10
#     n2 = N % 10
#     add = n1 + n2
#     N = n2 * 10 + add % 10
#     count += 1
#     if N == result:
#         break
# print(count)