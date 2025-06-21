import time
from dialogue_data import safe_input, say, say_multiline, split_clues

def interact_with_butler(events_log, clues, variables, lang="en"):
    """
    与老管家的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 {'emotion_butler': 0, 'suspect_butler': 0,'truth_window_butler': False}）
    :param lang: "zh" or "en" - The chosen language
    """
   
    print(say("butler_profile", lang))
    print(say("butler_greeting", lang))

    while True:
      

        
        print(say("chat_start_prompt", lang))
        print("1. " + say("butler_choice_1", lang))
        print("2. " + say("butler_choice_2", lang))
        print("3. " + say("butler_choice_3", lang))
        print("4. " + say("butler_choice_4", lang))
        print("5. " + say("butler_choice_5", lang))
        print("6. " + say("butler_choice_6", lang))

      
        choice = input(say("input_prompt", lang))

        if choice == "1":
            say_multiline("butler_reason_fired", lang) 
            clues.add(say("clue_butler_silver_notes", lang)) 
            events_log.append(say("log_ask_butler_fired", lang)) 
            variables['emotion_butler'] = variables.get('emotion_butler', 0) + 1

        elif choice == "2":
            print(say("butler_loyalty_response1", lang)) 
            print(say("butler_loyalty_response2", lang)) 
            events_log.append(say("log_ask_butler_loyalty", lang)) 
            variables['emotion_butler'] = variables.get('emotion_butler', 0) + 1
            variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1
            variables['truth_window_butler'] = True

        elif choice == "3":
            print(say("butler_master_unusual_response1", lang)) 
            print(say("butler_master_unusual_response2", lang)) 
            clues.add(say("clue_will_burned", lang)) 
            events_log.append(say("log_ask_master_unusual", lang)) 
        
        elif choice == "4":
            print(say("butler_altar_observation1", lang)) 
            print(say("butler_altar_observation2", lang)) 
            
            if variables.get('truth_window_butler', False): # Using .get for safety
                say_multiline("butler_hidden_bottle_story", lang) 
                clues.add(say("clue_poison_bottle_1", lang)) 
                events_log.append(say("log_gain_poison_bottle_1", lang)) 
                variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            else:
                print(say("butler_altar_no_hidden_clue", lang)) 
                clues.add(say("clue_altar_spirit_tablet", lang)) 
                events_log.append(say("log_observe_butler_altar", lang)) 
                variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1

        elif choice == "5":
            print(say("butler_accusation_response", lang)) 
            variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1
            events_log.append(say("log_accuse_butler", lang)) 

        elif choice == "6":
            print(say("butler_leave", lang)) 
            break

        else:
            print(say("invalid_input", lang))

