def get_user_input():
    user_input=input("Enter a list of integers,separated by spaces:")
    return user_input
def process_input(user_input):
    result=[]
    for num in user_input.split():
        if int(num)>100:
            result.append("over")
        else:
            result.append(num)
    return result
def main():
    user_input=get_user_input()
    result=process_input(user_input)
    print(result)
if __name__ == "__main__":
    main()


















    
