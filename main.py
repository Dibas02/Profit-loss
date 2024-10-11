cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))

profit = sp-cp
loss = cp-sp

if cp<= sp:
    print("You got a profit of: ", profit)

else:
    print("You got a loss of: ", loss)