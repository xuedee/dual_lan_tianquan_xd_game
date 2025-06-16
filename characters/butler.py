def interact_with_butler(events_log, clues, variables):
    """
    与老管家的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 {'emotion_butler': 0, 'suspect_butler': 0,'truth_window_butler': False}）
    """
    print("老管家 \n 身份：天泉山庄元老 \n 年龄：62岁 \n 人设关键词：忠仆、念旧、沉默寡言 \n 背景信息：一手将沈庄主带大，亦见证山庄盛衰。前不久与庄主发生口角冲突，俩人不欢而散，\n 后来传出庄主强制让管家“退休”，管家本人据说当时显得十分愤怒。\n 公开信息：说话带刺，爱抱怨庄主无情")

    print("\n你来到偏院，老管家正在为主厅整理供桌，动作迟缓，神色黯然。")
    print("他听见脚步声抬头，看了你一眼，叹了口气：“尊驾是清音阁来的？你们阁主真是消息灵通，这么快就派人来了，请问吧，我定然知无不言，言无不尽。”")

    while True:
        print("\n你想向老管家询问什么？")
        print("1. 问他为何被庄主开除")
        print("2. 问他对庄主的忠诚是否动摇")
        print("3. 询问庄主生前是否有异样")
        print("4. 观察供桌与供果")
        print("5. 暗示他可能对庄主下手")
        print("6. 离开老管家")

        choice = input("请选择（输入数字）：")

        if choice == "1":
            chat_text = [
                "“哎，其实我本来也不理解...还很生气，但...”",
                "“庄主后来跟我私下道了个歉。”他眼眶泛红...",
                "“他只说怕仇家寻仇，劝我尽快离开天泉山庄。”",
                "“他还给了我一笔养老银子，我并不怨他。”"
                ]
            
            import time
            for line in chat_text:
                print(line)
                time.sleep(1.5)  # 每句间隔1.5秒
            
            
            clues.add("管家获得银票补偿")
            events_log.append("询问管家被开除原因")
            variables['emotion_butler'] = variables.get('emotion_butler', 0) + 1

        elif choice == "2":
            print("\n“我跟了庄主四十年，他连生病都不会瞒着我的。”")
            print("“我怎么会害他，我只是不放心他罢了。”")
            events_log.append("探问管家忠诚")
            variables['emotion_butler'] = variables.get('emotion_butler', 0) + 1
            variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1
            # 触发choice == "4"隐藏剧情
            variables['truth_window_butler'] = True

        elif choice == "3":
            print("\n他思索道：“哎，最近庄主让妙音仙子整顿药房，还吩咐将库房钥匙交给沈小姐。”")
            print("“还亲自拟了份遗书，只不过那遗书又被他自己烧了。”")
            clues.add("遗书已被焚毁")
            events_log.append("获取遗书情报")
        
        elif choice == "4":
            print("\n你留意到屋内有一供桌，上面供奉着天泉山庄庄主沈天正的灵位，还摆着一些瓜果。")
            print("\n你对着灵位上了根香，发现供桌下面有一个很精致的小红瓶。")
            
                
            # 隐藏剧情（只在使用过“choice 2”后触发）
            if variables['truth_window_butler'] == True:
                chat_text = [
                    "你伸手把瓶子捡了起来“你这瓶子倒是十分精致。”",
                    "管家显得神色有些慌张",
                    "“这瓶子是我在房门外捡的。”",
                    "你目光灼灼盯着管家观察",
                    "“其实后来我发现，这瓶子是妙音仙子用来装毒药的”他眼眶泛红...",
                    "“妙音仙子或许就是杀害庄主的真凶，还请清音阁为我们天泉山庄做主。”见老管家要给你跪下，你一把扶起他",
                    "你面色不悦：“既然如此，你刚才为何不说。”",
                    "老管家神情不安道：“妙音仙子善毒，我怕她杀我灭口。”",
                    "老管家神色逐渐变得有些惭愧：“我见你如此年轻，也不知能力几何，故意将瓶子留在地上，也想试探你一二。”",
                    "“原来如此。”你点点头，拿走了瓶子。"
                    ]
                import time
                for line in chat_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒
                #毒药瓶子必须收集全才可获得正确结局
                clues.add("毒药瓶1")
                events_log.append("获得毒药瓶1")
                variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            else:
                print("\n你上完了香。")
                clues.add("供桌灵位")
                events_log.append("观察供桌表面")
                variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1

        elif choice == "5":
            print("\n老管家苦笑：“你看我这把年纪，还能毒杀主子？清音阁真是多疑。”")
            variables['suspect_butler'] = variables.get('suspect_butler', 0) + 1
            events_log.append("质疑管家动机")

        elif choice == "6":
            print("\n你道声告辞，老管家默默点头，继续为供桌摆放花果。")
            break

        else:
            print("无效输入，请重新选择。")
