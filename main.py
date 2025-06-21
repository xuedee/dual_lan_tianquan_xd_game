from chen import interact_with_chen
from lanyi import interact_with_lanyi
from lin import interact_with_lin
from miaoyin import interact_with_miaoyin
from butler import interact_with_butler
from jing import interact_with_jing
from endings import make_final_judgment
from clues_log import view_log_and_clues
from dialogue_data import safe_input, say, DIALOGUES 


"""
xd_tianquan_game_project/
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



def accuse_culprit_menu(lang):
    """
    提示玩家选择最终指认的凶手。
    返回被指认角色的键名 (例如 'lin', 'lanyi') 
    或 None (如果玩家选择返回)。
    """
    while True:
        print("\n" + say("accuse_prompt", lang))
        print("1. " + say("character_lanyi", lang))
        print("2. " + say("character_chen", lang))
        print("3. " + say("character_lin", lang))
        print("4. " + say("character_miaoyin", lang))
        print("5. " + say("character_butler", lang))
        print("6. " + say("character_jing", lang))
        print("0. " + say("accuse_cancel", lang)) # 选项：返回主菜单

        #accuse_choice_num = input(say("input_prompt", lang))

        #for code in place auto run use only
        accuse_choice_num = safe_input(say("input_prompt", lang), default="1")

        if accuse_choice_num == "1": return 'lanyi'
        elif accuse_choice_num == "2": return 'chen'
        elif accuse_choice_num == "3": return 'lin'
        elif accuse_choice_num == "4": return 'miaoyin'
        elif accuse_choice_num == "5": return 'butler'
        elif accuse_choice_num == "6": return 'jing'
        elif accuse_choice_num == "0": return None # 玩家选择返回主菜单
        else:
            print(say("invalid_input", lang))




def choose_language():
    print("Choose your language / 请选择语言：")
    print("1. English")
    print("2. 中文")
    #choice = input("Enter your choice / 输入你的选择（1或2）：")
    
    

    # for code in place auto run only
    choice = safe_input("Enter your choice / 输入你的选择（1或2）：", default="1")



    return "zh" if choice == "2" else "en"

def get_player_name(lang):
    """
    Asks the player for their name.
    If the input is empty (space or just enter), uses a default name.
    """
    default_name_zh = "慕容泓" # Default Chinese name
    default_name_en = "Murong Hong" # Default English name

    name_prompt_key = "player_name_prompt"
    
    # Get the appropriate prompt for the chosen language
    prompt = say(name_prompt_key, lang)
    
    player_name = input(prompt).strip() 

    # .strip() removes leading/trailing whitespace including spaces

    if not player_name: 
        # If name is empty after stripping (e.g., just Enter or spaces)
        return default_name_zh if lang == "zh" else default_name_en
    else:
        return player_name

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
        'lin_confessed_poison_triggered': False,
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
    # Language selection
    lang = choose_language()
    # Pass language to initial interaction
    
  

    # Get player name right after language selection
    player_actual_name = get_player_name(lang)

    print("\n"+say("game_welcome",lang))
   
    print(say("player_intro", lang).format(player_name=player_actual_name))



 

    while True:
        
        
        # Main menu prompt
        print("\n" + say("main_menu_prompt", lang)) 
        print("1. " + say("character_lanyi", lang))
        print("2. " + say("character_chen", lang))
        print("3. " + say("character_lin", lang))
        print("4. " + say("character_miaoyin", lang))
        print("5. " + say("character_butler", lang))
        print("6. " + say("character_jing", lang))
        print("7. " + say("menu_view_log_clues", lang))
        print("0. " + say("menu_end_investigation", lang))

      
        #choice = input(say("input_prompt",lang))

        

        # for code in place auto run only
        choice = safe_input(say("input_prompt",lang), default="1")




        if choice == "1":
            interact_with_lanyi(events_log, clues, variables, lang)
        elif choice == "2":
            interact_with_chen(events_log, clues, variables, lang)
        elif choice == "3":
            interact_with_lin(events_log, clues, variables, lang)
        elif choice == "4":
            interact_with_miaoyin(events_log, clues, variables, lang)
        elif choice == "5":
            interact_with_butler(events_log, clues, variables, lang)
        elif choice == "6":
            interact_with_jing(events_log, clues, variables, lang)
        elif choice == "7":
            view_log_and_clues(events_log, clues, variables, lang)
        elif choice == "0":
            
            accused_char_key = accuse_culprit_menu(lang)
            if accused_char_key is not None:
                
                make_final_judgment(clues, variables, events_log, lang, accused_char_key)
                break
        else:
            
            print(say("invalid_input",lang))


if __name__ == "__main__":
    main()
