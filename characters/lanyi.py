#from dialogue_data import say, say_multiline
#def interact_with_lanyi(events_log, clues, variables, lang='en'):
def interact_with_lanyi(events_log, clues, variables):
    """
    与沈澜衣的互动分支
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合（set）
    :param variables: 其他状态变量，如 {'emotion_lanyi': 0, 'suspect_lanyi': 0, 'truth_window_lanyi', 'love_points': 0}
    :param lang: "zh" or "en"
    """

    print("\n你来到湖心亭，沈澜衣倚栏独立，湖面波光粼粼。她神色凄苦，一转身望见你，向你微微行礼：“阁下便是清音阁特使？有劳了。”")

    print("沈澜衣 \n 身份：沈庄主之女 \n 年龄：22岁 \n 人设关键词：孝顺、敏感、敢爱敢恨 \n 背景信息：自幼聪慧，为人冷静，颇得庄主宠爱。最近被逼婚，却早已与林修私定终身。\n 公开信息：曾与父亲激烈争执，反对联姻，之后独居偏院。")

    while True:
        print("\n你想要问她什么？")
        print("1. 问她最近父亲有何异常")
        print("2. 询问她与林修的感情")
        print("3. 询问她知不知道毒药是哪里来的")
        print("4. 观察她的衣袖和随身物品")
        print("5. 安慰她，表达理解")
        print("6. 离开沈澜衣")

        choice = input("请选择（输入数字）：")

        if choice == "1":
            print("\n她点点头：“父亲曾亲口对我说，他不愿再纠缠于江湖旧怨，想借妙音姑姑之手脱身。”")
            clues.add("假死药真相")
            events_log.append("询问假死计划")
        
        elif choice == "2":
            print("\n她低声道：“我一直担心林修可能不会真的原谅父亲……但我还是希望，一切能有一个善终。”")
            print("\n她神色呆滞疲惫，眼中却藏着忧虑：“林修他心里藏着太多沉重，我只是想陪他一起放下。”")
            
            
            variables['love_points'] = variables.get('love_points', 0) + 1
            variables['emotion_lanyi'] = variables.get('emotion_lanyi', 0) + 1
            events_log.append("谈林修")
            if variables['truth_window_lanyi'] == True and variables['love_points'] >= 3:
                #说出自己下药的真相
                # 触发隐藏剧情
           
                memory_text = [
                "“事已至此，我没什么好隐瞒的了，是我……是我害死了爹。”",
                "“我和林修两情相悦，父亲却逼我和昆山派的聂清昭定亲，我十分不愿，和他大吵了一架。”",
                "“父亲后来把我关了一个月的禁闭。”她苦笑道",
                "“再之后我假意顺从，才被放了出来。上个月偶然偷听到父亲和妙音姑姑商量",
                "“二十年之约已到，父亲有意假死避战。”",
                "“我便和林修商量，想趁机私奔。父亲武艺高强，我不知妙音姑姑的假死药能让父亲‘假死’多久”",
                "“万一父亲醒来，发现我和林修私奔，肯定会吧我俩抓回来的”",
                "“于是我就去偷了妙音姑姑的毒药，我想着他中了假死药，身子虚，再灌下点毒……妙音姑姑解毒也需要时间。”",
                "她回忆道：“我动手之时，十分慌乱，毒粉散了出来，没有全给爹服下，反而大部分抖在了我的衣服上。”",
                "“我以为……我以为这样做我就能和林修永远离开天泉山庄。”",
                "“私奔那晚，林修来迟了，我还埋怨他怎么磨蹭。”",
                "“到了山门外，他解释说他心里不踏实，也……也喂了一瓶毒药给我爹。”",
                "“我们俩谁也没跟谁说……是走在山门外才对上口风的。我吓坏了！”",
                "“三种毒下在一人身上，林修还把瓶子扔了……我怕真的……真的出事。”",
                "“我求他回去，跪着求的。他不愿意，说此刻怕是已经出事了，回去就是自投罗网。我拿自己性命要挟，他才答应”",
                "“可我们赶回去时，爹已经……已经没气了。妙音姑姑没救回来……我……我也不配活着了……”"
                ]
            
                import time
                for line in memory_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒
            else:
                #说出自己和林相爱的往事
                memory_text = [
                "“我和林修……是从小一起长大的。”",
                "“他沉默寡言，却很照顾我。小时候我摔伤了腿，血流了一地”",
                "“是他小小年纪把我从山门一步一步背回来的，在路上他整个身体都在抖，”",
                "“我让他放我下来，我说我俩可以扶着一起走，他却不肯。”",
                "“后来我练剑偷懒，他也总在我爹面前替我遮掩。”",
                "“我以为……我俩会开心的一起长大。”她苦笑道",
                "“直到有一次，我见他一个人，在后院跪了一整夜。",
                "“我问他怎么了，他不肯说。后来我才知道，他的父母，死于一场二十年前的一场瘟疫。",
                "“那时江湖上流传天泉山庄后山生长的七寸三叶金钱树根可以解这疫症，",
                "“三叶金钱树乃是自然生成，本就不多，爹为了救人，把后山都快挖空了，”",
                "“尽管如此，还是不断有江湖人士前来上门求药，林修的父母便是其中之一。",
                "“后来舅舅和外祖母都染上了疫症……",
                "“后山的三叶金钱树早已被挖的没有了，父亲便下令把最后一根库房的七寸三叶金钱树根送去外祖家。",
                "“舅舅救过来了，但是外祖母也因此病故……而林修的父母，更是不治身亡。",
                "“林修……林修便是那林家遗孤。”",
                "“天泉山庄不想杀人，却……也没救他们。林修说过一句话我记得很清楚，他说：‘若是那年能有一节七寸三叶金钱树根，或许我还能有个娘抱着睡。”",
                "“我怕他恨爹。可他从没说过一句埋怨，只是越来越沉默寡言。”",
                "“后来有一天，他突然跟我说，他喜欢我。”"
                ]
            
                import time
                for line in memory_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒
                
                variables['love_points'] = variables.get('love_points', 0) + 1


        elif choice == "3":
            print("\n她愣了一下，随即避开你的目光：“若说用毒，那特使应该去问妙音姑姑，毕竟她们五毒教才是用毒高手。”")
            print("你感觉她隐瞒了什么。")
            variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
            events_log.append("质疑毒药线索")

        elif choice == "4":
            print("\n你观察她的衣袖，发现一缕淡淡的绿色痕迹，倒是与死者身上散落的毒药颜色相似。")
            clues.add("绿粉痕迹1")
            events_log.append("调查沈澜衣袖口")
            variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1
        
        elif choice == "5":
            print("\n你安慰了她，她朝你苦笑：“多谢。父亲突然去世，庄内事务皆是我在安排，招待不周请您鉴谅。”")
            variables['emotion_lanyi'] += 1
            events_log.append("安慰澜衣")
            #获得隐藏窗口
            variables['truth_window_lanyi'] = True
            
            #下面这是debug用的 为了开窗，等下删掉
            #variables['love_points'] = variables.get('love_points', 0) + 1

        elif choice == "6":
            print("\n你点头离去，沈澜衣背影伶仃，如湖心孤影。")
            break

        else:
            print("无效输入，请重新输入。")
