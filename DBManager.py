import json
import os.path

# PRZYKLADOWY SCHEMAT DB
# informacje o dacie dnia dzisiejszego oraz nazwie tego dnia (pon, wt) będzie trzeba podawać przy inicjalizacji klasy
# może być od użytkownika z konsoli lub od systemu
# {
#     "06.06.2021": [
#         {
#             "date": "06.06.2021",
#             "time": "12:00-13:30",
#             "place": "Restauracja Alfa",
#             "participants": ["Jan Kowalski", "Adam Nowak"],
#             "description": None
#         },
#         {
#             "date": "06.06.2021",
#             "time": "18:00-18:45",
#             "place": "Stadion Miejski",
#             "participants": ["Jan Kowalski"],
#             "description": None
#         }
#     ],
#     "07.06.2021": [
#         {
#             "date": "07.06.2021",
#             "time": "9:00-10:30",
#             "place": "MS Teams",
#             "participants": ["Adam Nowak"],
#             "description": "Wykład z matematyki"
#         }
#     ]
# }



class calender_db:
    def __init__(self, date="07.06.2021", name="poniedziałek", start_day_time="8:00", end_day_time="20:00", file_path="data-base/calender.json"):
        self.DB = {}
        self.start_day_time = start_day_time
        self.end_day_time = end_day_time
        self.today_date = date
        self.today_day_name = name
        self.today_day, self.today_month, self.today_year = self.get_day_month_year(self.today_date)
        if os.path.isfile(file_path):
            with open(file_path, 'r+') as input:
                self.DB = json.load(input)

    def save_db(self):
        with open(file_path, 'w+') as output:
            self.DB = json.dumps(input)

    # CRUD methods

    def create_meeting(self, meeting_dict):
        date = meeting_dict['date'].lower()
        if date == "dziś":
            date = self.today_date
        elif is_date_day_name(date):
            offset = get_days_difference(date)
            date = calculate_date_with_offset(offset)
        #TODO chceck date format
        if date in self.DB.keys():
            self.DB[date].append(meeting_dict)
            self.save_db()
        else:
            self.DB[date] = [meeting_dict]
            self.save_db()

    def is_collision(self, date, time):
        # TODO zaimplementować oferowanie innego czasu w razie kolizji
        if date in self.DB.keys():
            meetings = DB[date]
            for m in meetings:
                meeting_time = m['time'].split("-")
                start = meeting_time[0]
                # meeting has start and end time
                if len(meeting_time > 1):
                    end = meeting_time[1]
                    seeking_hour, seeking_min = self.get_hour_minutes(time)
                    seeking_hour_s, seeking_min_s = self.get_hour_minutes(start)
                    seeking_hour_e, seeking_min_e = self.get_hour_minutes(end)
                    if seeking_hour < seeking_hour_s:
                        return False
                    if seeking_hour == seeking_hour_s and seeking_min < seeking_min_s:
                        return False
                    if seeking_hour == seeking_hour_e and seeking_min >= seeking_min_e:
                        return False
                    if seeking_hour > seeking_hour_e:
                        return False
                    return True
                # meeting has only start time
                else:
                    seeking_hour, seeking_min = self.get_hour_minutes(time)
                    seeking_hour_s, seeking_min_s = self.get_hour_minutes(start)
                    if seeking_hour == seeking_hour_s and seeking_min == seeking_min_s:
                        return True
                    else:
                        return False
        else:
            return False

    def is_collision(self, date, time_start, time_end):
        # TODO zaimplementować oferowanie innego czasu w razie kolizji
        if date in self.DB.keys():
            meetings = DB[date]
            for m in meetings:
                meeting_time = m['time'].split("-")
                start = meeting_time[0]
                # meeting has start and end time
                if len(meeting_time > 1):
                    end = meeting_time[1]
                    hour_s, min_s = self.get_hour_minutes(time_start)
                    hour_e, min_e = self.get_hour_minutes(time_end)
                    seeking_hour_s, seeking_min_s = self.get_hour_minutes(start)
                    seeking_hour_e, seeking_min_e = self.get_hour_minutes(end)
                    if hour_s < seeking_hour_s and hour_e < seeking_hour_s:
                        return False
                    if hour_s < seeking_hour_s and hour_e == seeking_hour_s and min_e <= seeking_min_s:
                        return False
                    if hour_s == seeking_hour_s and min_s < seeking_min_s and hour_e == seeking_hour_s and min_e <= seeking_min_s:
                        return False
                    if hour_s == seeking_hour_e and min_s >= seeking_min_e:
                        return False
                    if hour_s > seeking_hour_e:
                        return False
                    return True
                # meeting has only start time
                else:
                    seeking_hour, seeking_min = self.get_hour_minutes(time)
                    seeking_hour_s, seeking_min_s = self.get_hour_minutes(start)
                    if seeking_hour == seeking_hour_s and seeking_min == seeking_min_s:
                        return True
                    else:
                        return False
        else:
            return False

    def find_meeting(self, date, time):
        if date in self.DB.keys():
            meetings = DB[date]
            for m in meetings:
                if time == m['time']:
                    return m
            return None
        else:
            return None

    def get_meetings(self, date_list):
        meetings = []
        for date in date_list:
            if date in self.DB.keys():
                date_meetings = self.DB[date]
                for m in date_meetings:
                    meetings.append(m)
        return meetings

    def get_freetime(self, date_list):
        freetime_dict = {}
        for date in date_list:
            time_str = self.start_day_time + "-" + self.end_day_time
            freetime_dict[date] = [time_str]
            # Change free time if there are meetings at this day
            if date in self.DB.keys():
                for meeting in self.DB[date]:
                    meeting_time = meeting['time'].split("-")
                    start = meeting_time[0]
                    # meeting has start and end time
                    if len(meeting_time > 1):
                        end = meeting_time[1]
                        meet_start_h, meet_start_m = self.get_hour_minutes(start)
                        meet_end_h, meet_end_m = self.get_hour_minutes(end)
                        for slot in freetime_dict[date]:
                            slot_time = slot.split("-")
                            slot_start_h, slot_start_m = self.get_hour_minutes(slot_time[0])
                            slot_end_h, slot_end_m = self.get_hour_minutes(slot_time[1])
                            # if meeting time have collision with slot time - change / split slot

                            # meeting starts inside slot
                            if meet_start_h == slot_start_h and meet_start_m > slot_start_m and meet_start_h < slot_end_h:
                                pass
                            elif meet_start_h == slot_start_h and meet_start_m > slot_start_m and meet_start_h == slot_end_h and meet_start_m < slot_end_m:
                                pass
                            elif meet_start_h > slot_start_h and meet_start_h < slot_end_h:
                                pass
                            elif meet_start_h > slot_start_h and meet_start_h == slot_end_h and meet_start_m < slot_end_m:
                                pass

                            # starts before slot, ends inside slot
                            elif (meet_end_h > slot_start_h) or (meet_end_h == slot_start_h and meet_end_m > slot_start_h):
                                # meeting in whole slot - delete this slot
                                if meet_end_h == slot_end_h and meet_end_m == slot_end_m:
                                    pass
                                # cut slot from left side
                                else:
                                    pass
                            # if meeting starts and ends before slot start time - do nothing
                    # meeting has only start time
                    else:
                        m_start_h, m_start_m = self.get_hour_minutes(start)

    def update_meeting(self, date, time, new_meeting_dict):
        # TODO nie testowane
        if date in self.DB.keys():
            meetings = DB[date]
            to_update = next(m for m in meetings if m['time'] == time)
            if type(to_update) is dict:
                to_update = new_meeting_dict
                self.save_db()

    def delete_meeting(self, date, time):
        # TODO nie testowane
        if date in self.DB.keys():
            meetings = DB[date]
            to_delete = next(m for m in meetings if m['time'] == time)
            if type(to_delete) is dict:
                del to_delete
                self.save_db()

    # other methods

    def get_hour_minutes(self, time):
        temp = time.split(":")
        return int(temp[0]), int(temp[1])

    def get_day_month_year(self, date):
        temp = date.split(".")
        return int(temp[0]), int(temp[1]), int(temp[2])

    def calculate_date_with_offset(self, offset):
        last_month_day = self.month_last_day(self.today_month, self.today_year)
        new_day = self.today_day + offset
        if new_day > last_month_day:
            while True:
                difference = new_day - last_month_day
                if self.today_month == 12:
                    new_month = 1
                    new_year = self.today_year+1
                else:
                    new_month = self.today_month+1
                    new_year = self.today_year
                last_month_day = self.month_last_day(new_month, new_year)
                new_day = difference
                if new_day <= last_month_day:
                    date_str = ""
                    if new_day < 10:
                        date_str += "0"
                    date_str += str(new_day)
                    date_str += "."
                    if new_month < 10:
                        date_str += "0"
                    date_str += str(new_month)
                    date_str += "."
                    date_str += str(new_year)
                    return date_str
        else:
            date_str = ""
            if new_day < 10:
                date_str += "0"
            date_str += str(new_day)
            date_str += "."
            if self.today_month < 10:
                date_str += "0"
            date_str += str(self.today_month)
            date_str += "."
            date_str += str(self.today_year)
            return date_str

    def month_last_day(self, month, year):
        last_month_day = 30
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            last_month_day = 31
        elif month == 2:
            if year % 4 == 0:
                last_month_day = 29
            else:
                last_month_day = 28
        return last_month_day

    def is_date_day_name(self, date):
        if date == "poniedziałek":
            return True
        if date == "wtorek":
            return True
        if date == "środa":
            return True
        if date == "czwartek":
            return True
        if date == "piątek":
            return True
        if date == "sobota":
            return True
        if date == "niedziela":
            return True
        return False

    def get_days_difference(self, date):
        if date == "poniedziałek":
            if date == "poniedziałek":
                return 7
            if date == "wtorek":
                return 1
            if date == "środa":
                return 2
            if date == "czwartek":
                return 3
            if date == "piątek":
                return 4
            if date == "sobota":
                return 5
            if date == "niedziela":
                return 6
        if date == "wtorek":
            if date == "poniedziałek":
                return 6
            if date == "wtorek":
                return 7
            if date == "środa":
                return 1
            if date == "czwartek":
                return 2
            if date == "piątek":
                return 3
            if date == "sobota":
                return 4
            if date == "niedziela":
                return 5
        if date == "środa":
            if date == "poniedziałek":
                return 5
            if date == "wtorek":
                return 6
            if date == "środa":
                return 7
            if date == "czwartek":
                return 1
            if date == "piątek":
                return 2
            if date == "sobota":
                return 3
            if date == "niedziela":
                return 4
        if date == "czwartek":
            if date == "poniedziałek":
                return 4
            if date == "wtorek":
                return 5
            if date == "środa":
                return 6
            if date == "czwartek":
                return 7
            if date == "piątek":
                return 1
            if date == "sobota":
                return 2
            if date == "niedziela":
                return 3
        if date == "piątek":
            if date == "poniedziałek":
                return 3
            if date == "wtorek":
                return 4
            if date == "środa":
                return 5
            if date == "czwartek":
                return 6
            if date == "piątek":
                return 7
            if date == "sobota":
                return 1
            if date == "niedziela":
                return 2
        if date == "sobota":
            if date == "poniedziałek":
                return 2
            if date == "wtorek":
                return 3
            if date == "środa":
                return 4
            if date == "czwartek":
                return 5
            if date == "piątek":
                return 6
            if date == "sobota":
                return 7
            if date == "niedziela":
                return 1
        if date == "niedziela":
            if date == "poniedziałek":
                return 1
            if date == "wtorek":
                return 2
            if date == "środa":
                return 3
            if date == "czwartek":
                return 4
            if date == "piątek":
                return 5
            if date == "sobota":
                return 6
            if date == "niedziela":
                return 7
