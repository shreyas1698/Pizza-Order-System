# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    total_bill = 15
    if add_pepperoni == 'Y':
        total_bill = total_bill + 2
    if extra_cheese == 'Y':
        total_bill = total_bill + 1
        print(f'Your final bill is: ${total_bill}.')
    else :
        print(f'Your final bill is: ${total_bill}.')
elif size == 'M':
    total_bill = 20
    if add_pepperoni == 'Y':
        total_bill = total_bill + 3
    if extra_cheese == 'Y':
        total_bill = total_bill + 1
        print(f'Your final bill is: ${total_bill}.')
    else :
        print(f'Your final bill is: ${total_bill}.')
elif size == 'L':
    total_bill = 25
    if add_pepperoni == 'Y':
        total_bill = total_bill + 3
    if extra_cheese == 'Y':
        total_bill = total_bill + 1
        print(f'Your final bill is: ${total_bill}.')
    else :
        print(f'Your final bill is: ${total_bill}.')
else : 
    print('Please select the size to order a pizza')

