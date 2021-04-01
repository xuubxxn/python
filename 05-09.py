a = int(input("A를 입력하세요"))
ch = input("연산자를 입력하세요")
b = int(input("B를 입력하세요"))

if ch == "+" :
    print("%d + %d = %d" %(a, b, a+b))
elif ch == "-" :
    print("%d - %d = %d" %(a, b, a-b))

