# Counterfeit Coin Algorithm | Gur Shulman (Sep 2021)

## The Counterfeit Coin Problem
- You have 9 coins.
- 8 of the coins weigh the same, but one of the coins is counterfeit and weighs less than the others.

The Goal:
- Find the counterfeit coin, by using only a balance, only twice (two weighings).

### Solution:
<details> 
  <summary>Show Solution
 </summary>
		
		Let's start by numbering the coins 1 to 9.
		Put 1,2 & 3 on the left side and 4,5 & 6 on the right side.
		There are three possible outcomes:
		- scale tilts right - means the counterfeit coin is in group 1,2 & 3
		- scale tilts left - means the counterfeit coin is in group 4,5 & 6
		- scale balances - means the counterfeit coin is in group 7,8 & 9

		Using one weighing we have successfully narrowed three groups down to one.

		We need to do the same again and we will arrive at the final coin.
		Let's label the three coins we have narrowed it down to as A, B & C - Putting A on the left side, B on the right, and C to the side.
		- A goes down - B is the counterfeit coin.
		- B goes down - A is the counterfeit coin.
		- Neither goes down - C is the counterfeit coin.
		
		That way, we can always find the counterfeit coin, in only 2 steps (weighings).
</details>

### You can try and solve the problem, for 9 coins, or for as many coins as you want.

## The Algorithm:

### The purpose of the algorithm is to find the counterfeit coin from any number of coins, in the same way as described in the question, in the least weighs possible, while showing the steps (visually).

- The algorithm gets the initial number of coins (9 coins in the original problem).
- The coins get created, with a number assigned to each coin.
- All coins get the same weight (5), and one of the coins is randomly chosen - the counterfeit coin, which gets a lighter weight (4). 
- It finds the best and optimal way (the one with the least weighs possible) to find the coin, by iterating the following step:
	- The current pile of coins gets OPTIMALLY divided into 3 groups, while always making group 1 and 2 The same amount of coins.
	- The two equal-weighted groups (groups 1 and 2) get weighted and compared to each other, while the 3rd group is kept on the side.
	- If one of the groups weigh less, it means the counterfeit coin is in that group, and the algorithm chooses that lighter group.
	- If the groups weigh the same, the algorithm than chooses the group on the side (group 3), as the counterfeit coin is there.
	- The algorithm prints out (visually) the weigh and the weigh's result.
	- (The algorithm then continues and repeat the same process with the chosen pile).
- Eventually, the (1) counterfeit coin is found.
- The algorithm prints out the number of the counterfeit coin, and how many steps it takes to find it.


### Please leave a comment with any question, problem, or idea you might have - I'd love to hear those!


**Gur Shulman | Sep 2021**

<!---
GuiShulman/GuiShulman is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
