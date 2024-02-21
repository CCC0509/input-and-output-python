import random

secretNum = random.randint(1, 101)
min = 1
max = 100


while True:
    guessNum = int(input(f"終極密碼～\n你可以選擇的範圍是{min}~{max}："))
    if guessNum == secretNum:
        print("恭喜猜中密碼")
        break
    elif guessNum < min or guessNum > max or guessNum < 1 or guessNum > 100:
        print(f"你的選擇超出範圍\n")
        continue
    elif secretNum < guessNum:
        max = guessNum
    elif guessNum < secretNum:
        min = guessNum
