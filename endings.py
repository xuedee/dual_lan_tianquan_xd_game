import time
from dialogue_data import say, DIALOGUES
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

    #print("\n=== 结局揭晓 ===")
    print(f"\n=== {say('ending_title', lang)} ===")

    # --- 阶段 1: 关键物证门槛检查 ---
    # 确保这两件核心物证的键名与 dialogue_data.py 中定义的一致
    bottle1_found = say("clue_poison_bottle_1", lang) in clues
    bottle2_found = say("clue_poison_bottleX2", lang) in clues # 注意：此键名现在对应 '获得毒药瓶x2' / 'Gained Two Poison Bottles'

    if not (bottle1_found and bottle2_found):
        # 结局 1: 证据不足，凶手逍遥法外
        print(say("ending_failure_insufficient_evidence_msg", lang))
        ending_key = "ending_failure_insufficient_evidence_name"
        
        print(say("ending_prompt_fail_options", lang))
        final_input = input("") # 等待用户输入

        if final_input == '*':
            print(say("ending_hint_fail", lang))
        
        print("====================")
        return ending_key # 游戏在此处直接返回，结束判断

    # --- 阶段 2: 准备结局判断所需的关键变量 ---
    # 确认林修的完整供述是否已触发
    lin_confessed_in_dialogue = variables.get('lin_confessed_poison_triggered', False)

    # 确认林修的线索是否已收集 (注意：'clue_unusual_poison_signs' 已确认删除)
    lin_access_miaoyin_medicine_clue_found = say("clue_lin_access_miaoyin_medicine", lang) in clues
    
    # 玩家是否“客观上”发现了林修是凶手（即：林修接触药物线索已收集 且 他的完整供述已触发）
    player_objectively_found_lin_guilty = (
        lin_access_miaoyin_medicine_clue_found and
        lin_confessed_in_dialogue
    )

    # 林修与沈澜衣的感情及玩家对他们的情感倾向
    love_points_lin_lanyi = variables.get('love_points', 0)
    emotion_lin = variables.get('emotion_lin', 0)
    emotion_lanyi = variables.get('emotion_lanyi', 0)

    # --- 阶段 3: 根据玩家的最终指认来判断结局 ---
    ending_key = "ending_unresolved_name" # 默认结局，如果所有条件都不满足

    # 情况 A: 玩家指认林修
    if accused_char_key == 'lin':
        # 子分支 1: 沈澜衣为爱顶罪（高优先级触发，只有在指认林修时才可能发生）
        if love_points_lin_lanyi >= 4:
            print(say("ending_lanyi_jumps_in_for_lin", lang))
            if emotion_lin > emotion_lanyi:
                # 结局 3: 恋爱脑断案，误判忠贞
                print(say("ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_msg", lang))
                ending_key = "ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_name"
                print(say("ending_tip_love_brain_damage", lang))
            else: # emotion_lanyi >= emotion_lin
                # 结局 4: 青天大判官，公正无私
                print(say("ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_msg", lang))
                ending_key = "ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_name"
                print(say("ending_jinghui_takes_lanyi_away", lang))
        # 子分支 2: 玩家直接指认林修 (沈澜衣未顶罪)
        elif player_objectively_found_lin_guilty:
            # 结局 2: 真相大白，悲剧收场 (完美结局)
            print(say("ending_true_killer_found_line", lang)) # 注意：这里使用合并后的单行字符串
            ending_key = "ending_true_killer_name"
            print(say("ending_success_appraisal_msg", lang))
        else:
            # 结局 5: 迷迷糊糊断案王 (指认对但证据不全)
            print(say("ending_muddled_judgment_message", lang))
            ending_key = "ending_muddled_judgment_name"

    # 情况 B: 玩家指认林修之外的任何角色
    elif accused_char_key in ['lanyi', 'chen', 'jing', 'miaoyin', 'butler']:
        if player_objectively_found_lin_guilty:
            # 结局 6: 指鹿为马，颠倒黑白 (知道真凶却故意指认他人)
            print(say("ending_false_accusation_knew_truth_msg", lang))
            ending_key = "ending_false_accusation_knew_truth_name"
        else:
            # 玩家未客观发现林修有罪，且指认了无辜者（具体文本根据角色细分）
            if accused_char_key == 'lanyi':
                # 结局 7a: 错判红颜，无辜受累
                print(say("ending_false_accusation_lanyi_msg", lang))
                ending_key = "ending_false_accusation_lanyi_name"
            elif accused_char_key == 'chen':
                # 结局 7b: 错指掌门，威信受损
                print(say("ending_false_accusation_chen_msg", lang))
                ending_key = "ending_false_accusation_chen_name"
            elif accused_char_key == 'jing':
                # 结局 7c: 诬陷高僧，业障加身
                print(say("ending_false_accusation_jing_msg", lang))
                ending_key = "ending_false_accusation_jing_name"
            elif accused_char_key == 'miaoyin':
                # 结局 7d: 误会重重，仙子蒙冤 (妙音的冤枉结局，使用合并后的单行字符串)
                print(say("ending_suspect_miaoyin_line", lang))
                ending_key = "ending_suspect_miaoyin_name"
            elif accused_char_key == 'butler':
                # 结局 7e: 忠诚之谜，未解之谜 (老管家的冤枉结局，使用合并后的单行字符串)
                print(say("ending_suspect_butler_line", lang)) # 注意：这里使用合并后的单行字符串
                ending_key = "ending_suspect_butler_name"

    # 情况 C: 玩家未指认任何特定凶手，或指认无效
    else: # accused_char_key 为 None (取消指认) 或其他非预期的值
        # 结局 8: 无果遗憾 (兜底结局)
        print(say("ending_unresolved_line", lang)) # 注意：这里使用合并后的单行字符串
        ending_key = "ending_unresolved_name"

    print("====================")
    return ending_key # 返回最终的结局键名