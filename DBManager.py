import json
from pathlib import Path
from dateHelper import format_date, get_date, format_time, get_end_time
import datetime

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
    def __init__(self, db_path="data-base/calendar.json"):
        self.db = {}
        self.db_file_path = Path(db_path)
        if self.db_file_path.is_file():
            with open(self.db_file_path, 'r+') as f:
                self.db = json.load(f)

    def save_db(self):
        with open(self.db_file_path, 'w+') as f:
            json.dump(self.db, f)

    # CRUD methods
    def create_meeting(self, meeting_dict):
        date_time = get_date(
            meeting_dict['date'].lower(), meeting_dict['time'].lower())

        if format_date(date_time) in self.db.keys():
            if not self.is_collision(format_date(date_time), meeting_dict['time']):
                self.db[format_date(date_time)].append(meeting_dict)
                self.save_db()
        else:
            self.db[format_date(date_time)] = [meeting_dict]
            self.save_db()

    def delete_meeting(self, date, time):
        date_time = get_date(date, time)

        if format_date(date_time) in self.db.keys():
            meetings = self.db[format_date(date_time)]
            for key, meeting in enumerate(meetings):
                if format_time(meeting['time']) == format_time(time):
                    meetings.remove(meeting)

            self.db[format_date(date_time)] = meetings
            self.save_db()

    def update_meeting(self, meeting_dict):
        date_time = get_date(
            meeting_dict['date'].lower(), meeting_dict['time'].lower())

        if format_date(date_time) in self.db.keys():
            meetings = self.db[format_date(date_time)]
            for key, meeting in enumerate(meetings):
                if format_time(meeting['time']) == format_time(meeting_dict['time'].lower()):
                    meetings.remove(meeting)

            meetings.append(meeting_dict)
            self.db[format_date(date_time)] = meetings
            self.save_db()

    def find_meeting(self, date, time):
        if date in self.db.keys():
            meetings = self.db[date]
            for m in meetings:
                # Czas może być w formacie (13, 13:00, 13:00-13:30), trzeba dopasować obie strony i porównywać tylko czas startu
                if format_time(time) == format_time(m['time']):
                    return m
            return None
        else:
            return None

    def get_meetings(self, date_list):
        # lista dat dla których chcemy znaleźć spotkania
        meetings = []
        for date in date_list:
            if date in self.db.keys():
                meetings += self.db[date]
        return meetings

    def is_collision(self, date, time):
        meetings = self.db[date]
        start_time = format_time(time)
        end_time = get_end_time(time)

        for meeting in meetings:
            if self.overlap(start_time, end_time, format_time(meeting['time']), get_end_time(meeting['time'])):
                return True
            if start_time == format_time(meeting['time']) or end_time == get_end_time(meeting['time']):
                return True
        return False

    def overlap(self, checking_start, checking_end, base_start, base_end):
        interval1 = [datetime.datetime.strptime(checking_start, '%H:%M'),
                     datetime.datetime.strptime(checking_end, '%H:%M')]
        interval2 = [datetime.datetime.strptime(base_start, '%H:%M'),
                     datetime.datetime.strptime(base_end, '%H:%M')]
        results = []
        for timestamp in interval1:
            results.append(interval2[0] < timestamp < interval2[1])
        for timestamp in interval2:
            results.append(interval1[0] < timestamp < interval1[1])
        return True in results

    # def get_freetime(self, date_list):
    #     freetime_dict = {}
    #     for date in date_list:
    #         time_str = self.start_day_time + "-" + self.end_day_time
    #         freetime_dict[date] = [time_str]
    #         # Change free time if there are meetings at this day
    #         if date in self.DB.keys():
    #             for meeting in self.DB[date]:
    #                 meeting_time = meeting['time'].split("-")
    #                 start = meeting_time[0]
    #                 # meeting has start and end time
    #                 if len(meeting_time > 1):
    #                     end = meeting_time[1]
    #                     meet_start_h, meet_start_m = self.get_hour_minutes(
    #                         start)
    #                     meet_end_h, meet_end_m = self.get_hour_minutes(end)
    #                     for slot in freetime_dict[date]:
    #                         slot_time = slot.split("-")
    #                         slot_start_h, slot_start_m = self.get_hour_minutes(
    #                             slot_time[0])
    #                         slot_end_h, slot_end_m = self.get_hour_minutes(
    #                             slot_time[1])
    #                         # if meeting time have collision with slot time - change / split slot

    #                         # meeting starts inside slot
    #                         if meet_start_h == slot_start_h and meet_start_m > slot_start_m and meet_start_h < slot_end_h:
    #                             pass
    #                         elif meet_start_h == slot_start_h and meet_start_m > slot_start_m and meet_start_h == slot_end_h and meet_start_m < slot_end_m:
    #                             pass
    #                         elif meet_start_h > slot_start_h and meet_start_h < slot_end_h:
    #                             pass
    #                         elif meet_start_h > slot_start_h and meet_start_h == slot_end_h and meet_start_m < slot_end_m:
    #                             pass

    #                         # starts before slot, ends inside slot
    #                         elif (meet_end_h > slot_start_h) or (meet_end_h == slot_start_h and meet_end_m > slot_start_h):
    #                             # meeting in whole slot - delete this slot
    #                             if meet_end_h == slot_end_h and meet_end_m == slot_end_m:
    #                                 pass
    #                             # cut slot from left side
    #                             else:
    #                                 pass
    #                         # if meeting starts and ends before slot start time - do nothing
    #                 # meeting has only start time
    #                 else:
    #                     m_start_h, m_start_m = self.get_hour_minutes(start)


# Tests

# db = calender_db()
# db.create_meeting({"date": "16.06.2021", "time": "15:00",
#                   "description": "chuj"})
# db.create_meeting({"date": "14.06.2021", "time": "13:00-18:00"})
# db.delete_meeting("16.06.2021", "15:00")
# print(db.find_meeting("16.06.2021", "13:00-14:00"))
# print(db.get_meetings(["16.06.2021", "14.06.2021"]))
# print(db.is_collision("16.06.2021", "12:30-13"))
