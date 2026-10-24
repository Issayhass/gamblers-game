# think and explain

jp_m = {}
for i in range(20):
    jp_m[play_game(10, 50, p=0.5)[1]] = i+1
for i in jp_m.keys():
    print(i,end=' ')
longest_game = jp_m[max(jp_m.keys())]
print('\nthe longest game is game number :', longest_game)
shortest_game = jp_m[min(jp_m.keys())]
print('the shortest game is game number :',shortest_game)