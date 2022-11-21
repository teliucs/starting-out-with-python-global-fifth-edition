# Professional Appliance Service, Inc. offers maintenance and repair services for household appliances. The owner wants to give each of the company’s service technicians a small handheld computer that displays step-by-step instructions for many of the repairs that they perform. To see how this might work, the owner has asked you to develop a program that displays the following instructions for disassembling an Acme laundry dryer:

# Step 1: Unplug the dryer and move it away from the wall.
# Step 2: Remove the six screws from the back of the dryer.
# Step 3: Remove the dryer’s back panel.
# Step 4: Pull the top of the dryer straight up.

def main():
    startup_message()
    input('Press Enter to see Step 1.') 
    
    step_1()
    input('Press Enter to see Step 2.')
    
    step_2()
    input('Press Enter to see Step 3.')
    
    step_3()
    input('Press Enter to see Step 4.') 
    
    step_4()
    
def startup_message():
    print("Hi everybody this is Maneskin.")

def step_1():
    print("# Step 1: Unplug the dryer and move it away from the wall.")
    
def step_2():
    print("# Step 2: Remove the six screws from the back of the dryer.")

def step_3():
    print("# Step 3: Remove the dryer’s back panel.")

def step_4():
    print("# Step 4: Pull the top of the dryer straight up.")

main()