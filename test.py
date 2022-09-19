number = int(input("enter the number"))
factorial = 1
if (number<0):
      print("there is no factorial for negative  number")
else:
      for i in range (1,number+1):
            factorial = factorial * i
            print("",factorial)
