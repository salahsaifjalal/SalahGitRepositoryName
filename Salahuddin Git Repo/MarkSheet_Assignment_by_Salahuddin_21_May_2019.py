#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assalam-o-Alaikum Dear. This is a Marksheet Program in Python Language, made by Muhammad Salahuddin.

print("Assalam-o-Alaikum Dear. This is a Marksheet Program in Python Language, made by Muhammad Salahuddin.")
print("="*100)

print()

while True:
    input_user_name = input("Welcome Dear! Please Enter Your Good Name: ")   # Get the input
    if input_user_name != "":       # If it is not a blank line...
        break           # ...break the loop
    
while True:             # Loop continuously
    inp1 = input("Please Enter Your First Subject's Name: ")   # Get the input
    if inp1 != "":       # If it is not a blank line...
        break           # ...break the loop

while True:             # Loop continuously
    inp2 = input("Please Enter Your First Subject's Marks Obtained out of 100: ")   # Get the input
    if inp2 != "":
        inp3=float(inp2)
        if inp3 >= 0 and inp3 <=100: 
            break           # ...break the loop


while True:             # Loop continuously
    inp4 = input("Please Enter Your Second Subject's Name: ")   # Get the input
    if inp4 != "":       # If it is not a blank line...
        break           # ...break the loop

while True:             # Loop continuously
    inp5 = input("Please Enter Your Second Subject's Marks Obtained out of 100: ")   # Get the input
    if inp5 != "":
        inp6=float(inp5)
        if inp6 >= 0 and inp6 <=100: 
            break           # ...break the loop

            
while True:             # Loop continuously
    inp7 = input("Please Enter Your Third Subject's Name: ")   # Get the input
    if inp7 != "":       # If it is not a blank line...
        break           # ...break the loop

while True:             # Loop continuously
    inp8 = input("Please Enter Your Third Subject's Marks Obtained out of 100: ")   # Get the input
    if inp8 != "":
        inp9=float(inp8)
        if inp9 >= 0 and inp9 <=100: 
            break           # ...break the loop
            
Total_Marks_Gained =float(inp3+inp6+inp9)
Percentage=float((Total_Marks_Gained*100)/300)
print()
print("This is a MarkSheet of", input_user_name,'.')
print()

if (Percentage >= 80):
    print("Your Total Marks Obtained is:",  Total_Marks_Gained  ,"\nYour Percentage is: ",Percentage,"%"  ,"\nYou got A-1 grade.")
elif (Percentage >= 70):
    print("Your Total Marks Obtained is:",  Total_Marks_Gained  ,"\nYour Percentage is: ",Percentage,"%"  ,"\nYou got A grade.")
elif (Percentage >= 60):
    print("Your Total Marks Obtained is:",  Total_Marks_Gained  ,"\nYour Percentage is: ",Percentage,"%"  ,"\nYou got B grade.")
elif (Percentage >= 50):
    print("Your Total Marks Obtained is:",  Total_Marks_Gained  ,"\nYour Percentage is: ",Percentage,"%"  ,"\nYou got C grade.")
elif (Percentage>=40 or Percentage<40):
    print("Your Total Marks Obtained is:",  Total_Marks_Gained  ,"\nYour Percentage is: ",Percentage,"%"  ,"\nYou got D grade.", "\nYou Failed.")
             

