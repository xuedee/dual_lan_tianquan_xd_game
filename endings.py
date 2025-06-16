def make_final_judgment(clues, variables, events_log):
    """
    根据玩家线索和怀疑变量判断游戏结局
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如怀疑度）
    :return: 结局字符串
    """

    print("\n=== 结局揭晓 ===")

    # 先判断真凶线索是否完整
    true_killer = False
    if ("林修接触妙音仙子药物" in clues and
        "中毒迹象异常" in clues and
        variables.get('suspect_lin_xiu', 0) > 0):
        true_killer = True

    # 判断对妙音仙子怀疑过重
    suspect_miaoyin = variables.get('suspect_miaoyin', 0) > 1
    suspect_butler = variables.get('suspect_butler', 0) > 1

    # 根据线索和怀疑变量判定结局
    if true_killer:
        print("你成功找出了真凶：林修。")
        print("他并非蓄意杀人，而是误用毒药混合，导致庄主身亡。")
        print("一场误会掀起了江湖悲剧，恩怨终成遗恨。")
        ending = "真相大白，悲剧收场"

    elif suspect_miaoyin and not true_killer:
        print("你怀疑妙音仙子是凶手。")
        print("她虽然深爱庄主，但毒药在她手中变成了杀人的利器。")
        print("但你没有确凿证据证明她故意杀人，只能作为怀疑者离开。")
        ending = "误会重重，仙子蒙冤"

    elif suspect_butler and not true_killer:
        print("你怀疑老管家行凶。")
        print("但他的行为更像是忠诚与无奈，缺少杀意。")
        print("你留下疑问，江湖恩怨未了。")
        ending = "忠诚之谜，未解之谜"

    else:
        print("你未能准确找到真凶。")
        print("沈庄主的死因成了无人能解的江湖秘事。")
        print("你只能带着遗憾离开。")
        ending = "无果遗憾"

    print("====================")
    return ending
