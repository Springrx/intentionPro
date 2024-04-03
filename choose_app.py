from apps import apps
from utils.ask_gpt4v import ask_gpt4v
from prompts import choose_app_prompt
import re
import json
from user_cmds import origin_user_cmds,one_shot_refined_user_cmds, loca_or_collo_exp, refined_loca_or_collo_exp, ambiguity_exp, integrated_exp

def choose_app(task_desc: str):
    # 选择app
    str_apps = str(apps)
    # 将str中的<app_list>替换为apps
    choose_app_cmd=choose_app_prompt.replace("<app_list>", str_apps).replace("<user_command>", task_desc)
   
    rsp = ask_gpt4v(choose_app_cmd)
    if "error" not in rsp:
        app = rsp["choices"][0]["message"]["content"]
        match = re.search(r"<task_and_app>(.*?)<end>", app)
        # 将match转换为数组格式
        if match:
            # 如果match的长度为1，则返回match[0]
            app_info = match.group(1)
            # 将单引号替换为双引号以符合JSON格式
            json_str = app_info.replace("'", '"')
        
            app = json.loads(json_str)
           
            return app
        else:
            print("No app information found.")
            return {}
    else:
        print("Error occurred while retrieving app information.")
        return {}

# 测试
ans=[]
for exp in one_shot_refined_user_cmds:
    for task_desc in exp:
        app_and_task = choose_app(task_desc)
        ans.append(app_and_task)
        print(f"Original command: {task_desc}", f"Refined command: {app_and_task}", sep='\n')
print(ans)
