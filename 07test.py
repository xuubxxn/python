import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while(True):
        A, B = map(int, input().split())
        if 0 < A < 10 or 0 < B < 10:
            print(A + B)
        else:
            break
