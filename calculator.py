def calculator():
  print("Hello welcome to this simple calculator")
  while True:
     print("Press 1 ->for addition:")
     print("Press 2 ->for substraction:")
     print("Press 3 ->for multiplication:")
     print("Press 4 ->for division:")
     print("Press 5 ->for exit:")
     ch=int(input("Enter your choice:"))
     if(ch==5):
        print("-------Thank you for using this calculator--------")
        break
     x=int(input("Enter first Number:"))
     y=int(input("Enter first Number:"))
     def addition():
        print("Sum of given numbers comes out to be:",x+y)
     def substraction():
        print("Difference of given numbers comes out to be:",x-y)
     def multiplication():
        print("Product of given numbers comes out to be:",x*y)
     def division():
        if(y!=0):
         print("Division of given numbers comes out to be:",x/y)
        else:
         print("Division by 0 is not possible")
     if(ch==1):
        addition()
     if(ch==2):
        substraction()
     if(ch==3):
        multiplication()
     if(ch==4):
        division()
calculator()
