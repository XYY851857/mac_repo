data = [
    ["女巫", "鬼", "蝙蝠", "糖果"],
    ["蜘蛛", "蜘蛛", "糖果", "女巫"],
    ["鬼", "南瓜", "蝙蝠", "鍋子"],
    ["墓碑", "墓碑", "南瓜", "鍋子"],
    ["南瓜", "女巫", "女巫", "蜘蛛"],
    ["墓碑", "鬼", "墓碑", "鬼"],
    ["鍋子", "糖果", "糖果", "蝙蝠"],
    ["鍋子", "蜘蛛", "蝙蝠", "南瓜"],
    ["墓碑", "蜘蛛", "糖果", "糖果"],
    ["南瓜", "蜘蛛", "鬼", "鍋子"],
    ["女巫", "墓碑", "蝙蝠", "蝙蝠"],
    ["南瓜", "鍋子", "女巫", "鬼"],
    ["糖果", "南瓜", "墓碑", "鍋子"],
    ["鬼", "鬼", "女巫", "蜘蛛"],
    ["女巫", "蜘蛛", "蝙蝠", "糖果"],
    ["鍋子", "墓碑", "南瓜", "蝙蝠"],
    ["鬼", "墓碑", "蜘蛛", "鍋子"],
    ["蜘蛛", "女巫", "蝙蝠", "墓碑"],
    ["女巫", "鬼", "糖果", "南瓜"],
    ["南瓜", "蝙蝠", "鍋子", "糖果"],
    ["女巫", "墓碑", "鍋子", "鬼"],
    ["鬼", "女巫", "蝙蝠", "糖果"],
    ["蜘蛛", "墓碑", "南瓜", "糖果"],
    ["蝙蝠", "蜘蛛", "南瓜", "鍋子"]
]


def process_data(data):
    # 初始化元素次數的字典
    element_count = {}

    # 初始化每局遊戲元素的排列情況列表
    game_arrangements = []

    # 遍歷每局遊戲
    for game in data:
        game_arrangement = ', '.join(game)
        game_arrangements.append(game_arrangement)

        # 遍歷每個元素，更新次數
        for element in game:
            element_count[element] = element_count.get(element, 0) + 1

    return element_count, game_arrangements


element_count, game_arrangements = process_data(data)

# 顯示每個元素的出現次數
print("每個元素的出現次數:")
for element, count in element_count.items():
    print(f"{element}: {count}")

# 顯示每局遊戲元素的排列情況
print("\n每局遊戲元素的排列情況:")
for i, arrangement in enumerate(game_arrangements, 1):
    print(f"Game {i}: {arrangement}")
