from characters.chen import interact_with_chen
from characters.lanyi import interact_with_lanyi
from characters.lin import interact_with_lin
from characters.miaoyin import interact_with_miaoyin
from characters.butler import interact_with_butler
from characters.jing import interact_with_jing
from endings import make_final_judgment
from clues_log import view_log_and_clues

"""
your_game_project/
│
├── main.py                     # 主入口，运行游戏
├── characters/
│   ├── lanyi.py                # 沈澜衣的分支
│   ├── chen.py                 # 陈奇曼的分支
│   ├── lin.py                  # 林修的分支
│   ├── miaoyin.py              # 妙音仙子的分支
│   └── butler.py               # 管家的分支
│   └── jing.py                 # 静慧师太的分支
│
├── endings.py                 # 结局判断
├── clues_log.py               # 线索/行为日志模块
├── assets/                    # 文本、图像、剧情素材等
└── requirements.txt           # 项目依赖（如果有额外库）

"""


def main():
    clues = set()
    events_log = []
    variables = {
        'emotion_butler': 0,
        'suspect_butler': 0,
        'truth_window_butler': False,
        'emotion_chen': 0,
        'suspect_chen': 0,
        'emotion_lin': 0,
        'suspect_lin': 0,
        'truth_window_lin': False,
        'love_points': 0,
        'emotion_lanyi': 0,
        'suspect_lanyi': 0,
        'truth_window_lanyi': False,
        'emotion_miaoyin': 0,
        'suspect_miaoyin': 0,
        'truth_window_miaoyin': False,
        'emotion_jing': 0,
        'suspect_jing': 0,
        'truth_window_jing': False
    }

    print("🎮 欢迎来到《天泉山庄疑案》")
    print("你是清音阁特使执事澹台洛林，应掌教穆长风之命，协助调查天泉山庄沈天正庄主之死。")

    while True:
        print("\n请选择你要调查的角色：")
        print("1. 沈澜衣")
        print("2. 陈奇曼")
        print("3. 林修")
        print("4. 妙音仙子")
        print("5. 老管家")
        print("6. 静慧师太")
        print("7. 查看调查日志")
        print("0. 结束调查，进行推理")

        choice = input("你的选择是：")

        if choice == "1":
            interact_with_lanyi(events_log, clues, variables)
        elif choice == "2":
            interact_with_chen(events_log, clues, variables)
        elif choice == "3":
            interact_with_lin(events_log, clues, variables)
        elif choice == "4":
            interact_with_miaoyin(events_log, clues, variables)
        elif choice == "5":
            interact_with_butler(events_log, clues, variables)
        elif choice == "6":
            interact_with_jing(events_log, clues, variables)
        elif choice == "7":
            view_log_and_clues(events_log, clues, variables)
        elif choice == "0":
            make_final_judgment(clues, variables, events_log)
            break
        else:
            print("无效输入，请重新选择。")

# 测试流程
if __name__ == "__main__":
    main()