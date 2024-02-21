# 設定9公格
counter = 0
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

# 顯示


def display(*args):
    print(args[0])
    print(args[1])
    print(args[2])

# 選擇位置


def user_choise():
    choise = input("請選擇1～9之間的數字：")
    while not choise.isdigit() or int(choise) not in (range(1, 10)):
        if not choise.isdigit():
            print("請輸入數字。。。")
        else:
            print("請輸入範圍在1～9之間的數字。。。")
        choise = input("請選擇1～9之間的數字：")
    return int(choise)

# 依照順序顯示符號


def get_current_symbol():
    global counter
    symbol_list = ["X", "O"]
    counter += 1
    return symbol_list[counter % 2]

# 當選擇對應位置時，要改變符號


def update_table(index):
    global row1, row2, row3
    if index in range(1, 4):
        if row1[index-1] == " ":
            row1[index-1] = get_current_symbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3-1] == " ":
            row2[index % 3-1] = get_current_symbol()
            return True
        else:
            return False
    elif index in range(7, 10):
        if row3[index % 3-1] == " ":
            row3[index % 3-1] = get_current_symbol()
            return True
        else:
            return False

# 當達成勝利條件時就結束遊戲


def check_winning():
    global counter
    player1_wins = False
    player2_wins = False
    if row1[0] == row1[1] and row1[1] == row1[2] and " " not in row1:
        if (row1[0] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row2[0] == row2[1] and row2[1] == row2[2] and " " not in row2:
        if (row2[0] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row3[0] == row3[1] and row3[1] == row3[2] and " " not in row3:
        if (row3[0] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row1[0] == row2[0] and row2[0] == row3[0] and row1[0] != " " and row2[0] != " " and row3[0] != " ":
        if (row1[0] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row1[1] == row2[1] and row2[1] == row3[1] and row1[1] != " " and row2[1] != " " and row3[1] != " ":
        if (row1[1] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row1[2] == row2[2] and row2[2] == row3[2] and row1[2] != " " and row2[2] != " " and row3[2] != " ":
        if (row1[2] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row1[0] == row2[1] and row2[1] == row3[2] and row1[0] != " " and row2[1] != " " and row3[2] != " ":
        if (row1[0] == "X"):
            player2_wins = True
        else:
            player1_wins = True
    elif row1[2] == row2[1] and row2[1] == row3[0] and row1[2] != " " and row2[1] != " " and row3[0] != " ":
        if (row1[2] == "X"):
            player2_wins = True
        else:
            player1_wins = True

    if player1_wins:
        return "player1勝利～"
    elif player2_wins:
        return "player2勝利～"
    else:
        return "平手～"

# 將上面的功能串接在一起


def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            # 確認位置是否重複
            choise = user_choise()
            if update_table(choise):
                break
            print("位置已被選擇，請重新選擇。。。")
        result = check_winning()
        if result == "player1勝利～":
            display(row1, row2, row3)
            print("player1勝利～")
            return
        elif result == "player2勝利～":
            display(row1, row2, row3)
            print("player2勝利～")
            return
        elif result == "平手～" and counter == 9:
            display(row1, row2, row3)
            print("平手～")
            return


start_game()
