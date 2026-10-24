def estimate(start, target, games, p=0.5):
    a=games
    count_win=0
    list_round=[]
    while games >0:
        final_coins, number_of_rounds = play_game(start, target,p)
        if final_coins == target:
            count_win +=1
            list_round.append(number_of_rounds)
        games-=1
    fraction_of_wins = round(count_win/a,2)
    average_number_of_rounds = round(sum(list_round)/count_win)
    return fraction_of_wins, average_number_of_rounds

print(estimate(5, 10, 5000))
