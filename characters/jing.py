import time
from dialogue_data import say, say_multiline, split_clues 
# Ensure split_clues is imported if needed


def interact_with_jing(events_log, clues, variables, lang="en"):
    """
    与静慧师太的互动模块
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合
    :param variables: 状态变量 dict，如 {'emotion_jing': 0, 'suspect_jing': 0,'truth_window_jing'}
    :param lang: "zh" or "en"-language
    """
    #print("静慧师太 \n 身份：玉泉院住持，华山派掌门陈奇曼好友 \n 年龄：56岁 \n 人设关键词：出家人不打诳语 \n 背景信息：受华山派掌门陈奇曼邀请，前来天泉山庄参与见证二十年之约，由于处理玉泉院事务，来迟了两个时辰。\n 公开信息：德高望重。")

    #print("\n你来到外院禅房，静慧师太正在打坐。她神色安逸，见到你来，温声道：“清音阁特使吧？请坐。”")

    print(say("jing_profile", lang))
    print(say("jing_greeting", lang))

    while True:
        #print("\n你想做什么？")
        print(say("chat_start_prompt", lang))
        #print("1. 直接询问静慧师太和陈奇曼的关系")
        #print("2. 听说静慧师太受邀见证二十年之约，何故迟到")
        #print("3. 询问静慧师太可曾注意任何异常")
        #print("4. 偷偷观察静慧师太房间")
        #print("5. 离开静慧师太")
        print("1. " + say("jing_choice_1", lang))
        print("2. " + say("jing_choice_2", lang))
        print("3. " + say("jing_choice_3", lang))
        print("4. " + say("jing_choice_4", lang))
        print("5. " + say("jing_choice_5", lang))

        #choice = input("请选择（输入数字）：")
        choice = input(say("input_prompt", lang))

        if choice == "1":
            #print("\n静慧师太点点头：“，陈掌门是我多年好友，我受邀前来见证沈陈二人二十年之约。据我所知，陈掌门已无杀心，这点我愿为他做保。”")
            print(say("jing_relation_chen_response", lang))
            variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
            variables['suspect_chen'] = variables.get('suspect_chen', 0) - 1
            #events_log.append("谈论陈奇曼")
            events_log.append(say("log_jing_talk_chen", lang))
        
        elif choice == "2":
            
            """
            chat_text = [
                "静慧师太无奈道：“近日玉泉院附近来了一些灾民，说是豫州大旱，且起了蝗灾”",
                "“玉泉院一直忙于安排他们住宿和释粥。”",
                "“三天前有弟子发现其中有人得了伤寒，玉泉院上下一直忙于备药分发。”",
                "“院中事物繁复，灾民众多，故而来迟了。”"
                ]
            
            import time
            for line in chat_text:
                print(line)
                time.sleep(1.5)  # 每句间隔1.5秒
            """
            say_multiline("jing_reason_late_dialogue", lang)

            variables['truth_window_jing'] = True
            ## active Jing truth window
            #触发静慧师太真话窗口
            variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
            #events_log.append("追问静慧师太为何晚来")
            events_log.append(say("log_jing_ask_why_late", lang))
        
        elif choice == "3":
            #if variables['truth_window_jing'] == True :
            if variables.get('truth_window_jing', False): 
            # Using .get for safety
            # 从 variables 字典中尝试获取键 'truth_window_jing' 对应的值；
            # 如果这个键不存在，就默认返回 False；
            # 如果这个键存在，就返回 True，然后执行if下面的模块。
            
                """

                chat_text = [
                    "静慧师太此次前来，还带了一个小徒弟。",
                    "小徒弟脸蛋圆圆的，一双眼睛滴溜溜的转，看起来有点活泼。",
                    "静慧师太回头问道：“妙真，凶案发生当天你可曾留意到有何异常么？”",
                    "“是的，掌门，那天后半夜，弟子听见外面有一对男女在争执，好像说什么迟到之类的。”",
                    "“因是半夜，声音格外清楚，持续时间不长，之后应该就离开了。”",
                    "“后来第二天传出沈庄主过世的消息，我随师父进入主院。”",
                    "“见到了沈小姐，那声音是沈小姐的。”",
                    "你选择相信静慧师和妙真师父。你对他们表示感谢，你怀疑沈小姐有一些秘密。"
                ]
                import time
                for line in chat_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒

                """     

                say_multiline("jing_disciple_testimony", lang)
            
                #events_log.append("你怀疑沈小姐有秘密")
                events_log.append(say("log_jing_suspect_lanyi_secret", lang))

                variables['suspect_jing'] = variables.get('suspect_jing', 0) - 1 # Reduce suspicion on Jing
                variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
                variables['suspect_lanyi'] = variables.get('suspect_lanyi', 0) + 1 # Increase suspicion on Lanyi
                


            else:
                """
                
                
                chat_text = [
                "静慧师太无奈道：“我傍晚方至，管家本安排我住进内院。”",
                "“但我生性喜静，我看外院有间禅房，便请管家安排我住在这里了。”",
                "“我一直打坐到深夜，外面的事务，我没有注意。”",
                "你对静慧师太表示感谢，但她一问三不知，反而让你觉得有点可疑。"
                ]
                import time
                for line in chat_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒
                """

                say_multiline("jing_no_abnormalities_dialogue", lang) 
                variables['suspect_jing'] = variables.get('suspect_jing', 0) + 1
                variables['emotion_jing'] = variables.get('emotion_jing', 0) - 1
                #events_log.append("你怀疑静慧师太")
                events_log.append(say("log_jing_suspect_jing", lang))
        
        elif choice == "4":
            #print("\n你偷偷观察静慧师太双手，发现指甲缝有些异色，像是药粉残留。")
            print(say("jing_hand_observation_result", lang))
            
            #print("你获得了线索：静慧师太手药粉痕迹")
            #clues.add("药粉痕迹")

            clues.add(say("clue_jing_powder_trace", lang))

            #events_log.append("观察静慧师太手部发现药粉")
            events_log.append(say("log_jing_observe_hand_powder", lang))
            
            #if variables['truth_window_jing'] == True :
            if variables.get('truth_window_jing', False):
                variables['emotion_jing'] = variables.get('emotion_jing', 0) + 1
                #静慧师太为了灾民伤寒治疗亲手做药，感动
                ## Increase emotion due to understanding
            else:
                variables['suspect_jing'] = variables.get('suspect_jing', 0) + 1
                #静慧师太手上可能就是残留毒药
                # Increase suspicion
        
        elif choice == "5":
            #print("\n你点头告辞，静慧师太看着你离去的背影，又开始打坐了。")
            print(say("jing_leave_dialogue", lang))
            break

        else:
            #print("无效输入，请重新选择。")
            print(say("invalid_input", lang))
