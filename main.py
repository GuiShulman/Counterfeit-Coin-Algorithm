################################
#  Counterfeit Coin Algorithm  #
#  Gur Shulman | Sep 2021      #
################################

from random import randrange, uniform


# Getting an input from the user - how many coins to solve for.

while True:
	n_coins = 0
	try:
		n_coins = int(input("How many coins do you want? > "))
	except: pass
	if n_coins > 1:
		break
	else:
		print("Please enter the number of coins you want. \n(It must be and integer, bigger than 1)")


# Generate the chosen number of coins, with one random counterfeit coin, and assgining weights to the coins.

coins = {}
for coin in range(1, n_coins + 1):
	coins[coin] = 5

random_coin = randrange(1, n_coins)
coins[random_coin] = 4

print(f"\nGenerated {n_coins} coins.\nOne of the coins is Counterfeit, and weighs less than all the other coins.")


# (Optimaly) Devide to groups function
def group(current_coins):
	group_1, group_2, group_3 = {}, {}, {}
	if len(current_coins) != 2:
		a = len(current_coins) // 3
		b = len(current_coins) // 3
		if len(current_coins) % 3 == 0:
			c = len(current_coins) // 3
		else:
			c = len(current_coins) // 3 + len(current_coins) % 3
	else:
		a, b, c = 1, 1, 0
	for coin in current_coins:
		if list(current_coins.keys()).index(coin) + 1 <= a:
			group_1[coin] = current_coins[coin]
		elif list(current_coins.keys()).index(coin) + 1 <= a+b:
			group_2[coin] = current_coins[coin]
		elif list(current_coins.keys()).index(coin) + 1 <= a+b+c:
			group_3[coin] = current_coins[coin]
	return group_1, group_2, group_3


# Weighing function - comparing groups 1 & 2, 3 is kept on the side.
def weigh(group_1, group_2, group_3):
	weight_1, weight_2 = 0, 0
	
	weight_1 = sum(group_1.values())
	weight_2 = sum(group_2.values())

	if len(group_3) == 0:
		leftout = ""
	else:
		leftout = f"({len(group_3)})"
	spaces = 15 - len(str(len(group_1)))

	if weight_1 > weight_2:
		print(" |---HEAVIER---||-------------|")
		print("/\             ||             /\ ")
		print(str(len(group_1)) + spaces * " " + "||" + spaces * " " + str(len(group_2)))
		print("               ||               ")
		print("               ||               ")
		print("             ======        ",leftout)
		group_name = "RIGHT"
		print(f"Chose {group_name} group for next step.")
		print("\n")
		return "1"
	elif weight_1 < weight_2:
		print(" |-------------||---HEAVIER---|")
		print("/\             ||             /\ ")
		print(str(len(group_1)) + spaces * " " + "||" + spaces * " " + str(len(group_2)))
		print("               ||               ")
		print("               ||               ")
		print("             ======        ",leftout)
		group_name = "LEFT"
		print(f"Chose {group_name} group for next step.")
		print("\n")
		return "2"
	else:
		print(" |-------------||-------------|")
		print("/\             ||             /\ ")
		print(str(len(group_1)) + spaces * " " + "||" + spaces * " " + str(len(group_2)))
		print("               ||               ")
		print("               ||               ")
		print("           EQUALWEIGHT     ",leftout)
		group_name = "NOT MEASSURED"
		print(f"Chose {group_name} group for next step.")
		print("\n")
		return "="


# Making the algorithm do its thing
current_coins = coins
steps = 0

print("\n")

while len(current_coins) != 1: # While the counterfeit coin was yet to be found...
	steps += 1
	print(f"STEP: [{steps}]")
	group_1, group_2, group_3 = group(current_coins)

	w_result = weigh(group_1, group_2, group_3)
	if w_result == "=":
		current_coins = group_3
	elif w_result == "1":
		current_coins = group_2
	elif w_result == "2":
		current_coins = group_1


# counterfeit coin was found
fake = list(current_coins.keys())[0]
print(f"*************************************\n\nThe counterfeit coin is coin number {fake}/{str(n_coins)}.\nIt takes {steps} steps to find the coin.")
