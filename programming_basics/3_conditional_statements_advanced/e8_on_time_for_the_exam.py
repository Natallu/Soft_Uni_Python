exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_minutes = exam_hour * 60 + exam_minute
arrival_time_minutes = arrival_hour * 60 + arrival_minute
early = exam_time_minutes - arrival_time_minutes
late = arrival_time_minutes - exam_time_minutes


if arrival_time_minutes == exam_time_minutes:
    print('On time')
elif arrival_time_minutes < exam_time_minutes:
    if early <= 30:
        print('On time')
        print(f"{early} minutes before the start")
    elif early > 30:
        print('Early')
        if 30 < early < 60:
            print(f"{early} minutes before the start")
        elif early >= 60:
            early_hours = early // 60
            early_minutes = early % 60
            if early_minutes < 10:
                print(f'{early_hours}:0{early_minutes} hours before the start')
            else:
                print(f'{early_hours}:{early_minutes} hours before the start')
elif arrival_time_minutes > exam_time_minutes:
    print("Late")
    if late < 60:
        print(f'{late} minutes after the start')
    elif late >= 60:
        late_hours = late // 60
        late_minutes = late % 60
        if late_minutes < 10:
            print(f"{late_hours}:0{late_minutes} hours after the start")
        else:
            print(f"{late_hours}:{late_minutes} hours after the start")
