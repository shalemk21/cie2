import sys
def check_even_odd(num):
    if(num%2==0):
        return f"{num} is Even"
    else:
        return f"{num} is Odd"


if __name__=="__main__":
    print("Enter the number: ")
    num=sys.argv[1]
    print(check_even_odd(num))