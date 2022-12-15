# USER INPUT HANDLING

def handleUserInput(prompt_string):

  user_input = input(prompt_string)
  if user_input == "\exit":
    print ("\nThanks for learning. Come back soon to pick up where you left off! \n")
    exit(0)
  if user_input == "\home":
    from viper import viper_main
    viper_main()
  else:
    return user_input


def handleUserInput_stringOnly(prompt_string):

  while True: # this will continously ask user for input until a break condition
    user_input = input(prompt_string)
    if user_input == "\exit":
      print ("\nThanks for learning. Come back soon to pick up where you left off! \n")
      exit(0)
    if user_input == "\home":
      from viper import viper_main
      viper_main()
    if not user_input.isalpha(): # this is for if user enters a string with an int 
      print ("\nPlease enter a valid non-numeric input.\n")
    if user_input.isalpha(): # this is only True if the string is only alphabetical
      break

  return user_input