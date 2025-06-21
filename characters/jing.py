import time
from dialogue_data import safe_input, say, say_multiline, split_clues 
# Ensure split_clues is imported if needed


def interact_with_jing(events_log, clues, variables, lang="en"):
    """
    与静慧师太的互动模块
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合
    :param variables: 状态变量 dict，如 {'emotion_jing': 0, 'suspect_jing': 0,'truth_window_jing'}
    :param lang: "zh" or "en"-language
    """

    print(say("jing_profile", lang))
    print(say("jing_greeting", lang))

    while True:
        
        print(say("chat_start_prompt", lang))
        
        print("1. " + say("jing_choice_1", lang))
        print("2. " + say("jing_choice_2", lang))
        print("3. " + say("jing_choice_3", lang))
        print("4. " + say("jing_choice_4", lang))
        print("5. " + say("jing_choice_5", lang))

        
        choice = input(say("input_prompt", lang))

        if choice == "1":
            
            print(say("jing_relation_chen_response", lang))
            variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
            variables['suspect_chen'] = variables.get('suspect_chen', 0) - 1
            
            events_log.append(say("log_jing_talk_chen", lang))
        
        elif choice == "2":
            
            
            say_multiline("jing_reason_late_dialogue", lang)

            variables['truth_window_jing'] = True
            # active Jing truth window
           
            variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
            
            events_log.append(say("log_jing_ask_why_late", lang))
        
        elif choice == "3":
            
            if variables.get('truth_window_jing', False): 
            # Using .get for safety process
            # try to get "truth_window_jing" from variables, if exists, return True, and run code inside "if"; 
            # otherwise, "truth_window_jing" is False by default.
            
                

                say_multiline("jing_disciple_testimony", lang)
            
                
                events_log.append(say("log_jing_suspect_lanyi_secret", lang))

                variables['suspect_jing'] = variables.get('suspect_jing', 0) - 1 # Reduce suspicion on Jing
                variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
                variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1 # Increase suspicion on Lanyi
                


            else:
                

                say_multiline("jing_no_abnormalities_dialogue", lang) 
                variables['suspect_jing'] = variables.get('suspect_jing', 0) + 1
                variables['emotion_jing'] = variables.get('emotion_jing', 0) - 1
                
                events_log.append(say("log_jing_suspect_jing", lang))
        
        elif choice == "4":
            
            print(say("jing_hand_observation_result", lang))
            
            
            clues.add(say("clue_jing_powder_trace", lang))

            
            events_log.append(say("log_jing_observe_hand_powder", lang))
            
            
            if variables.get('truth_window_jing', False):
                variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
                
                ## Increase emotion due to understanding jing was helping people
            else:
                variables['suspect_jing'] = variables.get('suspect_jing', 0) + 1
                #jing might used posion
                # Increase suspicion
        
        elif choice == "5":
            
            print(say("jing_leave_dialogue", lang))
            break

        else:
            
            print(say("invalid_input", lang))
