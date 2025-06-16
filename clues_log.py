def view_log_and_clues(events_log, clues, variables):
    """
    显示玩家当前的调查日志和线索
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict，供显示关键信息（可选）
    """

    print("\n=== 调查日志 ===")

    if not events_log and not clues:
        print("你还没有收集到任何线索或调查记录。")
        return

    if events_log:
        print("\n调查进展记录：")
        for i, event in enumerate(events_log, 1):
            print(f"  {i}. {event}")

    if clues:
        print("\n已收集线索：")
        for i, clue in enumerate(clues, 1):
            print(f"  - {clue}")


    # 根据变量状态展示简要推测（可选）
    print("\n当前推测状态：")
    suspects = []
    if variables.get('suspect_butler', 0) > 0:
        suspects.append("老管家")
    if variables.get('suspect_miaoyin', 0) > 0:
        suspects.append("妙音仙子")
    if variables.get('suspect_lin', 0) > 0:
        suspects.append("林修")
    if variables.get('suspect_chen', 0) > 0:
        suspects.append("陈奇曼")
    if variables.get('suspect_lanyi', 0) > 0:
        suspects.append("沈澜衣")
    

    if suspects:
        print(f"  你怀疑：{', '.join(suspects)}")
    else:
        print("  你暂时没有明确怀疑的对象。")

    # 展示玩家对关键角色的情感值（可选辅助）    
    print("\n角色情感倾向：")
    for key in ['emotion_butler', 'emotion_miaoyin','emotion_lin','emotion_jing', 'emotion_lanyi', 'emotion_chen']:
        val = variables.get(key, 0)
        if val != 0:
            print(f"  对 {key.replace('emotion_', '')} 的情感值：{val}")


    
    
    
    
    
    print("================")





"""
触发隐藏回忆剧情，逐行显示文字，加入新线索与情绪变化。

:param speaker_name: 对话人姓名
:param memory_lines: 要显示的回忆文字列表
:param clues_set: 记录线索的集合
:param events_log: 行为日志
:param clue_to_add: 触发后加入的线索
:param event_to_log: 触发后加入的行为日志
:param emotion_variable: 如需修改情绪值，对应变量名
:param emotion_change: 情绪变化值（正负）
:param variables: 可选的变量字典（如果有情绪变量）
"""
def trigger_hidden_memory(
    speaker_name,
    memory_lines,
    clues_set,
    events_log,
    clue_to_add,
    event_to_log,
    emotion_variable=None,
    emotion_change=0,
    variables=None
    ):
    if clue_to_add in clues_set:
        return  # 避免重复触发

    print(f"\n你注意到，{speaker_name}神情一黯，缓缓讲述起过往……")
    for line in memory_lines:
        print(f"{speaker_name}：{line}")

    clues_set.add(clue_to_add)
    events_log.append(event_to_log)

    if emotion_variable and variables is not None:
        variables[emotion_variable] = variables.get(emotion_variable, 0) + emotion_change

