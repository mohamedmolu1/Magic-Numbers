# We are going to create a program where the user is able to enter a magic number however if they pick the number then they win
def magic_number():
  user_value = input("Enter your magic number beteen 0 - 10:  ")
  if user_value < "10":
    print ("this is your magic number {} ".format(int(user_value)))
  elif user_value == "10":
   print("try again")
  else:
    if user_value >"0": 
      print("try again")

magic_number()
magic_number
