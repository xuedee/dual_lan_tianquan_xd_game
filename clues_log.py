from dialogue_data import say, DIALOGUES

def view_log_and_clues(events_log, clues, variables, lang="en"):
    """
    显示玩家当前的调查日志和线索
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict，供显示关键信息（可选）
    :param lang: "zh" or "en" - The chosen language
    """

    #print("\n=== 调查日志 ===")
    print(f"\n======== {say('log_title', lang)} ========")

    if not events_log and not clues:
        #print("你还没有收集到任何线索或调查记录。")
        print(say("log_no_info", lang))
        return

    if events_log:
        #print("\n调查进展记录：")
        print(f"\n{say('log_progress_title', lang)}：")
        for i, event in enumerate(events_log, 1):
            print(f"  {i}. {event}")

    if clues:
        #print("\n已收集线索：")
        print(f"\n{say('log_clues_title', lang)}：")
        for i, clue in enumerate(clues, 1):
            print(f"  - {clue}")


    # 根据变量状态展示简要推测
    #print("\n当前推测状态：")
    print(f"\n{say('log_suspicion_status_title', lang)}")
    suspects = []

    # Mapping variable keys to display names using DIALOGUES
    
    suspect_map = {
        'suspect_butler': say("character_butler", lang),
        'suspect_miaoyin': say("character_miaoyin", lang),
        'suspect_lin': say("character_lin", lang),
        'suspect_chen': say("character_chen", lang),
        'suspect_lanyi': say("character_lanyi", lang),
        'suspect_jing': say("character_jing", lang) 
    }

    for key, display_name in suspect_map.items():
        if variables.get(key, 0) > 0:
            suspects.append(display_name)



    #if variables.get('suspect_butler', 0) > 0:
    #    suspects.append("老管家")
    #if variables.get('suspect_miaoyin', 0) > 0:
    #    suspects.append("妙音仙子")
    #if variables.get('suspect_lin', 0) > 0:
    #    suspects.append("林修")
    #if variables.get('suspect_chen', 0) > 0:
    #    suspects.append("陈奇曼")
    #if variables.get('suspect_lanyi', 0) > 0:
    #    suspects.append("沈澜衣")
    

    #if suspects:
    #    print(f"  你怀疑：{', '.join(suspects)}")
    #else:
    #    print("  你暂时没有明确怀疑的对象。")
    
    if suspects:
        # Join suspects with appropriate separator based on language
        if lang == "zh":
            print(f"  {say('log_suspect_you_suspect', lang)}：{', '.join(suspects)}")
        else: # English
            print(f"  {say('log_suspect_you_suspect', lang)}: {', '.join(suspects)}")
    else:
        print(say("log_suspect_no_target", lang))

    # 展示玩家对关键角色的情感值    
    #print("\n角色情感倾向：")
    print(f"\n{say('log_emotion_title', lang)}：")

    #for key in ['emotion_butler', 'emotion_miaoyin','emotion_lin','emotion_jing', 'emotion_lanyi', 'emotion_chen']:
    #    val = variables.get(key, 0)
    #    if val != 0:
    #        print(f"  对 {key.replace('emotion_', '')} 的情感值：{val}")
    # Mapping emotion keys to character names for display
    
    emotion_map = {
        'emotion_butler': say("character_butler", lang),
        'emotion_miaoyin': say("character_miaoyin", lang),
        'emotion_lin': say("character_lin", lang),
        'emotion_jing': say("character_jing", lang),
        'emotion_lanyi': say("character_lanyi", lang),
        'emotion_chen': say("character_chen", lang)
    }

    found_emotions = False
    for key, display_name in emotion_map.items():
        val = variables.get(key, 0)
        if val != 0:
            print(f"  {say('log_emotion_for', lang)} {display_name}：{val}")
            found_emotions = True
    
    if not found_emotions:
        print(say("log_emotion_no_records", lang)) # Default message if no emotions recorded
    
    ###===display the love_points for player
    #num_lov=variables.get('love_points',0)
    #if lang =="zh":
    #    print(f"\n当前恋爱脑指数：{num_lov}")
    #else:
    #    print(f"\nCurrent Love-Brain Interference Level: {num_lov}")

    # 将“当前恋爱脑指数”也放入 dialogue_data.py
    shen_lov=variables.get('shen_love_points',0)
    lin_lov=variables.get('lin_love_points',0)
    # 调用 dialogue_data.py 中新定义的恋爱脑key
    print(f"\n{say('lanyi_love_brain_level', lang)} {shen_lov}")
    print(f"{say('lin_love_brain_level', lang)} {lin_lov}")



    print("================================")
