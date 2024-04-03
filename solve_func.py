from user_cmds import loca_or_collo_exp, refined_loca_or_collo_exp, ambiguity_exp, ambiguity_answers, ambiguity_questions
from utils.ask_gpt4v import ask_gpt4v
from prompts import spoken_zero_shot_prompt, spoken_one_shot_prompt, spoken_two_shot_prompt, clarification_two_shot_prompt, choose_app_prompt, clarification_one_shot_prompt,clarification_zero_shot_prompt,integrate_cmd_prompt
import re
import json

def solve_local_collo_exp(task_desc: str,prompt:str):
    # 选择app
    # 将str中的<user_command>替换为task_desc
    prompt = prompt.replace("<user_command>", task_desc)
    rsp = ask_gpt4v(prompt)
    if "error" not in rsp:
        refined_cmd = rsp["choices"][0]["message"]["content"]
        return refined_cmd
    else:
        print("Error occurred while retrieving app information.")
        return ''

def solve_ambiguity_or_two_interpretations(task_desc: str, prompt: str):
    # 生成follow-up questions
    # 将str中的<user_command>替换为task_desc
    prompt = prompt.replace("<user_command>", task_desc)
    rsp = ask_gpt4v(prompt)
    if "error" not in rsp:
        questions = rsp["choices"][0]["message"]["content"]
        return questions
    else:
        print("Error occurred while generating follow-up questions.")
        return ''

def integrate_cmd(origin_command: str,questions_list:list,answers_list:list, prompt: str):
    # 生成follow-up questions
    # 将str中的<user_command>替换为task_desc
    prompt = prompt.replace("<origin_command>", origin_command).replace("<questions_list>", str(questions_list)).replace("<answers_list>", str(answers_list))
    rsp = ask_gpt4v(prompt)
    if "error" not in rsp:
        refined_cmd = rsp["choices"][0]["message"]["content"]
        return refined_cmd
    else:
        print("Error occurred while generating follow-up questions.")
        return ''
 
new_cmd=[]
origin_command= ["我最近去上海，帮我订个票","那个，帮我看一下账户余额"]
questions_list=[    ["您是想订机票还是火车票？", "您想订哪一天的票？"],
    ["您是想查看哪个账户的余额？是银行账户还是支付宝账户？"],]
answers_list=[    ["机票", "下周三"],
      ["支付宝"],]
for origin_command,questions_list,answers_list in zip(ambiguity_exp,ambiguity_questions,ambiguity_answers):
    refined_cmd=integrate_cmd(origin_command,questions_list,answers_list,integrate_cmd_prompt)
    new_cmd.append(refined_cmd)
print(new_cmd)
# exp='帮我下载一个适合老同志的软件'
# questions_list=['您是想下载一个适合老年人使用的软件吗，还是想下载一个适合同性恋者使用的软件？', '请问您具体想要哪一类的软件？比如健康管理，娱乐，还是社交？']
# answers_list=["适合老年人的软件", "健康管理"]
# refined_cmd=integrate_cmd(exp,questions_list,answers_list,integrate_cmd_prompt)
# print(f"Original command: {exp}",f"Refined command: {refined_cmd}",sep='\n')