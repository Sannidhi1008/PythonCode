num1 = int (input ("1st Number ")) 
num2 = int (input ("2nd Number ")) 

#if num1 is greater than num2
if num1 > num2:
    print (str (num1) + " is greater than " + str (num2))

#if num1 is equal to num2
elif num1==num2:
    print(str(num1) +" is equal to "+str(num2))

#if num2 is greater than num1
else:
    print (str (num2) + " is greater than " + str (num1))
