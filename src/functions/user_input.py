

# User input handling

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

  while True: # this effectively traps the user inside the while loop until they enter a string that leads to a break statement
    user_input = input(prompt_string)
    if user_input == "\exit":
      print ("\nThanks for learning. Come back soon to pick up where you left off! \n")
      exit(0)
    if user_input == "\home":
      from viper import viper_main
      viper_main()
    if not user_input.isalpha(): # this is only True if the string is only alphabetical
      print ("\nPlease enter a valid non-numeric input.\n")
    if user_input.isalpha(): # this is only True if the string is only alphabetical
      break

  return user_input