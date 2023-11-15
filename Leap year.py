year = int(input("Which year do you want to check? "))

# Parent container
if year % 4 == 0:

    # nested
   if year % 100 == 0:

       # Child
     if year % 400 == 0:
         print("A leap year")
     else:
         print("Not a leap year")


   else:
      print("A leap year")


else:
    print("Not a leap year")