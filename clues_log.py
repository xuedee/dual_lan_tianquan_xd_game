from dialogue_data import safe_input, say, DIALOGUES

def view_log_and_clues(events_log, clues, variables, lang="en"):
    """
    显示玩家当前的调查日志和线索
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict，供显示关键信息（可选）
    :param lang: "zh" or "en" - The chosen language
    """

   
    print(f"\n======== {say('log_title', lang)} ========")

    if not events_log and not clues:
       
        print(say("log_no_info", lang))
        return

    if events_log:
        
        print(f"\n{say('log_progress_title', lang)}：")
        for i, event in enumerate(events_log, 1):
            print(f"  {i}. {event}")

    if clues:
        
        print(f"\n{say('log_clues_title', lang)}：")
        for i, clue in enumerate(clues, 1):
            print(f"  - {clue}")


    
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

    
    if suspects:
        # Join suspects with appropriate separator based on language
        if lang == "zh":
            print(f"  {say('log_suspect_you_suspect', lang)}：{', '.join(suspects)}")
        else: # English
            print(f"  {say('log_suspect_you_suspect', lang)}: {', '.join(suspects)}")
    else:
        print(say("log_suspect_no_target", lang))

  
    print(f"\n{say('log_emotion_title', lang)}：")


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
        print(say("log_emotion_no_records", lang)) # New message if no emotions recorded



    print("================================")
