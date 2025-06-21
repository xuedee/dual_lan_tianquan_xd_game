import time
from dialogue_data import safe_input, say, say_multiline, split_clues

def interact_with_miaoyin(events_log, clues, variables, lang="en"):
    """
    与妙音仙子的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 'emotion_miaoyin', 'suspect_miaoyin','truth_window_miaoyin'）
    :param lang: "zh" or "en" - The chosen language
    """

    print(say("miaoyin_profile", lang))
    print(say("miaoyin_greeting", lang))

    while True:
        
        print(say("chat_start_prompt", lang))

        print("1. " + say("miaoyin_choice_1", lang))
        print("2. " + say("miaoyin_choice_2", lang))
        print("3. " + say("miaoyin_choice_3", lang))
        print("4. " + say("miaoyin_choice_4", lang))
        print("5. " + say("miaoyin_choice_5", lang))
        print("6. " + say("miaoyin_choice_6", lang))

        
        choice = input(say("input_prompt", lang))

        if choice == "1":
            print(say("miaoyin_bluff_response", lang))
            
            clues.add(say("clue_promise_of_reclusion", lang)) 

            variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            
            events_log.append(say("log_miaoyin_fake_death_claim", lang))

            variables['truth_window_miaoyin'] = True
            # Trigger truth window,will diff choice_3&5:
          

        elif choice == "2":
            print(say("miaoyin_no_rescue_response", lang))
            
            
            clues.add(say("clue_someone_else_poisoned", lang))
            variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1
            events_log.append(say("log_miaoyin_failed_rescue", lang))

        elif choice == "3":

            print(say("miaoyin_relationship_response", lang))
           
            clues.add(say("clue_former_master_disciple", lang)) 
            clues.add(say("clue_promise_of_reclusion", lang)) 

            
            events_log.append(say("log_miaoyin_relationship_history", lang))
            
            
            # easter egg, only trigger after choice 1 has been used
            if variables.get('truth_window_miaoyin', False):
                say_multiline("miaoyin_hidden_relationship_story", lang)

        elif choice == "4":
            
            say_multiline("miaoyin_observe_bottles_response", lang) 

           
            clues.add(say("clue_multiple_poisons", lang))
            
            clues.add(say("clue_poison_source_identified", lang))
            variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1
            
            events_log.append(say("log_miaoyin_observe_bottles", lang))

        elif choice == "5":
            
            say_multiline("miaoyin_secret_room_response", lang)
            
            
            clues.add(say("clue_poison_bottleX2", lang)) 
            # "毒药瓶x2" or two_poison_bottles
            events_log.append(say("log_miaoyin_gain_poison_bottle_x_2", lang))
            
            print(say("miaoyin_ask_more", lang))
            
            
            if variables.get('truth_window_miaoyin', False):
                say_multiline("miaoyin_powder_scent_reveal", lang)
                clues.add(say("clue_suspect_lanyi_access_miaoyin_medicine", lang))
                variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
                
            else:
                print(say("miaoyin_no_more_info", lang))
                variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
                variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1


        elif choice == "6":
            print(say("miaoyin_leave_dialogue", lang))
            break

        else:
            print(say("invalid_input", lang))
    



