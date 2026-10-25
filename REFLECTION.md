________________________HOW WE WORKED_________________________
Before explaining the content of the program, we worked in four steps: 
We dedicated the first day to a day of reflection, where everyone tried to read the project to get an idea of the content in order to know what is being asked and the tools we will need to do it. 
1.	On the second day, we found ourselves around a table where, in turn, everyone tried to explain what they understood by trying orally to say the algorithm that must be followed to achieve this. 
2.	After the round table, we tried to make sure that we had the same understanding of the points of divergence, while correcting each of our mistakes. 
3.	Once a single algorithm is fixed, we wrote the program. 
So the content here is not the product of one person, but the result of the reflection of all the members of the group.

____________________HOW THE SCRIPT WORK___________________________
This program simulates a game of chance (with random) and estimates, over a large number of games, the probability of winning as well as the average number of rolls needed to reach the objective. It is composed of two functions: play_game, which simulates a single game, and estimate, which repeats this simulation many times to derive statistics.
The play_game(start, target, p=0.5) function simulates only one part of the game.
It’s parameters are :
	start: the number of coins with which the player starts;
	target: the player’s objective to be achieved to win;
	p: the probability of winning a roll (default 0.5).

The game’s rules are :
If start is negative, the function play_game rejects the part and returns the message 'Negatives values unauthorized'.
As long as the player still has coins (start > 0) and has not reached the objective (start < target), the game turn:
a.	we draw a random number between 0 and 1 with random.random();
b.	if this number is less than p, the player wins one coin (start =start + 1);
c.	otherwise, he  loses one coin, and start decreases (start = start- 1);
d.	In both cases, the counter number_of_rounds is incremented.
The game stops in two cases:
a.	victory : start == target (the player has reached the goal);
b.	Ruin : Start == 0 (the player has no more coins).
The function returns a pair final_coins the final number of coins and number_of_rounds, the number of times the probability between 0 and 1 has been generated.

The function estimate(start, target, games, p=0.5)
This function repeats the simulation games times to get reliable statistics and its parameters are :
	start: the number of coins with which the player starts;
	target: the player’s objective to be achieved to win;
	p: the probability of winning a roll (default 0.5).
	games: the number of games to be simulated.

How is it going?

We save the total number of games in a variable (a = games), because games will be decremented in the loop.
We initialize two counters:
a.	count_win: the number of games won;
b.	list_round: The list of roll numbers only for games won.
We call play_game at each iteration. If the game ends with final_coins == target, we increment count_win and add the number of throws to list_round.
We calculate two states :
a.	fraction_of_wins, which is the proportion of wins, calculated as count_win / a, rounded to 2 decimal places. This is an estimate of the probability of winning.
b.	average_number_of_rounds, which is the average number of throws among the winning games, calculated as sum(list_round) / count_win.
At the end the function return the two statistics fraction_of_wins and average_number_of_rounds.

__________________THE PROBLEM WE GET AND HOW WE SOLD IT_________________

Writing the scripts wasn’t the most challenging part of the work but the submission on GitHub was challenging but as a team we help each other to permit every one to submit his work on time. For some case we had to create a new token because we forgot the password of the last one. But at the end we old that it was a great demonstration of team work.

