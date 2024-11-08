
def fact(num):
    if num == 1 or num == 0:
        return 1;
    return num*fact(num-1)

def func(n):
    res=0
    for i in range(0, n+1):
       res+=(n**i)/fact(i)
    return res


def print_message():
  print('Hello from github')
print_message()  
