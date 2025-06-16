def interact_with_miaoyin(events_log, clues, variables):
    """
    与妙音仙子的互动分支
    :param events_log: 玩家行为日志（list）
    :param clues: 玩家获得的线索集合（set）
    :param variables: 状态变量 dict（如 'emotion_miaoyin', 'suspect_miaoyin','truth_window_miaoyin'）
    """
    print("妙音仙子\n 身份：用毒高手，庄主旧识\n 年龄：38岁\n 人设关键词：冷艳、深情、危险\n 背景信息：原为沈庄主徒弟，后不明原因叛出师门改投五毒教，\n 如今为五毒教高阶长老。近年来与沈庄主关系匪浅，可谓红颜知己。\n 特长：擅制毒解毒；精音律善古琴。")

    print("\n你在后山石亭找到妙音仙子，她独自坐着，手里把玩着两枚药瓶。")
    print("“你来了。”她轻轻一笑，“想问我为何没能把他救回来吧？”")

    while True:
        print("\n你想向妙音仙子询问什么？")
        print("1. 诈一下她，问她为何要给庄主下毒")
        print("2. 询问她作为用毒高手，发现意外后，有否立刻施救沈庄主")
        print("3. 打探她与庄主的关系")
        print("4. 观察她屋内的毒药/药瓶")
        print("5. 试探她是否知道有其他人可以打开庄主密室")
        print("6. 离开妙音仙子")

        choice = input("请选择（输入数字）：")

        if choice == "1":
            print("\n“我没下毒。”她冷笑，“那是他求我的。他说只要假死，就能逃脱那场宿命的比武。”")
            print("“我给他的，只是让心跳假停三日的‘三叶息’，三日之后服下解药即可清醒。”")
            clues.add("归隐约定")
            variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            events_log.append("假死之说")
            variables['truth_window_miaoyin'] = True
            # 触发真话窗口，对选项3&5产生作用
          

        elif choice == "2":
            print("\n“他服下的是我给他的假死药，我本想守着待他三日后醒来。”她低头苦笑，“可当我推门进屋……发现他身中剧毒。”")
            print("“有人趁我不在，投了别的毒。”")
            clues.add("有人投毒")
            variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1
            events_log.append("妙音仙子未能解毒")

        elif choice == "3":
            print("\n她神情复杂：“当年我与他是师徒，我爱慕他，他却严词拒绝。”")
            print("“我一气之下叛出师门，拜了五毒教，后来经过一些事情，我们又遇见了。”")
            print("“他说，这次假死之后，愿与我归隐。”")
            clues.add("曾为师徒")
            clues.add("承诺隐居")
            events_log.append("了解妙音仙子关系史")
            
            # 触发隐藏剧情（只在使用过“choice 1.诈一下她”后触发）
            if variables['truth_window_miaoyin'] == True:
                memory_text = [
                "“你知道，当年他怎么说的吗？”",
                "“他说——师徒有别，不容越矩。他还闭关三月，罚我抄写清心咒一百遍。”",
                "“我一气之下，趁他闭关，留下书信偷跑去了南疆，拜入五毒教。”",
                "“多年后，我被崆峒派小人暗算，中毒濒死，是他救了我。”",
                "“他已不识得我的模样，以为只是救了个陌生人。”",
                "“我唤了他一声‘师父’，他才认出我。”",
                "“后来他承诺：‘若有一日，了结了这些江湖恩怨，那我便归你了。’”",
                "“这次假死，便是他兑现承诺的方式。”",
                "“可惜……他真的死了。”"
                ]
            
                import time
                for line in memory_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒

        elif choice == "4":
            print("\n妙音仙子主动拿出一个盒子，里面足有七八枚药瓶，分为红绿两种标签，大约是五毒教所传。")
            print("\n她向你介绍：“我五毒教的药瓶都有特殊印记，事后我才查到，我的毒药丢了3瓶。”")
            print("\n你询问她：“沈庄主难道是被你丢失的毒药所害？”")
            print("\n妙音仙子神情落寞：“不错。”")
            print("\n你一边观察她的神色，一边问她：“五毒教皆为用毒高手，自然配有解药，仙子竟然没能及时施救?”")
            print("\n妙音仙子眼中含泪：“是我学艺不经，没能断出那第三种毒的成分。”")
            print("\n你十分惊讶：“除了假死药，沈庄主竟然中了三种毒吗？”")
            print("\n妙音仙子声泪俱下：“不错，那两种药我已即刻为他解毒。但我竟不知他体内还有一种毒药，若我能及时发现，他也不至于...”")
            print("妙音仙子啼不成声，你仔细看了她一眼，那痛苦又不似作假。")
            clues.add("沈中三种毒")
            clues.add("毒药源锁定")
            variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
            variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1
            events_log.append("观察妙音仙子药瓶")

        elif choice == "5":
            print("\n她目光闪躲：“那密室钥匙有几把，我，管家和沈小姐都有钥匙。”")
            print("紧接着她拿出两个药瓶：“我发现沈庄主中了毒，其中两种毒药的空瓶就摆在密室桌上，我立刻为他解毒，没想到他身体里还有其他毒药，终究没能救的了他。毒药瓶子就是这两个。”")
            print("\n你十分惊讶：“沈庄主竟中了这么多毒？那剩下的毒药空瓶找到了么？”")
            print("\n妙音仙子眼中含泪：“没有找到，此事还得有劳特使尊驾了。”")
            clues.add("毒药瓶2")
            events_log.append("获得毒药瓶2")
            
            #二次询问才会打开隐藏窗口
            print("\n你仔细观察她脸上的神情：“仙子还有什么要补充的吗？”")
            
            if variables['truth_window_miaoyin'] == True:
                print("\n妙音仙子：“等一下，其实这空毒药瓶子上似乎有淡淡的水粉香味。”")
                print("\n你拿过瓶子轻轻嗅了一下，确实如此。：“山庄内近日女子出入不多，除了您和静慧师太...仙子莫非是在暗示沈小姐碰过这毒药瓶？”")
                print("\n妙音仙子：“也许是不小心沾上了也未可知。”")
                print("\n你：“多谢仙子。”")
                variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
                
            else:
                print("\n妙音仙子：“没有了。”")
                variables['suspect_miaoyin'] = variables.get('suspect_miaoyin', 0) + 1
                variables['emotion_miaoyin'] = variables.get('emotion_miaoyin', 0) + 1


        elif choice == "6":
            print("\n她摆摆手，神情憔悴：“希望阁下能早日破案，我也可以早日去陪他。”")
            break

        else:
            print("无效输入，请重新选择。")
    



