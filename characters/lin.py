import time # Ensure time imported if you use time.sleep
from dialogue_data import say, say_multiline,split_clues
def interact_with_lin(events_log, clues, variables, lang="en"):
    """
    与林修的多选互动模块
    :param events_log: 玩家行为日志
    :param clues: 玩家获得的线索集合
    :param variables: 状态变量 dict，如 {'emotion_lin': 0, 'suspect_lin': 0 'truth_window_lin', 'love_points': 0}
    """
    #print("林修 \n 身份：庄中孤儿，沈庄主抚养长大 \n 年龄：26岁 \n 人设关键词：隐忍、忠诚、有情有义 \n 背景信息：儿时被庄主带回抚养。似乎与沈澜衣关系匪浅。\n 公开信息：勤恳做事，是庄主最信任的年轻人之一。")
    #print("\n你来到后院，林修正在打水。他神色沉静，见你来，轻声道：“清音阁特使？”")
    
    print(say("lin_intro", lang))
    print()#start new line
    print(say("lin_greeting", lang))

    while True:
        #print("\n你想做什么？")
        #print("1. 偷偷观察他屋子的格局")
        #print("2. 听说沈庄主近日迁散众人，问他为何还留在山庄")
        #print("3. 诈一下他，说你知道就是他杀害了沈庄主")
        #print("4. 直接询问他和沈澜衣的关系")
        #print("5. 离开林修")
        #choice = input("请选择（输入数字）：")

        print()#add new line
        print(say("chat_start_prompt", lang))
        print("1. " + say("lin_choice_1", lang))
        print("2. " + say("lin_choice_2", lang))
        print("3. " + say("lin_choice_3", lang))
        print("4. " + say("lin_choice_4", lang))
        print("5. " + say("lin_choice_5", lang))

        choice = input(say("input_prompt", lang))#ask the user to enter their choice 1-5

        
        if choice == "1":
            #print("\n你查看他屋内陈设，未见灵位，却发现少许香灰。")
            #print("你获得了线索：少许香灰")
            #Print the full dialogue containing the clue
            print(say("lin_obs_result",lang))
            #clues.add("少许香灰")
            #clues.add(say("lin_obs_result", lang).split('：')[-1].strip())
            #re.split('[:：]', clues.add(say("lin_obs_result", lang))[-1].strip())
            # Use the new function to extract the clue
            extracted_clue = split_clues("lin_obs_result", lang)
            if extracted_clue: # Only add if a clue was successfully extracted
                clues.add(extracted_clue)
            #events_log.append("观察林修房间")
            events_log.append(say("log_obs_lin_room", lang)) # Corrected log key

        elif choice == "2":
            #print("\n林修低头，再次抬头时，眼神坚定：“我原是想走的，但澜衣在这……我又能去哪。”")
            print(say("lin_reason_stay",lang))
            
            variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            variables['love_points'] = variables.get('love_points', 0) + 1
            #events_log.append("追问林修未离开原因")
            events_log.append(say("log_reason_lin_stay", lang)) 
            # add log key for "log_reason_lin_stay"
        
        elif choice == "3":
            if not variables.get('truth_window_lin', False):
            #when "truth_window_lin" is false, or window doesn't exist, process logic below
                say_multiline("lin_memory_early", lang)
                variables['love_points'] = variables.get('love_points', 0) + 1
                variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            else:
                # only apply when "truth_window_lin" is opened(True)
                # also check if clue "少许香灰" or "Traces of incense ash" already collected.
                incense_clue_found = False
                for clue in clues:
                    if "香灰" in clue or "incense ash" in clue.lower():
                        incense_clue_found = True
                        break

                if variables.get('emotion_lin', 0) >= 5 and variables.get('love_points', 0) >= 4 and incense_clue_found:
                    # only if emotion_lin & love_points meet the requirements, tell truth
                    say_multiline("lin_confess_poison", lang)
                    variables['lin_confessed_poison_triggered'] = True #*****！！！*****
                    clues.add(say("clue_lin_access_miaoyin_medicine", lang))
                    clues.add(say("clue_lin_full_confession_seen", lang))
                else:
                    #standard reply when "truth_window_lin" is opened(True)
                    say_multiline("lin_deny_poison", lang)
            """
            if variables['truth_window_lin'] == False:
            #回忆身世
                memory_text = [
                "“林修声音有些颤抖：“我父母就葬在天泉山庄外的义庄，”",
                "“当年他们因为瘟疫来天泉山庄求药，沈庄主却没有赐药救人。”",
                "“我少年时期无意得知此事，心有愤懑，然我也知瘟疫乃是天灾，与天泉山庄无关。”",
                "“况且是沈庄主收留了我，若他没收留我，我怕是早已饿死街头；”",
                "“若没有他悉心教导，我又何来今日身手？。”",
                "“我唤他庄主，其实他也是我的‘师父’。有时候想起已逝的父母，我会偷偷祭祀，聊表哀思。”",
                "“无论如何，我那么爱澜衣，我怎么舍得让她难过...”",
                "他不再理会你，仿佛陷入了沉思。"
                ]
            
                import time
                for line in memory_text:
                    print(line)
                    time.sleep(1.5)  # 每句间隔1.5秒
                variables['love_points'] = variables.get('love_points', 0) + 1
                variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            
            else:
                if variables['emotion_lin']>=5 and variables['love_points'] >=4 and "少许香灰" in clues:
                    #林修身世曝光
                    memory_text = [
                        "“林修看着你，忽然笑了：“特使果然又来找我了。”",
                        "“不错，我确实给沈庄主下了毒。”",
                        "“那日澜衣来找我，商量与我私奔。”",
                        "“她说沈庄主和妙音仙子商量，准备假死隐退。”",
                        "“我本来不信，后来沈庄主将山庄库房钥匙全给了澜衣。”",
                        "“我想，沈庄主大概真的在计划一些事情，澜衣说的可能是真的。”",
                        "“澜衣打听到了沈庄主假死的时间安排，我被告知沈庄主会在密室闭关，",
                        "“澜衣劝说我那天夜里和她私奔，我答应了，为了走江湖安全起见，",
                        "“我还提前偷了一瓶妙音仙子配置好的毒药。”",
                        "“我担心澜衣打听到的情报日期时间不准确，万一沈庄主只是在密室日常修炼，",
                        "“那我俩一定会被抓回来，到时候我怕是小命不保。”",
                        "“出发前，我在沈庄主闭关的密室周围徘徊，我看见澜衣从里面慌慌张张跑了出来，",
                        "“我想沈庄主假死应该是真的了，我于是也进入了密室，由于担心沈庄主醒来的过快，将我俩抓回来，”",
                        "“我随手将从妙音仙子那处偷来的毒药喂给了沈庄主，我并不担心他的毒，反正妙音仙子会解。",
                        "“然后我随手将药瓶扔在了管家的门外。我到门口时候，澜衣还埋怨我怎么迟到了。",
                        "“整件事情就是这样。”"]
                    import time
                    for line in memory_text:
                        print(line)
                        time.sleep(1.5)  # 每句间隔1.5秒
                else:
                    #解释不是自己干的
                    memory_text = [
                        "“林修看着你，眼神十分镇定：“特使还是去别处看看，莫要在我这朗费功夫了。”",
                        "“沈庄主收留了儿时的我，我才有了活命的机会，我无心害他。”",
                        "“况且我爱上了澜衣，余生我也只想守着她，让她开心快乐。”"]
                    import time
                    for line in memory_text:
                        print(line)
                        time.sleep(1.5)  # 每句间隔1.5秒
            """


            
            variables['suspect_lin'] = variables.get('suspect_lin', 0) + 1
            #events_log.append("林修身世")
            events_log.append(say("log_lin_backstory", lang))
        
        elif choice == "4":
            #print("\n林修微微一笑：“她是我此生唯一所爱。”")
            print(say("lin_love_response",lang))
            variables['emotion_lin'] = variables.get('emotion_lin', 0) + 1
            #events_log.append("谈论澜衣")
            events_log.append(say("log_talk_lin_love", lang))
            #trigger for the truth window
            variables['truth_window_lin'] = True
        
        elif choice == "5":
            #print("\n你点头告辞，林修看着你离去的背影，似有所思。")
            print(say("lin_leave",lang))
            break

        else:
            #print("无效输入，请重新选择。")
            print(say("invalid_input",lang))
            
