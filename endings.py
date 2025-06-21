import time
from dialogue_data import safe_input, say, DIALOGUES
def make_final_judgment(clues, variables, events_log,lang="en", accused_char_key=None):
    """
    根据玩家线索和怀疑变量判断游戏结局
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（存储游戏状态和角色属性的字典:情感值、怀疑度、真相窗口）
    :param events_log: 玩家行为日志 (optional, for debugging or complex endings)
    :param lang: "zh" or "en" - The chosen language
    :accused_char_key (str, optional): 玩家最终指认的凶手键名 ('lin', 'lanyi' 等)。如果玩家临时选择取消指认，则为 None。
    :return: str-触发的结局名称的键名 (例如 'ending_true_killer_name')。
    """

   
    print(f"\n=== {say('ending_title', lang)} ===")

    # --- pre con: 3 bottles all gain ---
     
    bottle1_found = say("clue_poison_bottle_1", lang) in clues
    bottle2_found = say("clue_poison_bottleX2", lang) in clues

    if not (bottle1_found and bottle2_found):
        # Ending_1: Failed to find all evidence
        print(say("ending_failure_insufficient_evidence_msg", lang))
        ending_key = "ending_failure_insufficient_evidence_name"
        
        print(say("ending_prompt_fail_options", lang))
        final_input = input("") # waiting for the input

        if final_input == '*':
            print(say("ending_hint_fail", lang))
        
        print("====================")
        return ending_key 

    # --- stage 2: check if SUCCESSFUL full condition meet ---
    
    #confirm if lin's truth tell dialogue been triggered
    lin_confessed_in_dialogue = variables.get('lin_confessed_poison_triggered', False)

    # confirm lin took miaoyin's poison
    lin_access_miaoyin_medicine_clue_found = say("clue_lin_access_miaoyin_medicine", lang) in clues
    
    
    # player should know LIN is the killer
    player_objectively_found_lin_guilty = (
        lin_access_miaoyin_medicine_clue_found and
        lin_confessed_in_dialogue
    )

    # love_points between lin_lanyi, player's emotion to lin(should be low to get SUCCESS), player's emotion to lanyi
    love_points_lin_lanyi = variables.get('love_points', 0)
    emotion_lin = variables.get('emotion_lin', 0)
    emotion_lanyi = variables.get('emotion_lanyi', 0)

    # --- stage 3: ENDING(s) ---
    ending_key = "ending_unresolved_name" # default ending, noting being found

   
    #Case A: Player accuses Lin Xiu
    if accused_char_key == 'lin':
        
        # Sub-branch 1: Shen Lanyi takes the blame for love (only possible if Lin is accused)
        if love_points_lin_lanyi >= 4:
            print(say("ending_lanyi_jumps_in_for_lin", lang))
            if emotion_lin > emotion_lanyi:
        
                # Ending 3: Blinded by love — misjudging the loyal
                print(say("ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_msg", lang))
                ending_key = "ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_name"
                print(say("ending_tip_love_brain_damage", lang))
            else: # emotion_lanyi >= emotion_lin
                
                # Ending 4: Just judgment — fairness above all
                print(say("ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_msg", lang))
                ending_key = "ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_name"
                print(say("ending_jinghui_takes_lanyi_away", lang))
        
        # Sub-branch 2: Player directly accuses Lin Xiu (Lanyi does not take the blame)
        elif player_objectively_found_lin_guilty:
            
            # Ending 2: Truth revealed — tragedy resolved (ideal ending)
            print(say("ending_true_killer_found_line", lang))
            ending_key = "ending_true_killer_name"
            print(say("ending_success_appraisal_msg", lang))
        else:
            
            # Ending 5: Lucky guess — partial truth with insufficient evidence
            print(say("ending_muddled_judgment_message", lang))
            ending_key = "ending_muddled_judgment_name"

    # Case B: Player accuses someone other than Lin Xiu
    elif accused_char_key in ['lanyi', 'chen', 'jing', 'miaoyin', 'butler']:
        if player_objectively_found_lin_guilty:
            # Ending 6: Willful false accusation despite knowing the truth
            print(say("ending_false_accusation_knew_truth_msg", lang))
            ending_key = "ending_false_accusation_knew_truth_name"
        else:
            # Player failed to find the real killer and wrongly accused someone else
            if accused_char_key == 'lanyi':
                # Ending 7a: Wrongly accused Lanyi — the innocent suffer
                print(say("ending_false_accusation_lanyi_msg", lang))
                ending_key = "ending_false_accusation_lanyi_name"
            elif accused_char_key == 'chen':
                # Ending 7b: Wrongly accused the sect leader — authority undermined
                print(say("ending_false_accusation_chen_msg", lang))
                ending_key = "ending_false_accusation_chen_name"
            elif accused_char_key == 'jing':
                # Ending 7c: Slandered a high monk — karmic burden
                print(say("ending_false_accusation_jing_msg", lang))
                ending_key = "ending_false_accusation_jing_name"
            elif accused_char_key == 'miaoyin':
                # Ending 7d: False suspicion — the Fairy MiaoYin wronged
                print(say("ending_suspect_miaoyin_line", lang))
                ending_key = "ending_suspect_miaoyin_name"
            elif accused_char_key == 'butler':
                #  Ending 7e: Loyal heart mistaken — the truth remains hidden
                print(say("ending_suspect_butler_line", lang))
                ending_key = "ending_suspect_butler_name"

    # Case C: Player made no valid accusation
    else: 
        # accused_char_key is None (no accusation, player quit without accusation anyone) or unexpected
        # Ending 8: No resolution — a lingering regret
        print(say("ending_unresolved_line", lang)) 
        ending_key = "ending_unresolved_name"

    print("====================")
    return ending_key
    # Return final ending key
