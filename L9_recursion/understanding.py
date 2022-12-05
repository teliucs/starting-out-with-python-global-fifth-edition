# This program has a recursive function.

def main(): 
  # By passing the argument 5 to the message 
  # function we are telling it to display the 
  # message five times.
  message(5)
  
def message(times):
    print(times)
    print('------')
    if times > 0:
        message(times - 1)
        print(times)

# Call the main function. 
main()