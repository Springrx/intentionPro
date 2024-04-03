from prompts import baseline_multi_task_prompt, cot_multi_task_prompt, one_shot_multi_task_prompt
from cmd import origin_user_cmds
from ask_gpt4v import ask_gpt4v
def solve_multi_task(task_desc: str, prompt: str):
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
res=[]
for task_desc in origin_user_cmds:
    refined_cmd=solve_multi_task(task_desc,baseline_multi_task_prompt)
    refined_cmd = refined_cmd.replace("<task>[", "").replace("]<t_end>", "").split(",")
    print(f"Original command: {task_desc}",f"Refined command: {refined_cmd}",sep='\n')
    res.append(refined_cmd)
print(res)