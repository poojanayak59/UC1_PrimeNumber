def validate():
    aa = int(user_input)
    # print(result)
    if aa > 1:
        # Python also allows us to use the else condition with for loops.
        # The else block just after for/while is executed only when the loop is NOT terminated by a break statement
        for i in range(2, int(aa / 2) + 1):
            print(i)
            if (aa % i) == 0:
                # print(i)
                print("Sorry, Not a prime number")
                break
        else:
            print("Correct, It is a prime number")

    else:
        print("Apologies")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a prime number \n")
    # a = int(user_input)
    validate()
