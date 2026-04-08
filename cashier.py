name  = input("Enter your name --> ")
print("You are welcome",name)


total_sum = 0.0

b = False
while b == False:

    price = input("Entre the price of item ---> ")
    print (price)
    if price == "done":
       
       b =True
    else:
        price = float(price)
        print(price)
        total_sum = total_sum + price
if price=="done":
    b = True
    if total_sum>=500:
        subtotal = total_sum-(total_sum*0.10)
        gst = (subtotal*0.12)+subtotal
        gpt = total_sum + (subtotal * 0.12) 
    print(f"Your total price is ---->",total_sum,"\nYour subtotal bill is ",subtotal,"rupees\nwith gst of 12% ",gst,"GRAND TOTAL PRICE = ",gpt,"rupees")
elif total_sum<500 :
     op = (total_sum*0.12)+total_sum
     
print(f"Your total price is ---->{total_sum} \nwith gst of 12% {op}")
ou = op
print ("GRAND TOTAL PRICE = {ou} rupees")