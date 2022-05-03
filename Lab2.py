def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    userinput = []
    str = input()
    userinput = str.split(",")
    for i in range(len(userinput)):
        userinput[i] = int(userinput[i])
    return userinput
def calc_average_temperature(userinput):
    total = 0
    for i in range(len(userinput)):
        total=total+userinput[i]
        avg=total/(i+1)
    print("Average is ",avg)
def calc_min_max_temperature(userinput):
    max = userinput[0]
    min = userinput[0]
    for i in range(len(userinput)):
        if(max<userinput[i]):
            max=userinput[i]
        if(min>userinput[i]):
            min=userinput[i]
    print("Maximum is ",max)
    print("Minimum is ",min)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    userinput = get_user_input()
    calc_average_temperature(userinput)
    calc_min_max_temperature(userinput)
if __name__ == "__main__":
    main()
