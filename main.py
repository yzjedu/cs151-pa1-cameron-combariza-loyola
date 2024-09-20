#Enter product sell, product cost, and quantity purchased 

sell_price = int(input("Enter sales price: ")) 

cost_price = int(input("Enter product cost : ")) 

quantity = int(input("Enter quantity: ")) 

 

#divide product sell from quantity 

#BEP, break even point 

BEP = cost_price * quantity 

#BEP divided by selling price 

num_product = BEP / sell_price 

 

#Print products sold to make profit 

print (“Items need to make profit :”, num_product) 

 

#profit per product 

profit_per_product = sell_price – cost_price 

print(“profit per product :”, profit_per_product) 

 
