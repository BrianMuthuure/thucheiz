import datetime

current_weight = 220   # in pounds
goal_weight = 180
avg_lbs_week = 2.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(end_date)
print(f'Reached goal in {(end_date - start_date).days // 7} weeks')