import time # Ensure time imported if you use time.sleep
from dialogue_data import safe_input, say, say_multiline,split_clues
def interact_with_lin(events_log, clues, variables, lang="en"):
    """
    与林修的多选互动模块
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合
    :param variables: 状态变量 dict，如 {'emotion_lin': 0, 'suspect_lin': 0 'truth_window_lin', 'love_points': 0}
    """
   
    
    print(say("lin_intro", lang))
    print()#start new line
    print(say("lin_greeting", lang))

    while True:
        
        
        print(say("chat_start_prompt", lang))
        print("1. " + say("lin_choice_1", lang))
        print("2. " + say("lin_choice_2", lang))
        print("3. " + say("lin_choice_3", lang))
        print("4. " + say("lin_choice_4", lang))
        print("5. " + say("lin_choice_5", lang))

        choice = input(say("input_prompt", lang))
        #ask the user to enter their choice 1-5

        
        if choice == "1":
            
            #Print the full dialogue containing the clue
            print(say("lin_obs_result",lang))
            #clues.add("少许香灰")
            #clues.add(say("lin_obs_result", lang).split('：')[-1].strip())
            #re.split('[:：]', clues.add(say("lin_obs_result", lang))[-1].strip())
            # Use the new function to extract the clue
            extracted_clue = split_clues("lin_obs_result", lang)
            if extracted_clue: # Only add if a clue was successfully extracted
                clues.add(extracted_clue)
            
            events_log.append(say("log_obs_lin_room", lang)) # Corrected log key

        elif choice == "2":
            
            print(say("lin_reason_stay",lang))
            
            variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            variables['love_points'] = variables.get('love_points', 0) + 1
            
            events_log.append(say("log_reason_lin_stay", lang)) 
            # add log key for "log_reason_lin_stay"
        
        elif choice == "3":
            if not variables.get('truth_window_lin', False):
            #when "truth_window_lin" is false, or window doesn't exist, process logic below
                say_multiline("lin_memory_early", lang)
                variables['love_points'] = variables.get('love_points', 0) + 1
                variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            else:
                # only apply when "truth_window_lin" is opened(True)
                # also check if clue "少许香灰" or "Traces of incense ash" already collected.
                incense_clue_found = False
                for clue in clues:
                    if "香灰" in clue or "incense ash" in clue.lower():
                        incense_clue_found = True
                        break

                if variables.get('emotion_lin', 0) >= 5 and variables.get('love_points', 0) >= 4 and incense_clue_found:
                    # only if emotion_lin & love_points meet the requirements, tell truth
                    say_multiline("lin_confess_poison", lang)
                    variables['lin_confessed_poison_triggered'] = True #*****tell truth here！！！*****
                    clues.add(say("clue_lin_access_miaoyin_medicine", lang))
                    clues.add(say("clue_lin_full_confession_seen", lang))
                else:
                    #standard reply when "truth_window_lin" is opened(True)
                    say_multiline("lin_deny_poison", lang)
            

            
            variables['suspect_lin'] = variables.get('suspect_lin', 0) + 1
            
            events_log.append(say("log_lin_backstory", lang))
        
        elif choice == "4":
            
            print(say("lin_love_response",lang))
            variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            
            events_log.append(say("log_talk_lin_love", lang))
            #trigger for the truth window
            variables['truth_window_lin'] = True
        
        elif choice == "5":
            
            print(say("lin_leave",lang))
            break

        else:
            
            print(say("invalid_input",lang))
            
