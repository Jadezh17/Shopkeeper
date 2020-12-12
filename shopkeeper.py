import sys
starting_price = float(sys.argv[1])
minimum_price = float(sys.argv[2])
stock = int(sys.argv[3])

day = 1
sell = 0
Yesterday_sell = int(0)
Sales = 0

while stock>0 and minimum_price <= starting_price:
	print(">", end = " ")
	inp = str(input( ))
	if inp == "bye":
		print("You made ${:.2f} in sales!\n".format(Sales))
		break
	elif inp == "sell":
		sell +=1
		stock -=1
		print("Sold 1 item\n")
		Sales = Sales + 1 * starting_price
	elif inp == "info":
		print("Day "+ str(day))
		print("Current price: ${:.2f}".format(starting_price))
		print("Current sales: ${:.2f}".format(Sales))
		print("Stock left: {}".format(stock))
		print("{} item(s) sold yesterday".format(int(Yesterday_sell)))
		print("{} item(s) sold so far today\n".format(sell))
	elif inp == "next":
		if Yesterday_sell > sell:
			starting_price -= 0.10
		Yesterday_sell=sell
		print("Summary of day {}: {} item(s) sold\n".format(day,Yesterday_sell))
		sell = 0
		day +=1
		if starting_price < minimum_price:
			starting_price = minimum_price
	else:
		print("Invalid command\n")
	if stock == 0:
		print("No more stock!\n")
		print("You made ${:.2f} in sales!\n".format(Sales))
		break	
	
	
	
		
		
	
		

