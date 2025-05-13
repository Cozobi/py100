import os
import platform

def clear_screen():
  """Clears the terminal screen."""
  input("Press any key to continue")
  system = platform.system()
  if system == "Windows":
    os.system('cls')
  elif system == "Linux" or system == "Darwin":
    os.system('clear')
  else:
    print("Operating system not supported.")

def calculator(bill, tip, people):
    if tip > 0:
        tip=(tip/bill)*100
        
    if bill <= 0:
        print("You should enter a bill greater than 0")
        return 0
    else:    
        if people <= 0:
            print("You need to type the number of people that will be paying") 
            return 0    
        elif  people > 1:
                total = (bill + tip) / people
                print(f"Each person should pay: {round(total,2)}")
        else:
                total = (bill + tip) / people
                print(f"You should pay: {round(total,2)}")
    return total
            
if __name__ == "__main__":
    cont=True
    billing = []
    while cont==True:
        
        print("============ BILL CALCULATOR ============")
        bill= float(input("What was the total bill?: "))
        tip = float(input("How much tip would you like to give?(5,10,15,20,25): "))
        people = int(input("How many people to split the bill?: "))
        
        total=calculator(bill, tip, people)
        
        clear_screen()
        print("\n=========================================================\n")
        sum=input("Would you like to calculate other bill?:(1=yes, 2=no): ")
        
        billing.append(total)
        
        if int(sum) == 2:
            cont = False 
            for x, y in enumerate(billing, start=1):
                print(f"The bill {x} is a total of: {y}")

    