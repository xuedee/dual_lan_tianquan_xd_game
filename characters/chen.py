import time
from dialogue_data import safe_input, say, say_multiline, split_clues
def interact_with_chen(events_log, clues, variables,lang="en"):
    """
    与陈奇曼的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 {'emotion_chen': 0, 'suspect_chen': 0}）
    :param lang: "zh" or "en" - The chosen language
    """
 
    


    print(say("chen_profile", lang))
    print(say("chen_greeting_intro1", lang))
    print(say("chen_greeting_intro2", lang))
    print(say("chen_greeting_player_reply", lang))




    while True:
        
        print(say("chat_start_prompt", lang))
        print("1. " + say("chen_choice_1", lang))
        print("2. " + say("chen_choice_2", lang))
        print("3. " + say("chen_choice_3", lang))
        print("4. " + say("chen_choice_4", lang))
        print("5. " + say("chen_choice_5", lang))
        print("6. " + say("chen_choice_6", lang))

        
        choice = input(say("input_prompt", lang))

        if choice == "1":
            
            
            say_multiline("chen_feud_resolved_dialogue", lang)
            variables['emotion_chen'] = variables.get('emotion_chen', 0) + 1
            
            events_log.append(say("log_chen_claim_resolved_feud", lang))


        elif choice == "2":
            
            print(say("chen_last_meeting_dialogue1", lang)) 
            print(say("chen_last_meeting_dialogue2", lang)) 
            
            clues.add(say("clue_no_victory_in_fight", lang)) 
           
            events_log.append(say("log_chen_last_meeting", lang))
        
        elif choice == "3":
            
            print(say("chen_hint_unforgiven_dialogue1", lang)) 
            print(say("chen_hint_unforgiven_dialogue2", lang))
            variables['suspect_chen'] = variables.get('suspect_chen', 0) + 1
            
            events_log.append(say("log_chen_probe_true_attitude", lang))
        
        
        elif choice == "4":
            
            say_multiline("chen_item_observation_dialogue", lang)
            clues.add(say("clue_chen_injured", lang))
            clues.add(say("clue_huashan_wounds_medicine", lang))
            clues.add(say("clue_chen_antidote_pill", lang))
            events_log.append(say("log_chen_check_items", lang))

           
            variables['suspect_chen'] = variables.get('suspect_chen', 0) + 1
        
        elif choice == "5":
            
            
           
            
            print(say("chen_direct_accusation_observation", lang))
            say_multiline("chen_direct_accusation_dialogue", lang)
           
            variables['emotion_chen']=variables.get('emotion_chen', 0) + 1
           
            events_log.append(say("log_chen_direct_accusation", lang))
            variables['suspect_chen'] = variables.get('suspect_chen', 0) - 1 # Reduce suspicion

        elif choice == "6":
            
            print(say("chen_leave_dialogue", lang)) 
            break

        else:
            
            print(say("invalid_input", lang))

