from user_cmds import ambiguity_exp
from prompts import choose_app_prompt
import os
a="<task>['查看明天闸北公园的路线','查看明天闸北公园的天气']<t_end>"
a = a.strip("<task>").strip("<t_end>").split(",")
print(a)