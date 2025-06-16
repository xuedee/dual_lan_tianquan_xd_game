# dialogue_data.py
# 这个文件负责存储沈澜衣的对话内容，支持中英双语

dialogue_lanyi = {
    "intro": {
        "zh": "你来到湖心亭，沈澜衣倚栏独立……她神色凄苦，一转身望见你，向你微微行礼：“阁下便是清音阁特使？有劳了。”",
        "en": "You arrive at the lakeside pavilion. Shen Lanyi leans on the railing... She turns and nods to you: 'You must be the envoy from Qingyin Pavilion. Thank you for coming.'"
    },
    "ask_father": {
        "zh": "她点点头：“父亲曾亲口对我说，他不愿再纠缠于江湖旧怨，想借妙音姑姑之手脱身。”",
        "en": "She nods, 'Father told me that—he no longer wished to be tangled in old grudges, and planned to fake his death with Aunt Miaoyin’s help.'"
    },
    "ask_love": {
        "zh": "她低声道：“我一直担心林修可能不会真的原谅父亲……但我还是希望，一切能有一个善终。”",
        "en": "She murmurs, 'I’ve always worried Lin Xiu might never truly forgive Father... But I still hope things can end peacefully.'"
    },
    "ask_poison": {
        "zh": "她愣了一下，随即避开你的目光：“若说用毒，那特使应该去问妙音姑姑，毕竟她们五毒教才是用毒高手。”",
        "en": "She pauses, then avoids your gaze. 'If you want to ask about poison, you should talk to Aunt Miaoyin. The Five Venoms Sect are the true experts in poison.'"
    },
    "comfort": {
        "zh": "你安慰了她，她朝你苦笑：“多谢。父亲突然去世，庄内事务皆是我在安排，招待不周请您鉴谅。”",
        "en": "You offer her some comfort. She forces a bitter smile. 'Thank you. With Father gone, I’ve been managing everything alone... Forgive me if I’ve been a poor host.'"
    },
    "leave": {
        "zh": "你点头离去，沈澜衣背影伶仃，如湖心孤影。",
        "en": "You nod and take your leave. Shen Lanyi’s lonely silhouette remains by the lake, like an isolated shadow." 
    },
    # 可继续添加其他对话条目...
}

# 工具函数

def say(key, lang):
    """
    打印对应语言的对话内容
    :param key: 对话关键词
    :param lang: 'zh' 或 'en'
    """
    if key in dialogue_lanyi and lang in dialogue_lanyi[key]:
        print("\n" + dialogue_lanyi[key][lang])
    else:
        print("[对话缺失 / Missing dialogue]")
