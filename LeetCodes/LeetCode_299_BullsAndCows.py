"""
這題目敘述有點長，我記得以前這是以前堂哥跟我玩的(猜數字遊戲)[http://codepen.io/skyyen999/full/VedwqQ/]，上面那一大串英文的意思是，這邊有一串隱藏的號碼(secret number)，然後你朋友會猜一串號碼， 如果號碼數字與位置都對了，給一個bull，數字對但位置不對，給一個cow。
範例:
Secret number:  "1807"
Friend's guess: "7810"
上面範例可以發現8得到一個bull，剩下1,0,7得到一個cow，所以得到1A3B
Secret number:  "1123"
Friend's guess: "0111"
第二個範例，第二個1得到一個bull，Friend's guess 第三個1得到一個cow(比對secret number的第一個1)，因此得到1A1B
"""
import random
import random as r


def game_chunk(guess, secret_num):
    if guess == 'GG':
        print(f'GameOverLoser Ans : {secret_num}')
        return False
    guess = list(guess)
    if len(guess) != 4:
        print('輸入的不是四位數')
        return True
    duplicate = False
    for i in range(0, 3):
        for j in range(i+1, 4):
            if guess[i] == guess[j]:
                print('輸入的數字不可重複，請更正')
                duplicate = True
                return True
        if duplicate:
            break
    if not duplicate:
        if guess == secret_num:
            report = algo(guess, secret_num)
            print(f"Graduation~~ANS:{secret_num}")
            return False
        else:
            report = algo(guess, secret_num)
        print(f'{report[0]}A{report[1]}B')
        return True

def generate_secret_num():
    # return random.sample(range(10),4)  # from ChatGPT BUGGGGGGG!!!!
    while True:
        secret_num = r.randint(1, 9999)
        secret_num = list(str(secret_num))
        if len(secret_num) != 4:
            continue
        duplicate = False
        for i in range(0, 3):
            for j in range(i+1, 4):
                if secret_num[i] == secret_num[j]:
                    duplicate = True
                    break
            if duplicate:
                break
        if not duplicate:
            return secret_num
    return False


def algo(guess_algo, secret_num_algo):
    count_a, count_b = 0, 0
    for i in range(4):
        if guess_algo[i] == secret_num_algo[i]:
            count_a += 1
    for i in range(4):
        if guess_algo[i] != secret_num_algo[i] and guess_algo[i] in secret_num_algo:
            count_b += 1
    count = [count_a, count_b]
    return count


if __name__ == '__main__':
    secret_num = generate_secret_num()
    print('\n~~  Bulls And Cows Game  ~~')
    print('RULE : 數字不重複。輸入“GG”可提前結束遊戲')
    while True:
        report = []
        guess = input('輸入四位數字 ： ')
        if not game_chunk(guess, secret_num):
            break
