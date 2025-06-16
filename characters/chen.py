def interact_with_chen(events_log, clues, variables):
    """
    与陈奇曼的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 {'emotion_chen': 0, 'suspect_chen': 0}）
    """
    print("\n 陈奇曼 \n 身份：华山派掌门 \n 年龄：50岁 \n 人设关键词：刚正、沉稳、外冷内柔 \n 背景信息：当年其幼子陈一峰品行不端，当街强抢民女，被天泉沈庄主误杀。\n 失子之后痛不欲生，发誓与沈庄主不共戴天。后经清音阁掌教穆长风调停， \n 二人约定二十年后在天泉山庄决一死战。二十年来掌管华山派，心境逐渐平和。\n 公开信息：此次前来是为履行当年之约，表面上仍不冷不热。")

    print("\n你来到偏厅，陈奇曼正独自喝茶。你听闻他是当年陈一峰之父，与沈庄主积怨已久。")
    print("他抬眼望你：“如此年轻，竟是清音阁特使执事？真是江山代有才人出，后生可畏啊。”")
    print("\n你盯着他，道“陈掌门过奖了。”")

    while True:
        print("\n你想向陈奇曼询问什么？")
        print("1. 问他是否真的已放下仇恨")
        print("2. 询问他与沈庄主最后见面情况")
        print("3. 暗示他其实并未原谅沈庄主")
        print("4. 留意他手边茶壶与药瓶是否有异常")
        print("5. 直接质问是否下了毒手")
        print("6. 离开陈奇曼")

        choice = input("请选择（输入数字）：")

        if choice == "1":
            print("\n陈奇曼沉默良久：“二十年了，我虽然难过，但过往种种，我儿也算是自食其果，天泉沈庄主又何尝不自责？”")
            print("“我是来了结仇怨，不是来索命。”")
            variables['emotion_chen'] = variables.get('emotion_chen', 0) + 1
            events_log.append("陈奇曼声称放下仇恨")

        elif choice == "2":
            print("\n“我们没有再动手。”他皱眉：“只是比了一招掌力，然后喝了几盏酒，言尽于此。”")
            print("你感受到一种压抑的克制。")
            clues.add("比掌未决胜负")
            events_log.append("了解陈奇曼与沈庄主对话内容")
        
        elif choice == "3":
            print("\n陈奇曼冷笑一声：“你是说我演戏？”")
            print("“我若要杀人，岂会藏头露尾？”")
            variables['suspect_chen'] = variables.get('suspect_chen', 0) + 1
            events_log.append("试探陈奇曼真实态度")
        
        elif choice == "4":
         
            chat_text = [
                "你瞥见他的茶壶略有异味，但无毒粉痕迹，并且在他袖口隐约看到两个不同颜色的小瓶贴着封条‘华山派特制’。",
                "你冲他礼貌点头：“陈掌门袖内可是华山派的宝贝？不知再下可否一观？”",
                "陈奇曼愣了一下，随后笑道，：“特使眼神真是锋利，这是我华山派独门金疮药。”",
                "你拿到两瓶药物，打开闻了闻：“确实是金疮药，那这另外一瓶，像是常见的解毒丸？”",
                "陈奇曼点点头，：“不错，出门在外，防身之物罢了。”",
                "你有些怀疑陈奇曼，但他身上没有发现任何毒药。",
                "你：“多谢陈掌门，在下告辞了。”"
                ]
            
            import time
            for line in chat_text:
                print(line)
                time.sleep(1.5)  # 每句间隔1.5秒
            
            




            clues.add("华山派金疮药")
            clues.add("陈奇曼解毒丸")
            events_log.append("检查陈奇曼物品")
            variables['suspect_chen'] = variables.get('suspect_chen', 0) + 1
        
        elif choice == "5":
            
            
            
            chat_text = [
                "他隐隐有些怒意：“我纵有恨意，也是二十年前...”",
                "“此次是来解怨，并非寻仇，不然我为何还邀请静慧师太前来见证...",
                "他昂起下巴“况且我陈奇曼从不屑暗箭伤人！”",
                "你观察他的神情，觉得他说的可能是真话。"
                ]
            print("他的反应真切，似乎并无杀机。")
            import time
            for line in chat_text:
                print(line)
                time.sleep(1.5)  # 每句间隔1.5秒
            
            
            variables['emotion_chen'] += 1
            events_log.append("质问陈奇曼是否下毒手")
            variables['suspect_chen'] = variables.get('suspect_chen', 0) - 1

        elif choice == "6":
            print("\n陈奇曼不再说话，低头饮茶。你起身离去，只觉此人深不可测。")
            break

        else:
            print("无效输入，请重新输入。")

