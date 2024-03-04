
# 1 print the abc in uppercase or lowercase.
# 2 print a word starting with a specific letter.
# 3 print N*N multiplication table
# 4 print square number of a given number
# 5 check if a given number is prime

task = input("what task you need ? ")
ab = "abcdefghijklmnopqrstuvwxyz"
match task:
        case '1':
            print(ab.lower())
        case '2':
            print(ab.upper())
        case '3':
            num = int(input("inter the number you want its multiplivation table "))
            for row in range(1,num+1):
                for column in range(1,num+1):
                    print(f"{row}x{column}={row*column}", end="\t")
                print(" ")


        case '4':
            num = int(input("inter the number you want to square"))
            print(num*num)
        case '5':
            num = int(input("inter the number you want tot check if prime: "))
            if num > 1:
                for i in range(2, int(num / 2) + 1):
                    if (num % i) == 0:
                        print(num, "is not a prime number")
                        break
                else:
                    print(num, "is a prime number")
            else:
                print(num, "is not a prime number")


        case _:
            print("invalid input")