
start, duration =("3:30 PM", "2:12")
start, duration =("11:55 AM", "3:12")
start, duration =("9:15 PM", "5:30")
start, duration =("11:40 AM", "0:25")
start, duration =("2:59 AM", "24:00")
start, duration =("11:59 PM", "24:05")
start, duration =("8:16 PM", "466:02")
start, duration =("5:01 AM", "0:00")
start, duration, day =("3:30 PM", "2:12", "Monday")
start, duration, day=("2:59 AM", "24:00", "saturDay")
start, duration, day =("11:59 PM", "24:05", "Wednesday")
start, duration, day =("8:16 PM", "466:02", "tuesday")



def add_time(start, duration, day=None):
    day_week = {

        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    # change time from hh:mm to mm
    def to_minute (time):
        try:
            if time.split(":")[1].split(" ")[1] == "PM":
                time_h = int(time.split(":")[0])+12
            else:
                time_h = int(time.split(":")[0])
        except IndexError:
            time_h = int(time.split(":")[0])

        return int(time.split(":")[1].split(" ")[0]) + time_h * 60

    def get_key(val):
        for key, value in day_week.items():
            if val == value:
                return key

    new_time_full = (to_minute(start) + to_minute(duration))
    # changes minutes to hh:mm AM/PM
    # american hour system
    new_time_h = new_time_full // 60
    i = 0
    if new_time_h % 12 == 0:
        i += 1
    while new_time_h > 12:
        new_time_h -= 12
        i += 1
    new_time_m = (new_time_full % 60) if new_time_full % 60 >= 10 else str(0) + str(new_time_full % 60)
    # AM/PM check
    if i%2:
        meridiem = "PM"
    else:
        meridiem = "AM"

    # prints how many days later we are
    if day is None:
        days_later = new_time_full // 60 // 24
        if days_later == 0: days_later = ""
        elif days_later == 1: days_later = " (next day)"
        elif days_later > 1: days_later = " ({} days later)".format(days_later)
        else: days_later = ""
        new_time = "{}:{} {}{}".format(new_time_h, new_time_m, meridiem,  days_later)
    else:
        day = day_week[day.capitalize()]
        new_day = new_time_full // 60 // 24 + day
        days_later = (new_day - day)
        if days_later == 0: days_later = ""
        elif days_later == 1: days_later = " (next day)"
        elif days_later > 1: days_later = " ({} days later)".format(days_later)
        else: days_later = ""
        if day is None:
            new_day = ""
        else:
            new_day = " "+str(get_key(new_day%7 if new_day%7 else new_day))


        new_time = "{}:{} {},{}{}".format(new_time_h, new_time_m, meridiem, new_day, days_later)

    return new_time

print(add_time(start, duration,day))