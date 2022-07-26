import os
import sys


def solution(num):

    num = int(input("Enter a number"))
    for n in range(2,num):
        if num % n == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    # if len(sys.argv) <= 1:
    #     sys.exit(os.error("Argument required"))

    # n = int(sys.argv[1])
    print(solution(num))