import time
from dialogue_data import safe_input, say, say_multiline,split_clues
def interact_with_lanyi(events_log, clues, variables, lang='en'):

    """
    与沈澜衣的互动分支
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合（set）
    :param variables: 其他状态变量，如 {'emotion_lanyi': 0, 'suspect_lanyi': 0, 'truth_window_lanyi', 'love_points': 0}
    :param lang: "zh" or "en"
    """

    print(say("lanyi_intro_scene", lang))
    print(say("lanyi_profile", lang))

    while True:
        print(say("chat_start_prompt", lang))

        print("1. " + say("lanyi_choice_1", lang))
        print("2. " + say("lanyi_choice_2", lang))
        print("3. " + say("lanyi_choice_3", lang))
        print("4. " + say("lanyi_choice_4", lang))
        print("5. " + say("lanyi_choice_5", lang))
        print("6. " + say("lanyi_choice_6", lang))


        choice=input(say("input_prompt",lang))
        if choice == "1":
            print(say("ask_lanyi_father", lang))
            clues.add(say("clue_fake_death_truth", lang)) 
            events_log.append(say("log_ask_lanyi_fake_death", lang)) 

        elif choice == "2":
            print(say("ask_lanyi_love", lang))
            print(say("lanyi_love_details", lang))
            
            #variables['love_points'] = variables.get('love_points', 0) + 1 #debug use
            variables['emotion_lanyi'] = variables.get('emotion_lanyi', 0) + 1
            events_log.append(say("log_talk_lanyi_love", lang)) 

            if variables.get('truth_window_lanyi', False) and variables.get('love_points', 0) >= 3:
                say_multiline("lanyi_confess_poison_truth", lang)
            else:
                say_multiline("lanyi_love_story_past", lang) 
                variables['love_points'] = variables.get('love_points', 0) + 1 

        elif choice == "3":
            print(say("ask_lanyi_poison", lang))
            print(say("lanyi_suspicion", lang)) 
            variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
            events_log.append(say("log_question_lanyi_poison", lang))

        elif choice == "4":
            print(say("lanyi_sleeve_obs_result", lang)) 
            clues.add(say("clue_green_trace_1", lang)) 
            events_log.append(say("log_observe_lanyi_sleeve", lang)) 
            variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
        
        elif choice == "5":
            print(say("comfort_lanyi", lang))
            variables['emotion_lanyi'] = variables.get('emotion_lanyi', 0) + 1 
            events_log.append(say("log_comfort_lanyi", lang))
            variables['truth_window_lanyi'] = True
            
            # debug line below
            # variables['love_points'] = variables.get('love_points', 0) + 1 

        elif choice == "6":
            print(say("leave_lanyi", lang))
            break

        else:
            print(say("invalid_input", lang))
