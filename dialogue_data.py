# dialogue_data.py
# 这个文件负责存储对话内容，支持中英双语
import re

DIALOGUES = {
    # ---最终指认菜单---
    "accuse_prompt": {
        "zh": "你最终指认的凶手是谁？",
        "en": "Who do you finally accuse as the culprit?"
    },
    "accuse_cancel": {
        "zh": "0. 返回主菜单",#不想现在猜，回到主菜单再溜达溜达。
        "en": "0. Return to Main Menu"
    },

    # --- 结局相关文本 ---
    "ending_title": {
        "zh": "结局揭晓",
        "en": "Ending Revealed"
    },

    # 结局 1: 证据不足，凶手逍遥法外 (未收集齐关键物证)
    "ending_failure_insufficient_evidence_msg": {
        "zh": "\n很遗憾，由于证据不足，仅凭你脑子里的怀疑，无法真正锁定凶手，凶手逍遥法外，天音阁的声望也被你影响。",
        "en": "\nRegrettably, due to insufficient evidence, your suspicions alone cannot truly pinpoint the culprit. The murderer remains at large, and Qingyin Pavilion's reputation has been affected by your failure."
    },
    "ending_failure_insufficient_evidence_name": {
        "zh": "证据不足，凶手逍遥法外",
        "en": "Insufficient Evidence, Culprit Remains at Large"
    },
    "ending_prompt_fail_options": {
        "zh": "按空格键结束游戏，按星号键（*）获取提示：",
        "en": "Press SPACE to end the game, press ASTERISK (*) for a hint:"
    },
    "ending_hint_fail": {
        "zh": "建议访问管家和妙音仙子，细心寻得作案工具。",
        "en": "Hint: Visit the Butler and Lady Miaoyin, and carefully look for the murder weapons."
    },

    # 结局 2: 真相大白，悲剧收场 (玩家完美指认林修)
    "ending_success_appraisal_msg": {
        "zh": "\n恭喜你，物证认证据在，你成功锁定了凶手，天音阁的声望自此大大增加。",
        "en": "\nCongratulations! With irrefutable physical and testimonial evidence, you've successfully identified the culprit. Qingyin Pavilion's prestige has significantly increased!"
    },
    "ending_true_killer_found_line": {
        "zh": "你成功找出了真凶：林修。\n 他并非蓄意杀人，而是误用毒药混合，导致庄主身亡。 \n 一场误会掀起了江湖悲剧，恩怨终成遗恨。",
        "en": "You successfully identified the true culprit: Lin Xiu.\n He did not kill intentionally, but accidentally mixed poisons, leading to the Master's death.\n A misunderstanding ignited a martial arts tragedy, and grudges ultimately became eternal regrets."
    },
    
    "ending_true_killer_name": {
        "zh": "真相大白，悲剧收场",
        "en": "Truth Revealed, Tragic End"
    },

    # 结局 3: 恋爱脑断案，误判忠贞 (指认林修，澜衣顶罪，玩家情感偏向林修)
    "ending_lanyi_jumps_in_for_lin": {
        "zh": "\n就在你即将指认林修时，沈澜衣突然冲了出来，跪倒在地，声泪俱下：“不！特使！凶手是我！与林修无关！”",
        "en": "\nJust as you were about to accuse Lin Xiu, Shen Lanyi suddenly rushed out, falling to her knees and weeping: 'No! Envoy! I am the murderer! It has nothing to do with Lin Xiu!'"
    },
    "ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_msg": {
        "zh": "你看着沈澜衣为爱顶罪，尽管心知她并非真凶，但你的情感偏向让你无法看清真相。最终，沈澜衣被定罪。",
        "en": "You watch Shen Lanyi take the blame for love, knowing in your heart she is not the true killer, yet your emotional bias prevents you from seeing the truth. Ultimately, Shen Lanyi is convicted."
    },
    "ending_lanyi_takes_blame_lin_emotion_high_lanyi_low_name": {
        "zh": "恋爱脑断案，误判忠贞",
        "en": "Love-Blind Judgment, Misjudged Loyalty"
    },
    "ending_tip_love_brain_damage": {
        "zh": "\n（提示：恋爱脑伤人啊，不要把emotion_lin刷的太高哦）",
        "en": "\n(Tip: Love makes you foolish; don't raise Lin Xiu's emotion points too high!)"
    },

    # 结局 4: 青天大判官，公正无私 (指认林修，澜衣顶罪，玩家情感公正)
    "ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_msg": {
        "zh": "沈澜衣为爱顶罪，但你头脑清醒，公正无私。你识破了她的苦心，决定深入调查，最终还林修清白。",
        "en": "Shen Lanyi takes the blame for love, but your mind is clear and impartial. You see through her earnest efforts and decide to investigate further, ultimately clearing Lin Xiu's name."
    },
    "ending_lanyi_takes_blame_lin_emotion_low_lanyi_high_name": {
        "zh": "青天大判官，公正无私",
        "en": "Impartial Judge, Selfless and Just"
    },
    "ending_jinghui_takes_lanyi_away": {
        "zh": "\n静慧师太上前，双手合十，叹息道：“阿弥陀佛，沈小姐，回头是岸。随贫尼去玉泉院清修吧。”她拉着沈澜衣，沈澜衣默默顺从，两人离去。",
        "en": "\nAbbess Jinghui stepped forward, clasped her hands, and sighed: 'Amitabha, Miss Shen, repentance is salvation. Come with this humble nun to Yuquan Monastery for quiet cultivation.' She took Shen Lanyi, who silently complied, and the two departed."
    },

    # 结局 5: 迷迷糊糊断案王 (指认林修但证据不全)
    "ending_muddled_judgment_message": { 
        "zh": "\n你抓到了凶手，但却迷迷糊糊，也说不清自己是怎么抓到的。天将神兵，你断案如神，但却不知其所以然。",
        "en": "\nYou caught the culprit, but vaguely, unable to explain how. Divine intervention, your judgment was swift, but without understanding."
    },
    "ending_muddled_judgment_name": {
        "zh": "迷迷糊糊断案王",
        "en": "Muddled Detective King"
    },

    # 结局 6: 指鹿为马，颠倒黑白 (知道真凶却指认他人)
    "ending_false_accusation_knew_truth_msg": {
        "zh": "\n你明明掌握了真凶的罪证，却指鹿为马，颠倒黑白。真凶逍遥法外，你的名声也因此蒙羞。",
        "en": "\nYou held the irrefutable evidence of the true culprit, yet you deliberately distorted the truth, accusing an innocent. The real murderer remains at large, and your reputation is now stained."
    },
    "ending_false_accusation_knew_truth_name": {
        "zh": "指鹿为马，颠倒黑白",
        "en": "Calling a Stag a Horse, Twisting Black into White"
    },

    # 结局 7a: 错判红颜，无辜受累 (指认沈澜衣但林修未被客观发现)
    "ending_false_accusation_lanyi_msg": {
        "zh": "你错误地指认了沈澜衣，她为此承受了不白之冤。真正的凶手逍遥法外。",
        "en": "You wrongly accused Shen Lanyi, and she bore the undeserved injustice. The true culprit remains at large."
    },
    "ending_false_accusation_lanyi_name": {
        "zh": "错判红颜，无辜受累",
        "en": "Misjudged Beauty, Innocent Suffers"
    },

    # 结局 7b: 错指掌门，威信受损 (指认陈奇曼但林修未被客观发现)
    "ending_false_accusation_chen_msg": {
        "zh": "你错误地指认了陈奇曼，他对此表示愤怒和不屑。真正的凶手逍遥法外。",
        "en": "You wrongly accused Chen Qiman, who responded with anger and disdain. The true culprit remains at large."
    },
    "ending_false_accusation_chen_name": {
        "zh": "错指掌门，威信受损",
        "en": "Wrongly Accused Sect Leader, Prestige Damaged"
    },

    # 结局 7c: 诬陷高僧，业障加身 (指认静慧师太但林修未被客观发现)
    "ending_false_accusation_jing_msg": {
        "zh": "你错误地指认了静慧师太，她对此报以慈悲的叹息。真正的凶手逍遥法外。",
        "en": "You wrongly accused Abbess Jinghui, who met your accusation with a compassionate sigh. The true culprit remains at large."
    },
    "ending_false_accusation_jing_name": {
        "zh": "诬陷高僧，业障加身",
        "en": "Slandered Monk, Karma Accumulates"
    },

    # 结局 7d: 误会重重，仙子蒙冤 (指认妙音仙子但林修未被客观发现)
    "ending_suspect_miaoyin_line": {
        "zh": "你怀疑妙音仙子是凶手。\n 她虽然深爱庄主，但毒药在她手中变成了杀人的利器。 \n 但你没有确凿证据证明她故意杀人，只能作为怀疑者离开。",
        "en": "You suspect Lady Miaoyin is the murderer. \n Although she deeply loved the Master, the poison in her hands became a deadly weapon. \n But you lack conclusive evidence that she killed intentionally, leaving you to depart as a mere suspect."
    },

    "ending_suspect_miaoyin_name": {
        "zh": "误会重重，仙子蒙冤",
        "en": "Heavy Misunderstanding, Lady Wronged"
    },

    # 结局 7e: 忠诚之谜，未解之谜 (指认老管家但林修未被客观发现)
    "ending_suspect_butler_line1": {
        "zh": "你怀疑老管家行凶。\n 但他的行为更像是忠诚与无奈，缺少杀意。 \n 你留下疑问，江湖恩怨未了。",
        "en": "You suspect the old butler of the crime. \n However, his actions seem more like loyalty and helplessness, lacking murderous intent. \n You leave with unanswered questions, the martial world's grievances unresolved."
    },
   
    "ending_suspect_butler_name": {
        "zh": "忠诚之谜，未解之谜",
        "en": "Mystery of Loyalty, Unsolved Enigma"
    },

    # 结局 8: 无果遗憾 (兜底结局)
    "ending_unresolved_line": {
        "zh": "你未能准确找到真凶。\n 沈庄主的死因成了无人能解的江湖秘事。\n 你只能带着遗憾离开。",
        "en": "You failed to accurately find the true culprit. \n Master Shen's cause of death remains an unsolved mystery in the martial world. \n You can only leave with regret. "
    },
    
    "ending_unresolved_name": {
        "zh": "无果遗憾",
        "en": "Unfruitful Regret"
    },



    # --- 结局相关文本 ---
    "ending_title": {
        "zh": "结局揭晓",
        "en": "Ending Revealed"
    },



    # --- General/System Messages ---
    "language_prompt": { # For choose_language()
        "en": "Choose your language:",
        "zh": "请选择语言："
    },
    "language_option_en": { # For choose_language()
        "en": "1. English",
        "zh": "1. English" # Displaying English option text even in Chinese mode
    },
    "language_option_zh": { # For choose_language()
        "en": "2. 中文",
        "zh": "2. 中文" # Displaying Chinese option text even in English mode
    },
    "language_input_prompt": { # For choose_language()
        "en": "Enter your choice (1 or 2):",
        "zh": "输入你的选择（1或2）："
    },
    # --- Player Name define ---
    "player_name_prompt": {
        "zh": "你好呀，你叫啥名啊？(空格或回车可跳过，默认名为：慕容泓): ",
        "en": "Hi there! what is your name? (Blank or Enter for default Name: Murong Hong): "
    },


    "game_welcome": { # For main()
        "zh": "🎮 欢迎来到《天泉山庄疑案》",
        "en": "🎮 Welcome to 'The Mystery of Tianquan Manor'"
    },
    #"player_intro": { # For main()
    #    "zh": "你是清音阁特使执事慕容泓，应掌教穆长风之命，协助调查天泉山庄沈天正庄主之死。\n",
    #    "en": "You are Murong Hong, special envoy of Qingyin Pavilion, \n entrusted by Master Mu Changfeng to aid in uncovering the truth behind \n the death of Tianquan Manor’s master, Shen Tianzheng. \n"
    #},

    "player_intro": { # Take player defined name
        "zh": "你是清音阁特使执事{player_name}，应掌教穆长风之命，协助调查天泉山庄沈天正庄主之死。",
        "en": "You are {player_name}, special envoy of Qingyin Pavilion, entrusted by Grandmaster Mu Changfeng to aid in uncovering the truth behind the death of Tianquan Manor’s master, Shen Tianzheng."
    },



    "main_menu_prompt": { # For main() loop
        "zh": "请选择你要调查的角色：",
        "en": "Please choose the character you wish to investigate:"
    },
    "character_lanyi": { # For main() menu option
        "zh": "沈澜衣",
        "en": "Shen Lanyi"
    },
    "character_chen": { # For main() menu option
        "zh": "陈奇曼",
        "en": "Chen Qiman"
    },
    "character_lin": { # For main() menu option
        "zh": "林修",
        "en": "Lin Xiu"
    },
    "character_miaoyin": { # For main() menu option
        "zh": "妙音仙子",
        "en": "Lady Miaoyin"
    },
    "character_butler": { # For main() menu option
        "zh": "老管家",
        "en": "The Old Butler"
    },
    "character_jing": { # For main() menu option
        "zh": "静慧师太",
        "en": "Abbess Jinghui"
    },
    "menu_view_log_clues": { # For main() menu option
        "zh": "查看调查日志",
        "en": "View Investigation Log"
    },
    "menu_end_investigation": { # For main() menu option
        "zh": "结束调查，进行推理\n>>>>>>>>",
        "en": "End Investigation, Begin Deduction\n>>>>>>>>"
    },


    #general questions

    "chat_start_prompt": {
        "zh": "\n你想做什么？",
        "en": "\nWhat would you like to do?"
    },

    "input_prompt": {
        "zh": "\n请选择（输入数字）：",
        "en": "\nPlease choose (enter number):"
    },
    "invalid_input": {
        "zh": "无效输入，请重新选择。",
        "en": "Invalid input, please choose again."
    },

    # --- Log and Clues Display ---
    "log_title": {
        "zh": "调查日志",
        "en": "Investigation Log"
    },
    "log_no_info": {
        "zh": "你还没有收集到任何线索或调查记录。",
        "en": "You haven't collected any clues or investigation records yet."
    },
    "log_progress_title": {
        "zh": "调查进展记录",
        "en": "Investigation Progress Log"
    },
    "log_clues_title": {
        "zh": "已收集线索",
        "en": "Clues Collected"
    },
    "log_suspicion_status_title": {
        "zh": "当前推测状态：",
        "en": "Current Suspicion Status:"
    },
    "log_suspect_you_suspect": {
        "zh": "你怀疑",
        "en": "You suspect"
    },
    "log_suspect_no_target": {
        "zh": "你暂时没有明确怀疑的对象。",
        "en": "You don't have a clear suspect at the moment."
    },
    "log_emotion_title": {
        "zh": "玩家对角色好感度",
        "en": "Player's favorability towards the Character"
    },
    "log_emotion_for": {
        "zh": "玩家好感度对",
        "en": "Emotion for" # e.g., "Emotion for Lin Xiu:"
    },
    "log_emotion_no_records": { # New
        "zh": "暂时没有玩家好感度记录。",
        "en": "No emotional records."
    },

    # --- Butler Dialogue ---
    "butler_profile": {
        "zh": "\n老管家 \n 身份：天泉山庄元老 \n 年龄：62岁 \n 人设关键词：忠仆、念旧 \n 背景信息：沈庄主的老部下，亦见证山庄盛衰。前不久刚刚与沈庄主发生口角，俩人不欢而散，\n 后来传出庄主强制让管家“退休”，管家本人据说当时显得十分愤怒。\n 公开信息：说话带刺，爱抱怨庄主无情\n",
        "en": "\nThe Old Butler \n Identity: Tianquan Manor Butler \n Age: 62 \n Traits: Loyal servant, nostalgic \n Background: Master Shen's subordinate for many years, also witnessed the rise of Tian Quan Manor. \n Had a quarrel with Master Shen recently, ending in an unpleasant conversation. \n It was later rumored that the Master forcibly 'retired' the butler, \n who was reportedly very angry at the time. \n Public Info: Speaks sharply, complains about the Master's ruthlessness\n"
    },
    "butler_greeting": {
        "zh": "你来到主厅，老管家正在为主厅整理供桌，动作迟缓，神色黯然。\n他听见脚步声抬头，看了你一眼，叹了口气：“尊驾是清音阁来的？\n你们阁主真是消息灵通，这么快就派人来了。\n请问吧，我定然知无不言，言无不尽。”",
        "en": "You arrive at the main hall. The old butler was slowly clearing the table in the hall, \n his expression was very serious. \n Hearing the footsteps, he raised his head, glanced at you, \n and sighed: 'You must be from Qingyin Pavilion? Your master is really well-informed. \n Sent someone over so quickly. Just ask and I will tell (you) everything I know.'"
    },

    # Butler choices
    
    "butler_choice_1": {
        "zh": "问他为何被庄主开除",
        "en": "Ask him why he was dismissed by Master Shen"
    },
    "butler_choice_2": {
        "zh": "问他对庄主的忠诚是否动摇",
        "en": "Ask if his loyalty to Master Shen wavered"
    },
    "butler_choice_3": {
        "zh": "询问庄主生前是否有异样",
        "en": "Asked if Master Shen had any abnormal behavior before his death"
    },
    "butler_choice_4": {
        "zh": "观察供桌与供果",
        "en": "Observe the altar and the fruits"
    },
    "butler_choice_5": {
        "zh": "暗示他可能对庄主下手",
        "en": "Suggesting that he may have harmed Master Shen"
    },
    "butler_choice_6": {
        "zh": "离开老管家",
        "en": "Leave the Old Butler"
    },

    # Butler short replies
    "butler_loyalty_response1": {
        "zh": "“我跟了庄主四十年，他吃喝拉撒都是我负责的，他的喜好连去世的沈夫人都没有我清楚。”",
        "en": "'I've served Master Shen for forty years; and I am responsible for his daily life, Even the late Mrs. Shen did not know Master Shen's preferences better than I do.'"
    },
    "butler_loyalty_response2": {
        "zh": "“我怎么会害他，我只是不放心他罢了。”",
        "en": "'How could I harm him? I was just worried about him.'"
    },
    "butler_master_unusual_response1": {
        "zh": "他思索道：“哎，最近庄主让妙音仙子整顿药房，然后吩咐将库房钥匙全部交给沈小姐。”",
        "en": "He said: 'Ah, recently Master Shen had Lady Miaoyin tidy up the pharmacy, and also asked me to give all warehouse keys to Miss Lan Yi for safekeeping.'"
    },
    "butler_master_unusual_response2": {
        "zh": "“还亲自拟了份遗书，只不过那遗书又被他自己烧了。”",
        "en": "'He also personally drafted a will, but then he burned it himself.'"
    },
    "butler_altar_observation1": {
        "zh": "你留意到屋内有一供桌，上面供奉着天泉山庄庄主沈天正的灵位，还摆着一些瓜果。",
        "en": "You notice an altar in the room, on which was enshrined the spirit tablet of Master Shen Tianzheng of Tianquan Manor, along with some fruits."
    },
    "butler_altar_observation2": {
        "zh": "你对着灵位上了根香，发现供桌下面有一个很精致的小红瓶。",
        "en": "You lit an incense stick for the spirit tablet and found a very delicate, small red bottle under the altar."
    },
    "butler_altar_no_hidden_clue": {
        "zh": "你上了香。",
        "en": "You lit the incense."
    },
    "butler_accusation_response": {
        "zh": "老管家苦笑：“你看我这把年纪，还能毒杀主子？清音阁真是多疑。”",
        "en": "The old butler smiled bitterly: 'At my age, do you truly believe I could still poison my master? The Qingyin Pavilion is ever distrustful, see shadows in every corner.'"
    },
    "butler_leave": {
        "zh": "你道声告辞，老管家默默点头，继续为供桌摆放花果。",
        "en": "'Goodbye.'you said. The old butler nodded silently and continued to place flowers and fruits on the altar."
    },

    # Butler related clues
    "clue_butler_silver_notes": {
        "zh": "管家获得银票补偿",
        "en": "Butler received compensation"
    },
    "clue_will_burned": {
        "zh": "遗书已被焚毁",
        "en": "Will has been burned"
    },
    "clue_poison_bottle_1": {
        "zh": "毒药瓶1",
        "en": "Poison Bottle 1"
    },
    "clue_altar_spirit_tablet": {
        "zh": "供桌灵位",
        "en": "Altar Spirit Tablet"
    },

    # Butler related event logs
    "log_ask_butler_fired": {
        "zh": "询问管家被开除原因",
        "en": "Asked butler about dismissal reason"
    },
    "log_ask_butler_loyalty": {
        "zh": "探问管家忠诚",
        "en": "Probed butler's loyalty"
    },
    "log_ask_master_unusual": {
        "zh": "获取遗书情报",
        "en": "Acquired will information"
    },
    "log_gain_poison_bottle_1": {
        "zh": "获得毒药瓶1",
        "en": "Gained Poison Bottle 1"
    },
    "log_observe_butler_altar": {
        "zh": "观察供桌表面",
        "en": "Observed altar surface"
    },
    "log_accuse_butler": {
        "zh": "质疑管家动机",
        "en": "Questioned butler's motive"
    },



    #lanyi dialogue
    "lanyi_intro_scene": {
        "zh": "你来到湖心亭，沈澜衣倚栏独立……她神色凄苦，一转身望见你，向你微微行礼：“阁下便是清音阁特使？有劳了。”\n",
        "en": "You arrive at the lakeside pavilion. Shen Lanyi leans on the railing... \n She turns and nods to you: 'You must be the envoy from Qingyin Pavilion. \n Thank you for coming.'\n "
    },
    "lanyi_profile": {
        "zh": "\n沈澜衣 \n 身份：沈庄主之女 \n 年龄：22岁 \n 人设关键词：孝顺、敏感、敢爱敢恨 \n 背景信息：自幼聪慧，为人冷静，颇得庄主宠爱。最近被逼婚，却早已与林修私定终身。\n 公开信息：曾与父亲激烈争执，反对联姻，之后独居偏院。”\n",
        "en": "\nLanyi Shen \n Identity: Daughter of the Villa Master \n Age: 22 \n Character: Filial, sensitive, passionate in love and hate \n Background: Intelligent since childhood and calm by nature, she was greatly favored by her father. \n Recently forced into an arranged marriage, \n though she has already secretly pledged herself to Lin Xiu. \n Public Info: Known to have had a fierce argument with her father over the marriage and now lives alone in the extra courtyard beside.\n "
    },
    
    # Lanyi choices
    "lanyi_choice_1": {
        "zh": "询问她父亲近日有何异常",
        "en": "Ask her if her father has behaved in any unusual way recently"
    },
    "lanyi_choice_2": {
        "zh": "询问她与林修的感情",
        "en": "Ask her about her relationship with Lin Xiu"
    },
    "lanyi_choice_3": {
        "zh": "询问她知不知道毒药是哪里来的",
        "en": "Ask her if she knows where the poison came from"
    },
    "lanyi_choice_4": {
        "zh": "观察她的衣袖和随身物品",
        "en": "Observe her sleeves and personal belongings"
    },
    "lanyi_choice_5": {
        "zh": "安慰她，表达理解",
        "en": "Comfort her, express understanding"
    },
    "lanyi_choice_6": {
        "zh": "你准备离开了。",
        "en": "You decide to leave." 
    },

    # lanyi short replies
    "ask_lanyi_father": {
        "zh": "她点点头：“父亲曾亲口对我说，他不愿再纠缠于江湖旧怨，想借妙音姑姑之手脱身。”",
        "en": "She nods, 'Father told me that—he no longer wished to be tangled in old grudges, and planned to fake his death with Aunt Miaoyin’s help.'"
    },
    "ask_lanyi_love": {
        "zh": "她低声道：“我一直担心林修可能不会真的原谅父亲……但我还是希望，一切能有一个善终。”",
        "en": "She murmurs, 'I’ve always worried Lin Xiu might never truly forgive Father... But I still hope things can end peacefully.'"
    },
    "lanyi_love_details": {
        "zh": "她神色呆滞疲惫，眼中却藏着忧虑：“林修他心里藏着太多沉重，我只是想陪他一起放下。”",
        "en": "Her expression is dull and weary, but her eyes hide a deep worry: 'Lin Xiu carries too much weight in his heart; I just want to help him let it go.'"
    },
    "ask_lanyi_poison": {
        "zh": "她愣了一下，随即避开你的目光：“若说用毒，那特使应该去问妙音姑姑，毕竟她们五毒教才是用毒高手。”",
        "en": "She pauses, then avoids your gaze. 'If you want to ask about poison, you should talk to Aunt Miaoyin. The Five Venoms Sect are the true experts in poison.'"
    },
    "lanyi_suspicion": {
        "zh": "你感觉她隐瞒了什么。",
        "en": "You sense she is hiding something."
    },
    "lanyi_sleeve_obs_result": {
        "zh": "你观察她的衣袖，发现一缕淡淡的绿色痕迹，倒是与死者身上散落的毒药颜色相似。",
        "en": "You observe her sleeve and find a faint green trace, similar in color to the poison scattered on the deceased."
    },
    "comfort_lanyi": {
        "zh": "你安慰了她，她朝你苦笑：“多谢。父亲突然去世，庄内事务皆是我在安排，招待不周请您鉴谅。”",
        "en": "You offer her some comfort. She forces a bitter smile. 'Thank you. With Father gone, I’ve been managing everything alone... Forgive me if I’ve been a poor host.'"
    },
    "leave_lanyi": {
        "zh": "你点头离去，沈澜衣背影伶仃，如湖心孤影。",
        "en": "You nod and take your leave. Shen Lanyi’s lonely silhouette remains by the lake, like an isolated shadow." 
    },
    
    # Lanyi related clues (text added to clues set)
    "clue_fake_death_truth": {
        "zh": "假死药真相",
        "en": "Fake Death Potion Truth"
    },
    "clue_green_trace_1": {
        "zh": "绿粉痕迹1",
        "en": "Green Powder Trace 1"
    },
    
    # Lanyi related event logs
    "log_ask_lanyi_fake_death": {
        "zh": "询问澜衣假死计划",
        "en": "Asked Lanyi about fake death plan"
    },
    "log_talk_lanyi_love": {
        "zh": "谈论澜衣与林修感情",
        "en": "Discussed Lanyi and Lin Xiu's relationship"
    },
    "log_question_lanyi_poison": {
        "zh": "质疑澜衣毒药线索",
        "en": "Questioned Lanyi about poison clue"
    },
    "log_observe_lanyi_sleeve": {
        "zh": "调查沈澜衣袖口",
        "en": "Investigated Shen Lanyi's sleeve"
    },
    "log_comfort_lanyi": {
        "zh": "安慰澜衣",
        "en": "Comforted Lanyi"
    },
    

    # lin dialogue choices
    "lin_intro": {
        "zh": "\n林修 \n 身份：庄中孤儿，沈庄主抚养长大 \n 年龄：26岁 \n 人设关键词：隐忍、忠诚、有情有义 \n 背景信息：儿时被庄主带回抚养。似乎与沈澜衣关系匪浅。\n 公开信息：勤恳做事，是庄主最信任的年轻人之一。\n",
        "en": "\nLin Xiu \n Identity: An orphan raised by Master Shen in Tianquan Manor \n Age: 26 \n Traits: Stoic, loyal, devoted \n Background: Rescued and raised by Master Shen as a child. \n Seems to have a close relationship with Shen Lanyi. \n Public Info: Hardworking and loyal, trusted by Master Shen.\n "
    },
    "lin_greeting": {
        "zh": "你来到后院，林修正在煮茶。他神色沉静，见你来，轻声道：“清音阁特使？”\n",
        "en": "You arrive at the backyard. Lin Xiu is making tea. \n He looks calm, and upon seeing you, speaks softly: \n'Envoy from Qingyin Pavilion?'\n"
    },

    "lin_choice_1": {
        "zh": "偷偷观察他屋子的格局",
        "en": "Secretly observe the layout of his room"
    },
    "lin_choice_2": {
        "zh": "听说沈庄主近日迁散众人，问他为何还留在山庄",
        "en": "Ask why he still stayed when others were all dismissed by Master Shen"
    },
    "lin_choice_3": {
        "zh": "诈一下他，说你知道就是他杀害了沈庄主",
        "en": "Bluff and just say you know he murdered Master Shen"
    },
    "lin_choice_4": {
        "zh": "直接询问他和沈澜衣的关系",
        "en": "Ask directly about his relationship with Shen Lanyi"
    },
    "lin_choice_5": {
        "zh": "离开林修",
        "en": "Leave Lin Xiu"
    },

    #lin clues

    "clue_lin_access_miaoyin_medicine": {
        "zh": "林修接触妙音仙子药物",
        "en": "Lin Xiu accessed Lady Miaoyin's medicine"
    },
   
    "clue_lin_full_confession_seen": {
        "zh": "林修完整供述",
        "en": "Lin Xiu's complete confession"
    },
    

    # lin dialogue short replies
    "lin_obs_result": {
        "zh": "你查看他屋内陈设，未见灵位，却发现少许香灰。 \n 你获得了线索：少许香灰",
        "en": "You inspect the room's layout. No spirit tablet, but you notice traces of incense ash. \n Clue acquired: Traces of incense ash"
    },
    "lin_reason_stay":{
        "zh": "林修低头，再次抬头时，眼神坚定：“我原是想走的，但澜衣在这……我又能去哪。",
        "en": "Lin Xiu lowers his head, then looks up again, his eyes firm: 'I originally intended to leave, but Lanyi is here... where else could I go?'"
    },
    "lin_love_response": {
        "zh": "林修微微一笑：“她是我此生真爱。”",
        "en": 'Lin Xiu smiles faintly: "She is the true love of mine."'
    },
    "lin_leave": {
        "zh": "你点头告辞，林修看着你离去的背影，似有所思。",
        "en": "You nod and take your leave. Lin Xiu watches your back thoughtfully."
    },
    "log_obs_lin_room": {
        "zh": "观察林修房间",
        "en": "Observed Lin Xiu's room"
    },
    "log_reason_lin_stay": {
        "zh": "追问林修未离开原因",
        "en": "Asked why Lin Xiu remained here"
    },
    "log_lin_backstory": {
        "zh": "林修身世",
        "en": "Lin Xiu's backstory"
    },
    "log_talk_lin_love": {
        "zh": "谈论澜衣",
        "en": "Discussed Lanyi"
    },

    #Chen Qiman dialogue
    "chen_profile": {
        "zh": "\n 陈奇曼 \n 身份：华山派掌门 \n 年龄：50岁 \n 人设关键词：刚正、沉稳、外冷内柔 \n 背景信息：当年其幼子陈一峰品行不端，当街强抢民女，被天泉沈庄主误杀。\n 失子之后痛不欲生，发誓与沈庄主不共戴天。后经清音阁掌教穆长风调停， \n 二人约定二十年后在天泉山庄决一死战。二十年来掌管华山派，心境逐渐平和。\n 公开信息：此次前来是为履行当年之约，表面上仍不冷不热。\n",
        "en": "\n Chen Qiman \n Identity: Huashan Sect Leader \n Age: 50 \n Traits: Upright, composed, outwardly cold but inwardly gentle \n Background: His young son, Chen Yifeng, misbehaved years ago, forcibly seizing a woman on the street, and was accidentally killed by Master Shen of Tianquan Manor. \n Overwhelmed with grief after losing his son, Chen Qiman swore eternal enmity with Master Shen. Later, mediated by Grandmaster Mu Changfeng of Qingyin Pavilion, the two agreed to a decisive battle at Tianquan Manor twenty years later. Having managed the Huashan Sect for twenty years, his state of mind has gradually become peaceful. \n Public Info: He is here to fulfill the long-standing agreement, outwardly still indifferent.\n "
    },
    "chen_greeting_intro1": {
        "zh": "你来到偏厅，陈奇曼正独自喝茶。你听闻他是当年陈一峰之父，与沈庄主积怨已久。",
        "en": "You arrive at the side hall. Chen Qiman is drinking tea alone. You've heard he is Chen Yifeng's father, and has harbored a long-standing grudge against Master Shen."
    },
    "chen_greeting_intro2": {
        "zh": "他抬眼望你：“如此年轻，竟是清音阁特使执事？真是江山代有才人出，后生可畏啊。”",
        "en": "He looks up at you: 'So young, yet an envoy from Qingyin Pavilion? Indeed, every era produces its talents; the younger generation is truly formidable.'"
    },
    "chen_greeting_player_reply": {
        "zh": "你盯着他，道“陈掌门过奖了。”",
        "en": "You look at him and say, 'Sect Leader Chen, you flatter me.'"
    },

    # Chen choices
    
    "chen_choice_1": {
        "zh": "问他是否真的已放下仇恨",
        "en": "Ask if he has truly let go of his hatred"
    },
    "chen_choice_2": {
        "zh": "询问他与沈庄主最后见面情况",
        "en": "Ask about his last meeting with Master Shen"
    },
    "chen_choice_3": {
        "zh": "暗示他其实并未原谅沈庄主",
        "en": "Hint that he hasn't actually forgiven Master Shen"
    },
    "chen_choice_4": {
        "zh": "留意他手边茶壶与药瓶是否有异常",
        "en": "Observe if the teapot and medicine bottles by his hand are unusual"
    },
    "chen_choice_5": {
        "zh": "直接质问是否下了毒手",
        "en": "Directly question if he used poison"
    },
    "chen_choice_6": {
        "zh": "离开陈奇曼",
        "en": "Leave Chen Qiman"
    },

    # Chen short replies
    "chen_last_meeting_dialogue1": {
        "zh": "“我们没有再动手。”他皱眉：“只是比了一招掌力，然后喝了几盏酒，言尽于此。”",
        "en": "'There was no further fighting.' He frowned. 'Just one exchange of palms — then a few cups of wine, and nothing more was said.'"
    },
    
    "chen_last_meeting_dialogue2": {
        "zh": "你感受到一种压抑的克制。",
        "en": "You can feel a heavy restraint held tightly within him."
    },
    
    "chen_hint_unforgiven_dialogue1": {
        "zh": "陈奇曼冷笑一声：“你是说我演戏？”",
        "en": "Chen Qiman let out a cold laugh. 'Are you accusing me of playing a part?'"
    },
    
    "chen_hint_unforgiven_dialogue2": {
        "zh": "“我若要杀人，岂会藏头露尾？”",
        "en": "'If I sought blood, would I skulk in shadows?'"
    },
    
    "chen_direct_accusation_observation": {
        "zh": "他的反应真切，似乎并无杀机。",
        "en": "His response feels sincere — no trace of killing intent in his manner."
    },

    "chen_leave_dialogue": {
        "zh": "陈奇曼不再说话，低头饮茶。你起身离去，只觉此人深不可测。",
        "en": "Chen Qiman said no more, lowering his gaze as he sipped his tea. \n You rose and took your leave, a single thought lingering — this man is far deeper than he appears."
    },

    # Chen related clues
    "clue_no_victory_in_fight": {
        "zh": "比掌未决胜负",
        "en": "Palm-strike ended without clear victor"
    },
    "clue_chen_injured": {
        "zh": "陈奇曼受伤",
        "en": "Chen Qiman was injured"
    },
    "clue_huashan_wounds_medicine": {
        "zh": "华山派金疮药",
        "en": "Huashan Sect Healing Balm"
    },
    "clue_chen_antidote_pill": {
        "zh": "陈奇曼解毒丸",
        "en": "Chen Qiman's Antidote Pill"
    },

    # Chen related event logs
    "log_chen_claim_resolved_feud": {
        "zh": "陈奇曼声称放下仇恨",
        "en": "Chen Qiman claimed to have resolved hatred"
    },
    "log_chen_last_meeting": {
        "zh": "了解陈奇曼与沈庄主对话内容",
        "en": "Learned about Chen Qiman's conversation with Master Shen"
    },
    "log_chen_probe_true_attitude": {
        "zh": "试探陈奇曼真实态度",
        "en": "Probed Chen Qiman's true attitude"
    },
    "log_chen_check_items": {
        "zh": "检查陈奇曼物品",
        "en": "Checked Chen Qiman's items"
    },
    "log_chen_direct_accusation": {
        "zh": "质问陈奇曼是否下毒手",
        "en": "Questioned Chen Qiman about poisoning"
    },
    
    # --- Jinghui Dialogue ---
    "jing_profile": {
        "zh": "\n静慧师太 \n 身份：玉泉院住持，华山派掌门陈奇曼好友 \n 年龄：56岁 \n 人设关键词：出家人不打诳语 \n 背景信息：受华山派掌门陈奇曼邀请，前来天泉山庄参与见证二十年之约，由于处理玉泉院事务，来迟了两个时辰。\n 公开信息：德高望重。\n ",
        "en": "\nAbbess Jinghui \n Identity: Abbess of Jade Spring Monastery; a longtime friend of Chen Qiman, leader of the Huashan Sect.\nAge: 56 \nTraits: A monastic who speaks no untruths.\nBackground: Invited by Sect Leader Chen Qiman to witness the twenty-year pact at Tianquan Manor. She arrived two hours late, delayed by affairs at Jade Spring Monastery. \n Public Info: Held in high esteem across the martial world.\n"
    },
    "jing_greeting": {
        "zh": "你来到外院禅房，静慧师太正在打坐。她神色安逸，见到你来，温声道：“清音阁特使吧？请坐。”",
        "en": "You arrive at the meditation room in the outer courtyard. \n Abbess Jinghui is seated in quiet meditation, her expression serene. Upon seeing you, \n she speaks gently: 'You must be the envoy from Qingyin Pavilion. Please, have a seat.'"
    },

    # Jing choices
    "jing_choice_1": {
        "zh": "直接询问静慧师太和陈奇曼的关系",
        "en": "Directly ask Abbess Jinghui about her relationship with Chen Qiman"
    },
    "jing_choice_2": {
        "zh": "听说静慧师太受邀见证二十年之约，何故迟到",
        "en": "They say Abbess Jinghui was called to witness the vow made twenty years ago — ask why did she arrive late?"
    },
    "jing_choice_3": {
        "zh": "询问静慧师太可曾注意任何异常",
        "en": "Ask Abbess Jinghui if she noticed anything unusual"
    },
    "jing_choice_4": {
        "zh": "偷偷观察静慧师太房间",
        "en": "Secretly observe Abbess Jinghui's room"
    },
    "jing_choice_5": {
        "zh": "离开静慧师太",
        "en": "Leave Abbess Jinghui"
    },

    # Jing short replies
    "jing_relation_chen_response": {
        "zh": "静慧师太点点头：“，陈掌门是我多年好友，我受邀前来见证沈陈二人二十年之约。据我所知，陈掌门已无杀心，这点我愿为他做保。”",
        "en": "Abbess Jinghui nodded gently. \n'Sect Leader Chen has been a friend of mine for many years. \n I was invited to witness the twenty-year pact between him and Master Shen. \n To my knowledge, he bears no intent to kill, on this, I am willing to stand as his guarantor.'"
    },
    "jing_hand_observation_result": {
        "zh": "你偷偷观察静慧师太双手，发现指甲缝有些异色，像是药粉残留。",
        "en": "You quietly study Abbess Jinghui's hands and notice \n a faint, unusual tint beneath her fingernails, \n as if some medicinal powder still clings there."
    },
    "jing_leave_dialogue": {
        "zh": "你点头告辞，静慧师太看着你离去的背影，又开始打坐了。",
        "en": "You nod and take your leave. \n Abbess Jinghui watches your departing figure in silence, \n then quietly returns to her meditation."
    },

    # Jing related clues
    "clue_jing_powder_trace": {
        "zh": "药粉痕迹",
        "en": "Medicine Powder Trace"
    },

    # Jing related event logs
    "log_jing_talk_chen": {
        "zh": "谈论陈奇曼",
        "en": "Discussed Chen Qiman"
    },
    "log_jing_ask_why_late": {
        "zh": "追问静慧师太为何晚来",
        "en": "Asked Abbess Jinghui why she was late"
    },
    "log_jing_suspect_lanyi_secret": {
        "zh": "你怀疑沈小姐有秘密",
        "en": "You suspect Miss Shen has a secret"
    },
    "log_jing_suspect_jing": {
        "zh": "你怀疑静慧师太",
        "en": "You suspect Abbess Jinghui"
    },
    "log_jing_observe_hand_powder": {
        "zh": "观察静慧师太手部发现药粉",
        "en": "Observed Abbess Jinghui's hand, found powder"
    },


     # --- Miaoyin Dialogue ---
    "miaoyin_profile": {
        "zh": "\n 妙音仙子\n 身份：用毒高手，庄主旧识\n 年龄：38岁\n 人设关键词：冷艳、深情、危险\n 背景信息：原为沈庄主徒弟，后不明原因叛出师门改投五毒教，\n 如今为五毒教高阶长老。近年来与沈庄主关系匪浅，可谓红颜知己。\n 特长：擅制毒解毒；精音律善古琴。",
        "en": "\n Lady Miaoyin\n Identity: Master of Poisons, Old Acquaintance of the Master\n Age: 38\n Traits: Cold & enchanting, deeply affectionate, dangerous\n Background: Originally Master Shen's disciple, she later inexplicably left the sect to join the Five Venoms Sect, now a high-ranking elder. In recent years, her relationship with Master Shen has been intimate, a true confidante.\n Specialty: Skilled in making and detoxifying poisons; proficient in music and ancient guqin."
    },
    "miaoyin_greeting": {
        "zh": "你在后山石亭找到妙音仙子，她独自坐着，手里把玩着两枚药瓶。\n“你来了。”她轻轻一笑，“想问我为何没能把他救回来吧？”",
        "en": "You find Lady Miaoyin in the back mountain stone pavilion, sitting alone, toying with two medicine bottles.\n'You're here.' She smiles softly, 'You've come to ask why I couldn't save him, haven't you?'"
    },

    # Miaoyin choices
    
    "miaoyin_choice_1": {
        "zh": "诈一下她，问她为何要给庄主下毒",
        "en": "Bluff her, ask why she poisoned the Master"
    },
    "miaoyin_choice_2": {
        "zh": "询问她作为用毒高手，发现意外后，有否立刻施救沈庄主",
        "en": "Ask her, as a master of poisons, if she immediately tried to save Master Shen after discovering the incident"
    },
    "miaoyin_choice_3": {
        "zh": "打探她与庄主的关系",
        "en": "Inquire about her relationship with the Master"
    },
    "miaoyin_choice_4": {
        "zh": "观察她屋内的毒药/药瓶",
        "en": "Observe the poisons/medicine bottles in her room"
    },
    "miaoyin_choice_5": {
        "zh": "试探她是否知道有其他人可以打开庄主密室",
        "en": "Probe if she knows if anyone else could open the Master's secret chamber"
    },
    "miaoyin_choice_6": {
        "zh": "离开妙音仙子",
        "en": "Leave Lady Miaoyin"
    },

    # Miaoyin short replies
    "miaoyin_bluff_response": {
        "zh": "“我没下毒。”她冷笑，“那是他求我的。他说只要假死，就能逃脱那场宿命的比武。\n 我给他的，只是让心跳假停三日的‘三日息’，三日之后服下解药即可清醒。”",
        "en": "'I didn't poison him.' She sneered, 'He begged me to. He said if he faked his death, he could escape that destined duel.\n What I gave him was merely the [Three-Day Slumber], \n  which weaks the heartbeat for three days; he would awaken after taking the antidote on the third day.'"
    },
    
    "miaoyin_no_rescue_response": {
        "zh": "“他服下的是我给他的假死药，我本想守着待他三日后醒来。”她低头苦笑，“可当我推门进屋……发现他身中剧毒。\n 有人趁我不在，给他下了别的毒。”",
        "en": "'He took the fake death potion I gave him. I intended to stay and wait for him to awaken after three days.' She smiled bitterly, lowering her head, \n 'But when I pushed the door open... I found he was severely poisoned.\n Someone poisoned him with something else while I was away.'"
    },
    
    "miaoyin_relationship_response": {
        "zh": "她神情复杂：“当年我与他是师徒，他还未成亲，我爱慕他，却他却严词拒绝了。”\n“我一气之下叛出师门，拜了五毒教，后来经过一些事情，我们又遇见了。”\n “后来他说，这次假死之后，愿与我归隐。”",
        "en": "Her expression was complex: 'Years ago, he was my master. Before he married, I admired him, but he sternly rejected me.\n In a fit of anger, I left the sect and joined the Five Venoms Sect. After some time, we met again.\n Later, he said that after this fake death, he wished to retire with me.'"
    },
    

    "miaoyin_ask_more": {
        "zh": "你仔细观察她脸上的神情：“仙子还有什么要补充的吗？”",
        "en": "You scrutinize her expression: 'Is there anything else you wish to add, Lady Miaoyin?'"
    },
    
    "miaoyin_no_more_info": {
        "zh": "妙音仙子：“没有了。”",
        "en": "Lady Miaoyin: 'Nothing else.'"
    },
    "miaoyin_leave_dialogue": {
        "zh": "她摆摆手，神情憔悴：“希望阁下能早日破案，我也可以放下心结，早日去陪他。”",
        "en": "She waved her hand, her expression haggard: 'I hope you can solve the case soon, so I can release this burden and join him earlier.'"
    },

    # Miaoyin related clues
    "clue_promise_of_reclusion": {
        "zh": "归隐约定",
        "en": "Promise of Reclusion"
    },
    "clue_someone_else_poisoned": {
        "zh": "有人投毒",
        "en": "Someone else poisoned"
    },
    "clue_former_master_disciple": {
        "zh": "曾为师徒",
        "en": "Once Master and Disciple"
    },
    "clue_multiple_poisons": {
        "zh": "沈身中多种毒药",
        "en": "Shen afflicted by multiple poisons"
    },
    "clue_poison_source_identified": {
        "zh": "毒药源锁定",
        "en": "Poison source identified"
    },
    "clue_poison_bottleX2": {
        "zh": "获得毒药瓶x2",
        "en": "Gained Two Poison Bottles"
    },
     "clue_suspect_lanyi_access_miaoyin_medicine": {
        "zh": "沈澜衣接触过妙音仙子药物",
        "en": "Lanyi accessed Lady Miaoyin's medicine"
    },
    

    # Miaoyin related event logs
    "log_miaoyin_fake_death_claim": {
        "zh": "假死之说",
        "en": "Claim of Fake Death"
    },
    "log_miaoyin_failed_rescue": {
        "zh": "妙音仙子未能解毒",
        "en": "Lady Miaoyin failed to detoxify"
    },
    "log_miaoyin_relationship_history": {
        "zh": "了解妙音仙子关系史",
        "en": "Learned Lady Miaoyin's relationship history"
    },
    "log_miaoyin_observe_bottles": {
        "zh": "观察妙音仙子药瓶",
        "en": "Observed Lady Miaoyin's medicine bottles"
    },
    "log_miaoyin_gain_poison_bottle_x_2": {
        "zh": "获得毒药瓶x2",
        "en": "Gained Poison Bottle x 2"
    }

}

MULTILINE_DIALOGUES = {
    # --- Butler Multiline Dialogue ---
    "butler_reason_fired": {
        "zh": [
            "“哎，其实我本来也不理解...还很生气，但...”",
            "“庄主后来跟我私下道了个歉。”他眼眶泛红...",
            "“他只说怕仇家寻仇，劝我尽快离开天泉山庄。”",
            "“他还给了我一笔养老银子，我并不怨他。”"
        ],
        "en": [
            "'I didn't understand at first... and was very angry, but...'",
            "'Master Shen apologized to me privately later on.' His eyes reddened...",
            "'He only said he feared enemies seeking revenge and urged me to leave Tianquan Manor ASAP.'",
            "'He also gave me a large pension for my retirement. I don't resent him.'"
        ]
    },
    "butler_hidden_bottle_story": { 
        "zh": [
            "你伸手把瓶子捡了起来“你这瓶子倒是十分精致。”",
            "管家显得神色有些慌张",
            "“这瓶子是我在房门外捡的。”",
            "你目光灼灼盯着管家观察",
            "“其实后来我发现，这瓶子是妙音仙子用来装毒药的”他眼眶泛红...",
            "“妙音仙子或许就是杀害庄主的真凶，还请清音阁为我们天泉山庄做主。”见老管家要给你跪下，你一把扶起他。",
            "你面色不悦：“既然如此，方才为何不说。”",
            "老管家神情不安道：“妙音仙子善毒，我怕她杀我灭口。”",
            "老管家神色逐渐变得有些惭愧：“其实，我见你如此年轻，也不知能力几何，故意将瓶子留在地上，也想试探你一二。”",
            "“原来如此。”你点点头，拿走了瓶子。"
        ],
        "en": [
            "You reached out and picked up the bottle. 'This bottle is quite exquisite.'",
            "The butler looked a bit flustered.",
            "'I found this bottle outside the door.'",
            "You gazed intently at the butler.",
            "'Actually, I found out this bottle is what Lady Miaoyin usually uses for her poison.' His eyes welled up…",
            "'I think it was Lady Miaoyin who really killed Master Shen. Please… Qingyin Pavilion bring justice to Tianquan Manor!' The old butler drops to his knees, but you rush forward and catch him just in time.",
            "You frown slightly, eyes fixed on him: 'If you’ve known this all along… why didn’t you speak up earlier?'",
            "'Lady Miaoyin’s good with poison… I was afraid she might get rid of me.' the butler said,",
            "'I wasn’t sure you were capable, with you being so young. So I left the bottle there on purpose… to test you.' the old butler looked increasingly ashamed.",
            "'Got it.' You nodded and took the bottle."
        ]
    },



    #Lan Yi's memory
     "lanyi_confess_poison_truth": {
        "zh": [
            "“事已至此，我没什么好隐瞒的了，是我……是我害死了爹。”",
            "“我和林修两情相悦，父亲却逼我和昆山派的聂清昭定亲，我十分不愿，和他大吵了一架。”",
            "“父亲后来把我关了一个月的禁闭。”她苦笑道",
            "“再之后我假意顺从，才被放了出来。上个月偶然偷听到父亲和妙音姑姑商量",
            "“二十年之约已到，父亲有意假死避战。”",
            "“我便和林修商量，想趁机私奔。父亲武艺高强，我不知妙音姑姑的假死药能让父亲‘假死’多久”",
            "“万一父亲很快醒来，发现我和林修私奔，肯定会吧我俩抓回来的”",
            "“于是我就去偷了妙音姑姑的毒药，我想着他中了假死药，身子虚，再灌下点毒……妙音姑姑解毒也需要时间。”",
            "她回忆道：“我动手之时，十分慌乱，毒粉都散了出来，没有全给爹服下，反而大部分抖在了我的衣服上。”",
            "“我以为……我以为这样做我就能和林修永远离开天泉山庄。”",
            "“私奔那晚，林修来迟了，我还埋怨他怎么磨蹭。”",
            "“到了山门外，他解释说他心里不踏实，也……也喂了一瓶毒药给我爹。”",
            "“我们俩谁也没跟谁说……是走在山门外才对上口风的。我吓坏了！”",
            "“三种毒下在一人身上，林修还把瓶子扔了……我怕真的……真的出事。”",
            "“我求他回去，跪着求的。他不愿意，说此刻怕是已经出事了，回去就是自投罗网。我拿自己性命要挟，他才答应”",
            "“可我们赶回去时，爹已经……已经没气了。妙音姑姑也没能把他救回来……我……我真不配活着……”"
        ],
        "en": [
            "'Now that things have come to this, I have nothing to hide... it was I who killed father.'",
            "'Lin Xiu and I were in love, but father forced me to get engaged to Nie Qingzhao of Kunshan Sect. I strongly refused and had a big argument with him.'",
            "'Father then confined me for a month,' she said with a bitter smile.",
            "'After that, I pretended to comply and was released. Last month, I accidentally overheard Father and Aunt Miaoyin discussing that the twenty-year agreement had arrived, and Father intended to fake his death to avoid conflict.'",
            "'So I discussed with Lin Xiu, hoping to take the opportunity to elope. Father is highly skilled in martial arts, and I didn't know how long Aunt Miaoyin's fake death potion would keep him 'fake dead'.'",
            "'If Father woke up in a short time and found Lin Xiu and me eloping, he would definitely catch us back.'",
            "'So I stole Aunt Miaoyin's poison. I thought that since he was weakened by the fake death potion, adding more poison... Aunt Miaoyin, as an expert, would also need more time to detoxify him.'",
            "She recalled, 'When I acted, I was in a great panic, and the poison powder spilled out, not all of it given to Father, but most of it fell on my clothes.'",
            "'I thought... I thought this way Lin Xiu and I could leave Tianquan Manor forever.'",
            "'That night we eloped, Lin Xiu was late, and I was complained about his dawdling.'",
            "'After we left the mountain gate, he explained that he felt uneasy, and he... he also fed a bottle of poison to my father.'",
            "'We hadn't discussed it with each other before... we only talked about it when we were outside the mountain gate. I was terrified!'",
            "'Three kinds of poison on one person, and Lin Xiu even threw away the bottle... I was afraid something... something really bad would happen.'",
            "'I begged him to go back, he refused, saying that something must have happened already, and going back would be walking into a trap. I threatened him with my own life before he agree to go back.'",
            "'But when we rushed back, Father was already... already gone. Even aunt Miaoyin couldn't save him... I... I really don't deserve to be alive...'"
        ]
    },
    "lanyi_love_story_past": {
        "zh": [
            "“我和林修……是从小一起长大的。”",
            "“他沉默寡言，却很照顾我。小时候我摔伤了腿，血流了一地”",
            "“是他小小年纪把我从山门一步一步背回来的，在路上他整个身体都在抖，”",
            "“我让他放我下来，我说我俩可以扶着一起走，他却不肯。”",
            "“后来我练剑偷懒，他也总在我爹面前替我遮掩。”",
            "“我以为……我俩会开心的一起长大。”她苦笑道",
            "“直到有一次，我见他一个人，在后院跪了一整夜。",
            "“我问他怎么了，他不肯说。后来我才知道，他的父母，死于一场二十年前的一场瘟疫。",
            "“那时江湖上流传唯有天泉山庄后山冷泉边生长的黄花蒿可以解这疫症，",
            "“黄花蒿乃是自然生成，本就不多，爹为了救人，把后山都快挖空了，”",
            "“尽管如此，还是不断有江湖人士前来上门求药，林修的父母便是其中之一。",
            "“后来舅舅和外祖母都染上了疫症……",
            "“后山的黄花蒿早已被挖的没有了，父亲便下令把最后一株库房留存的黄花蒿送去了外祖家。",
            "“舅舅救回来了，但是外祖母也因此病故……而林修的父母，更是不治身亡。",
            "“林修……林修便是那林家遗孤。”",
            "“天泉山庄不想杀人，却……也没救他们。林修曾说过‘若是那年能有一节黄花蒿，或许我娘还活着。”",
            "“我很怕他恨爹。可他从没说过一句埋怨，只是越来越沉默寡言。”",
            "“直到后来有一天，他突然跟我说，他很喜欢我，从小就喜欢。”"
        ],
        "en": [
            "'Lin Xiu and I... we grew up together since childhood.'",
            "'He was quiet, but always took good care of me. Once, when I was little, I fell and injured my leg, bleeding all over.'",
            "'He, though so young, carried me back step by step from the mountain gate. His whole body was trembling on the way.'",
            "'I told him to put me down, that we could walk together, supporting each other, but he refused.'",
            "'Later, when I was lazy in sword practice, he would always cover for me in front of my father.'",
            "'I thought... we would grow up happily together,' she said with a bitter smile.",
            "'Until one time, I saw him alone, kneeling in the backyard all night.'",
            "'I asked him what was wrong, but he wouldn't say. Later, I found out that his parents died in a epidemic twenty years ago.'",
            "'At that time, it was said that only sweet wormwood plant growing by the cold spring in the back hills of Tianquan Manor could cure the epidemic.'",
            "'The sweet wormwood grows naturally and is not abundant. Father, to save people, almost dug up the entire back mountain.'",
            "'Despite this, people kept coming to seek medicine, including Lin Xiu's parents.'",
            "'Later, my uncle and grandmother both contracted the epidemic...'",
            "'The sweet wormwood behind the mountain was already depleted, father sent the last sweet wormwood to my grandmother's side.'",
            "'My uncle was saved, but my grandmother passed away because of it... and Lin Xiu's parents died without being cured.'",
            "'Lin Xiu... Lin Xiu is that orphaned child from the Lin family.'",
            "'Tianquan Manor did not want to kill anyone, but... didn't save them either. Lin Xiu said once 'If there has been a piece of sweet wormwood that year, perhaps my mother would still be alive.'",
            "'I was afraid he hated Father. But he never said a word of complaint, only becoming more silent.'",
            "'Until one day, he suddenly told me that he liked me very much and had liked me since he was a child.'"
        ]
    },


    #Lin Xiu's long memory
    "lin_memory_early": {
        "zh": [
            "林修声音有些颤抖：“我父母就葬在天泉山庄外的义庄，”",
            "“当年他们因为瘟疫来天泉山庄求药，沈庄主却没有赐药救人。”",
            "“我少年时期无意得知此事，心有愤懑，然我也知瘟疫乃是天灾，与天泉山庄无关。”",
            "“况且是沈庄主收留了我，若他没收留我，我怕是早已饿死街头。”",
            "“若没有他悉心教导，我又何来今日身手？”",
            "“我唤他庄主，其实他也是我的‘师父’。有时候想起已逝的父母，我会偷偷祭祀，聊表哀思。”",
            "“无论如何，我那么爱澜衣，我不能让她难过...”",
            "他不再理会你，仿佛陷入了沉思。"
            ],
        "en": [
            "Lin Xiu trembles slightly: 'My parents were buried in the pauper's graveyard outside Tianquan Manor.'",
            "'They came here seeking medicine during the epidemic, but Master Shen refused to help.'",
            "'I discovered this by accident in my youth and I was angry-but I also knew the epidemic was a natural disaster.'",
            "'And Master Shen saved my life. If he hadn’t takeme in Tianquan Manor, I’d have died starving on the streets.'",
            "'If not for his guidance, how would I have the martial arts skills I have today?'",
            "'I call him Master Shen, but he’s actually my teacher and foster father. Sometimes when I think of my deceased parents,  I burn incense to express my condolences...'",
            "'No matter what, I love Lanyi so much... I can't let her be sad...'",
            "He stops the conversation, seemingly lost in thought."
        ]
    },

    "lin_confess_poison": {
        "zh": [
            "“林修看着你，忽然笑了：“特使果然又来找我了。”",
            "“不错，我确实给沈庄主下了毒。”",
            "“那日澜衣来找我，商量与我私奔。”",
            "“她说沈庄主和妙音仙子商量，准备假死隐退。”",
            "“我本来不信，后来沈庄主将山庄库房钥匙全给了澜衣。”",
            "“我想，沈庄主大概真的在计划一些事情，澜衣说的可能是真的。”",
            "“我担心澜衣打听到的情报日期时间不准确，万一沈庄主只是日常修炼...”",
            "“那我们俩肯定会被抓回来，我怕小命不保。”",
            "“为了稳妥起见，我事先偷了一瓶妙音仙子的毒药藏着。”",
            "“那晚出发前，我看见澜衣从密室慌张跑了出去，我便也悄悄地溜了进去”",
            "“我见沈庄主确实昏迷着，便直接喂了他我偷的那瓶毒药。”",
            "“我并不怕他中毒，反正妙音仙子能解。”",
            "“完成后我把毒瓶随手扔在了管家的门口。”",
            "“这就是全部事情的真相。”"
        ],
        "en": [
            "Lin Xiu looks at you and smiles faintly: 'So you've come again, emissary.'",
            "'Yes, I did poison Master Shen.'",
            "'That day, Lanyi came to me and said she wanted to elope.'",
            "'She told me Master Shen planned to fake his death and retire soon, with Lady Miaoyin's help.'",
            "'I didn’t believe it at first, but when Master Shen gave Lanyi all these vault keys, I knew it might be true.'",
            "'However, I still feared if Lanyi got the inaccurate date and time. If Master Shen was just meditating and we got caught... I’d be executed.'",
            "'So I stole a vial of poison from Lady Miaoyin, just in case.'",
            "'Before we left, I saw Lanyi run out of the chamber in panic. I sneak in later on...' ",
            "'Seeing Master Shen was indeed unconscious, I fed him the bottle of poison I stole...'",
            "'I wasn’t too worried, Lady Miaoyin, as an expert, could cure him anyway.'",
            "'Then I tossed the vial randomly near the butler's room.'",
            "'That’s it.'"
        ]
    },

    "lin_deny_poison": {
        "zh": [
            "“林修看着你，眼神十分镇定：“特使还是去别处吧，莫要在我这白费功夫了。”",
            "“沈庄主收留了儿时的我，我才有了活命的机会，我无心害他。”",
            "“况且我爱上了澜衣，余生我也只想守着她，让她开心快乐。”"
        ],
        "en": [
            "Lin Xiu looks at you calmly: 'You’d best search somewhere else, emissary. Don’t waste your time on me.'",
            "'Master Shen took me in when I was a child that I had a chance to survive. I had no intention of harming him.'",
            "'Besides, I love Lanyi, and I just want to stay with her and make her happy for the rest of my life.'"
        ]
    },

    # --- Chen Qiman Multiline Dialogue ---
    "chen_feud_resolved_dialogue": { 
        "zh": [
            "陈奇曼沉默良久：“二十年了，我虽然难过，但过往种种，我儿也算是自食其果，天泉沈庄主又何尝不自责？”",
            "“我是来了结仇怨，不是来索命。”"
        ],
        "en": [
            "Chen Qiman stood in silence for a long while before speaking. \n 'Twenty years have passed. Though sorrow remains, I have come to accept the past. \n My son’s fate was of his own making... And Master Shen of Tianquan Manor — has he not borne the weight of remorse all these years?'",
            "'I am here to end this enmity, not to seek blood in return.'"
            ]
    },
    "chen_item_observation_dialogue": { 
        "zh": [
            "你闻到他茶壶中飘来一股微妙的香气，色泽却无异样。你瞥见他袖口，隐约露出两个颜色各异的小瓶。",
            "你冲他礼貌点头：“陈掌门的茶叶好香啊？您袖内是什么宝贝？不知再下可否一观？”",
            "陈奇曼愣了一下，随即笑着打开茶壶：“特使果然眼力敏锐，这是我华山派独门金疮药。”随后从袖子里拿出两个小瓶，瓶口都贴着‘华山派特制’的封条。”",
            "你接过瓶子，打开其中一瓶闻了闻，与那茶壶里味道一致：“原来是贵派的金疮药，陈掌门这是受伤了？那这另外一瓶，闻起来像是常见的解毒丸？”",
            "陈奇曼苦笑着点点头，：“前日指点徒弟混元掌，他功力不稳，打在山石上，山石滚落，我为了救他，被击到胸口，受了点小伤，不碍事。”",
            "“因是要出门，夫人不放心，非让我随身带着这些药。嘿，都是些小伤，防患于未然罢了。”陈奇曼补充到。",
            "你心中有些怀疑，暗想陈奇曼身上的伤，到底是为了保护徒弟，还是沈庄主临终时所伤。但你并未在他身上发现任何毒药痕迹。",
            "你：“多谢陈掌门，您好好养伤，保重身体。”"
        ],
        "en": [
            "You catch a faint fragrance from his teapot, but nothing unusual about the color. Glancing at his sleeve, you spot two small bottles of different colors.",
            "You nod politely, 'Master Chen, your tea smells wonderful. What’s in your sleeve? May I take a look?'",
            "Chen Qiman pauses, then opens the teapot with a smile. 'Sharp eyes, Special Envoy. This is HuaShan Sect’s secret medicine for severe wounds.'\n He pulls out two small bottles, each labeled ‘HuaShan Sect Special Formula.’'",
            "You take one, sniff it-it matches the tea’s scent. 'Ah, HusShan Sect’s wound medicine. Master Chen, are you injured? And this one...smells like an antidote?'",
            "Chen Qiman nods with a wry smile. 'A few days ago, while demonstrating the HunYuan Palm, my disciple lost control and hit a rock.\n I was struck in the chest while saving him, just a small injury.'",
            "Since I’m traveling, my wife insisted I carry these,just a precaution.' he adds with a smile.",
            "You feel a bit suspicious of Chen Qiman, wondering whether his injuries really came from saving his disciple, or if they were caused by Master Shen before his death. \n But you don’t find any traces of poison on him.",
            "You: 'Thank you, Master Chen. Please take care and rest well.'"
        ]
    },
    "chen_direct_accusation_dialogue": { 
        "zh": [
            "他隐隐有些怒意：“我纵有恨意，也是二十年前...",
            "“此次是来解怨，并非寻仇，不然我为何还邀请静慧师太前来见证...",
            "他昂起下巴“况且我陈奇曼从不屑暗箭伤人！”"
        ],
        "en": [
            "A trace of anger flickered in his eyes. 'Even if resentment lingers in my heart, it dates back twenty years...'",
            "'I have come to settle grievances, not to pursue vengeance. \n If not, why would I have invited Abbess Jinghui to witness this meeting?'",
            "Lifting his chin with pride, he declared, 'Know this — I, Chen Qiman, have never stooped to strike from the shadows!'"
            ]
    },

    # --- Jinghui Multiline Dialogue ---
    "jing_reason_late_dialogue": { 
        "zh": [
            "静慧师太无奈道：“近日玉泉院附近来了一些灾民，说是豫州大旱，且起了蝗灾”",
            "“玉泉院一直忙于安排他们住宿和释粥。”",
            "“三天前有弟子发现其中有人得了伤寒，玉泉院上下一直忙于备药分发。”",
            "“院中事物繁复，灾民众多，故而来迟了。”"
        ],
        "en": [
            "Abbess Jinghui sighed softly: 'Lately, some refugees have arrived near Jade Spring Monastery, saying that Yuzhou has suffered from a great drought — and now, a locust plague.'",
            "'The monastery has been occupied with finding them shelter and offering porridge to the hungry.'",
            "'Three days ago, a disciple discovered that some had fallen ill with typhoid. Since then, we have been preparing and distributing medicine day and night.'",
            "'With so many hardships and people in need, the temple has been overwhelmed. That is why I arrived late.'"
]
    },
    "jing_disciple_testimony": { 
        "zh": [
            "静慧师太此次前来，还带了一个小徒弟。",
            "小徒弟脸蛋圆圆的，一双眼睛滴溜溜的转，看起来有点活泼。",
            "静慧师太回头问道：“妙真，凶案发生当天你可曾留意到有何异常么？”",
            "“是的，掌门，那天后半夜，弟子听见外面有一对男女在争执，好像说什么迟到之类的。”",
            "“因是半夜，声音格外清楚，持续时间不长，之后应该就离开了。”",
            "“后来第二天传出沈庄主过世的消息，我随师父进入主院。”",
            "“见到了沈小姐，那声音是沈小姐的。”",
            "你选择相信静慧师和妙真师父。你对他们表示感谢，你怀疑沈小姐有一些秘密。"
        ],
        "en": [
            "Abbess Jinghui arrived this time with a young disciple in tow.",
            "The young girl had a round face and bright, curious eyes that darted about — she looked rather lively.",
            "Abbess Jinghui turned and asked gently: 'Miaozhen, did you notice anything unusual on the night of the incident?'",
            "'Yes, Master. In the latter part of the night, I heard a man and a woman arguing outside. It sounded like they were quarreling about someone being late.'",
            "'Because it was so late, their voices were especially clear. The argument didn’t last long — they left shortly after.'",
            "'The next day, we heard that Master Shen had passed away. I followed you into the main courtyard.'",
            "'There, I saw Miss Shen. That voice — it was hers.'",
            "You choose to trust Abbess Jinghui and her disciple, Miaozhen. You thank them, though a quiet suspicion begins to grow: Miss Shen may be hiding something."
]
    },
    "jing_no_abnormalities_dialogue": { 
        "zh": [
            "静慧师太无奈道：“我傍晚方至，管家本安排我住进内院。”",
            "“但我生性喜静，我看外院有间禅房，便请管家安排我住在这里了。”",
            "“我一直打坐到深夜，外面的事务，我没有注意。”",
            "你对静慧师太表示感谢，但她一问三不知，反而让你觉得有点可疑。"
        ],
        "en": [
            "Abbess Jinghui sighed softly, 'I only arrived at dusk. The bulter had arranged for me to stay in the inner courtyard.'",
            "'But I cherish tranquility. Seeing a meditation room in the outer courtyard, I asked to be lodged there instead.'",
            "'I sat in meditation well into the deep night and paid little heed to matters beyond.'",
            "You express your thanks to Abbess Jinghui, yet her ignorance on the matter only deepens your suspicion."
            ]
        },

       

    # --- Miaoyin Multiline Dialogue ---
    "miaoyin_hidden_relationship_story": {
        "zh": [
            "“你知道，当年他怎么说的吗？”",
            "“他说——师徒有别，不容越矩。他还闭关三月，罚我抄写清心咒一百遍。”",
            "“我一气之下，趁他闭关，留下书信偷跑去了南疆，拜入五毒教。”",
            "“多年后，我被崆峒派小人暗算，中毒濒死，是他救了我。”",
            "“彼时沈夫人病亡，我也与他多年未见，他早已不识得我的模样，以为只是救了个陌生人。”",
            "“我唤了他一声‘师父’，他才认出我。”",
            "“后来他说：‘若有一日，了结了这些江湖恩怨，如果你还想要我，那我，便归你了。’”",
            "“这次假死，便是他兑现承诺的方式。”",
            "“可惜……他真的死了。”"
        ],
        "en": [
            "'Do you know what he said back then?'",
            "'He said—'Master and disciple have their boundaries, not to be overstepped.' He even went into seclusion for three months and punished me by making me copy the Heart-Purifying Mantra a hundred times.'",
            "'In a fit of anger, while he was in seclusion, I left a letter and secretly ran off to Southern疆, joining the Five Venoms Sect.'",
            "'Years later, I was ambushed by a villain from the Kongtong Sect and nearly died from poison. He was the one who saved me.'",
            "'At that time, Madam Shen had passed away, and I hadn't seen him for many years. He no longer recognized me, thinking he had just saved a stranger.'",
            "'Only when I called him 'Master' did he recognize me.'",
            "'Later he said: 'If one day, these martial world grievances are settled, and if you still want me, then I shall be yours.''",
            "'This fake death was his way of fulfilling that promise.'",
            "'Alas... he truly died.'"
            ]
        },
        "miaoyin_observe_bottles_response":{
            "zh":["妙音仙子主动拿出一个盒子，里面足有七八枚药瓶，分为红绿两种标签，大约是五毒教所传。",
                  "她向你介绍：“我五毒教的药瓶都有特殊印记，事后我才查到，我的毒药丢了几瓶。”",
                  "你询问她：“沈庄主难道是被你丢失的毒药所害？”",
                  "妙音仙子神情落寞：“不错。”",
                  "你一边观察她的神色，一边问她：“五毒教皆为用毒高手，自然配有解药，仙子竟然没能及时施救?”",
                  "妙音仙子眼中含泪：“是我学艺不经，毒药混在一起，我竟然没能及时诊出到底是哪几种毒。”",
                  "你十分惊讶：“所以除了假死药，沈庄主竟然还中了几种毒吗？”",
                  "妙音仙子声泪俱下：“不错，除了假死药，我当时发现他还中了其他两种毒，便即刻为他解毒。但我竟不知他体内竟还存有其他毒药，若我能及时发现，他也不至于...”\n妙音仙子啼不成声，你仔细看了她一眼，那痛苦又不似作假。"
                  ],
            "en":["Lady Miaoyin proactively brought out a box containing seven or eight medicine bottles, labeled red and green, likely from the Five Venoms Sect.",
                  "She explained to you: 'My Five Venoms Sect's medicine bottles have special markings. Afterwards, I discovered that several bottles of my poison were missing.'",
                  "You asked her: 'Was Master Shen perhaps harmed by your missing poison?'",
                  "Lady Miaoyin's expression was despondent: 'Indeed.'",
                  "While observing her expression, you asked her: 'The Five Venoms Sect are all masters of poison, surely equipped with antidotes. How is it that you, Lady Miaoyin, couldn't administer timely aid?'",
                  "Tears welled in Lady Miaoyin's eyes: 'It is my lack of skill; the poisons were mixed, and I couldn't promptly diagnose which types of poisons they were.'",
                  "You were greatly surprised: 'So besides the fake death potion, Master Shen was actually poisoned with several other types of poisons?'",
                  "Lady Miaoyin wept: 'Indeed, besides the fake death potion, I discovered he was also afflicted by two other poisons, \n and I immediately administered antidotes. But I didn't realize there were still other poisons in his body; '",
                  "'if I had discovered them in time, he wouldn't have...' Lady Miaoyin's voice broke. \n You looked closely at her; her pain seemed genuine."
                  ]
        },
         


        "miaoyin_secret_room_response": {
            "zh": ["她目光闪躲：“那密室钥匙有几把，我，管家和沈姑娘都有钥匙。”",
                   "紧接着她拿出两个药瓶：“我发现沈庄主中了毒，其中两种毒药的空瓶就摆在密室桌上，我立刻为他解毒，\n 没想到他身体里还有其他毒药，终究没能救的了他。毒药瓶子就是这两个。”",
                   "你十分惊讶：“沈庄主竟中了这么多毒？那剩下的毒药空瓶找到了么？”",
                   "妙音仙子眼中含泪：“没有找到，此事还得有劳特使尊驾了。”"
                   ],
            "en": ["Her gaze darted: 'There are several keys to the secret chamber; I, the butler, and Miss Shen all have keys.'",
                   "Immediately she produced two medicine bottles: 'I found Master Shen poisoned. \n Two empty bottles of poison were on the chamber table. \n I immediately tried to detoxify him, but I didn't expect there to be other poisons in his body. \n In the end, I couldn't save him. These are the two poison bottles.'",
                   "You were greatly surprised: 'Master Shen was afflicted by so many poisons? \n Were the remaining empty poison bottles found?'",
                   "Tears welled in Lady Miaoyin's eyes: \n 'They weren't found. This matter will require your esteemed assistance, Envoy.'"
                   ]
        },

        "miaoyin_powder_scent_reveal": {
            "zh": ["妙音仙子：“等一下，其实这空毒药瓶子上似乎有淡淡的水粉香味。”",
                   "你拿过瓶子轻轻嗅了一下，确实如此。：“山庄内近日女子出入不多，除了您和静慧师太...仙子莫非是在暗示沈小姐碰过这毒药瓶？”",
                   "妙音仙子：“也许是不小心沾上了也未可知。”",
                   "你：“多谢仙子。”"
                   ],
            "en": ["Lady Miaoyin: 'Wait, actually, there seems to be a faint scent of face powder on these empty poison bottles.'",
                   "You took the bottle and gently sniffed it; indeed, it was true. 'Not many women have entered or exited the manor recently, besides yourself and Abbess Jinghui...'",
                   "'Lady Miaoyin, are you implying Miss Shen touched this poison bottle?'",
                   "Lady Miaoyin: 'Perhaps it was accidentally transferred, who can say?'",
                   "You: 'Thank you, Lady Miaoyin.'"
                   ]
        }
  
    



}




# 工具函数

"""
def say(key, lang="en"):
    #打印对应语言的对话内容
    #:param key: 对话关键词
    #:param lang: 'zh' 或 'en'  
    if key in dialogue_lanyi and lang in dialogue_lanyi[key]:
        print("\n" + dialogue_lanyi[key][lang])
    else:
        print("[对话缺失 / Missing dialogue]")
"""

# --- Tool Functions --- #

def say(key, lang="en"):
    #print()
    return DIALOGUES.get(key, {}).get(lang, f"[Missing: {key}]")

def say_multiline(key, lang="en"):
    #print()
    lines = MULTILINE_DIALOGUES.get(key, {}).get(lang, [])
    for line in lines:
        print(line)
    #print()

def split_clues(dialogue_key: str, lang: str) -> str:
    """
    Extracts a clue from a dialogue string that follows a specific "Clue acquired:" or "你获得了线索：" pattern.
    This function is designed for dialogue entries like 'lin_obs_result' where the clue is embedded in the text.

    Args:
        dialogue_key (str): The key for the dialogue entry in the DIALOGUES dictionary
                            (e.g., "lin_obs_result").
        lang (str): The language ('zh' or 'en') to retrieve the dialogue in.

    Returns:
        str: The extracted clue string, or an empty string if no clue is found or extracted.
    """
    dialogue_string = say(dialogue_key, lang)
    
    # Define prefixes for clue extraction
    clue_prefix_zh = "你获得了线索："
    clue_prefix_en = "Clue acquired: "

    clue_text = ""
    if lang == "zh" and clue_prefix_zh in dialogue_string:
        # Split by the Chinese prefix and take the last part
        clue_text = dialogue_string.split(clue_prefix_zh, 1)[-1].strip()
    elif lang == "en" and clue_prefix_en in dialogue_string:
        # Split by the English prefix and take the last part
        clue_text = dialogue_string.split(clue_prefix_en, 1)[-1].strip()
    else:
        # Fallback: if the specific prefix isn't found, try splitting by either colon type.
        # This covers cases where the format might vary or be simpler.
        # Note: This fallback might be too broad if other parts of dialogue also contain colons.
        # Consider if you only want to extract clues from explicitly formatted lines.
        parts = re.split(r'[:：]', dialogue_string)
        if len(parts) > 1: # Ensure there was at least one split
            clue_text = parts[-1].strip()
        
    return clue_text