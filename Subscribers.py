# how long will it take to reach certain subscribers

import datetime
import math

goal_subs = 100000
current_sub = 40000
subs_to_go = goal_subs - current_sub

avg_sub_day = 200

days_to_go = math.ceil(subs_to_go / avg_sub_day)

today = datetime.date.today()
print(today + datetime.timedelta(days=days_to_go))