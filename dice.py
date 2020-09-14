from random import choices
ntrials=15000
player1wins=0
for i in range(ntrials):
    n_dice1=2
    n_dice2=3
    dice1=choices(range(1,7), k=n_dice1)
    if dice1[0]==dice1[1]:
        player1wins +=1

    dice2 = choices(range(1, 7), k= n_dice2)
    dice2.sort(reverse=True)
    sum1 = dice1[0]+dice1[1]
    sum2 = dice2[0]+dice2[1]
    if sum1 >= sum2:
        player1wins +=1
print("average roll=",player1wins/ntrials)
