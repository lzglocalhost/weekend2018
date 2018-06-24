import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """0: 石头
1: 剪刀
2: 布
请选择(0/1/2)："""
pwin = 0
cwin = 0

while True:
    ind = int(input(prompt))
    player = all_choice[ind]
    computer = random.choice(all_choice)

    print("Your choice:", player, "computer's choice:", computer)
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
        cwin += 1

    if pwin == 2 or cwin == 2:
        break
