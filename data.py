import json
import glob

from variable import *


class DataManager:
    def __init__(self):
        self._all_lecture_list = self.load_lecture_data()
        self.selected_depart = []

        self.cur_lectures = []
        self.df_list = {}

        self.init_cache()

    def init_cache(self):
        self.cache_daytime = {
            day: {
                time: None for time in times
            }
            for day in days_kr
        }

    def load_lecture_data(self):
        lecture_data = {}
        for filename in glob.glob("lecture/*.json"):
            depart = filename.lstrip("lecture\\").rstrip(".json")
            with open(filename, "r", encoding="UTF-8") as f:
                lecture_data[depart] = (json.loads(f.read()))

        return lecture_data

    def add_depart(self, num):
        depart = departments[num]
        self.selected_depart.append(depart)
        self.df_list[depart] = self._all_lecture_list[depart]

        self.init_cache()

    def del_depart(self, num):
        depart = departments[num]
        self.selected_depart.remove(depart)
        del self.df_list[depart]

        self.init_cache()

    def find_by_daytime(self, day, time):
        day = day_kr(day)
        if self.cache_daytime[day][time] is not None:
            return self.cache_daytime[day][time]

        ret = []
        for depart in self.selected_depart:
            for lecture in self.df_list[depart]:
                lec_t = lecture['time']
                if 'lab' in lecture:
                    lab_t = lecture['lab']['time']
                else:
                    lab_t = ""

                match_lec = day in lec_t and time in lec_t
                match_lab = day in lab_t and time in lab_t

                if match_lec or match_lab:
                    ret.append(lecture)

        return ret

    def add_lecture(self, lec_name):
        self.cur_lectures.append(lec_name)

    def del_lecture(self, lec_name):
        self.cur_lectures.remove(lec_name)

    def find_by_name(self, lec_name):
        for depart in departments:
            for lecture in self._all_lecture_list[depart]:
                if lecture['name'] == lec_name:
                    return lecture
        raise ValueError
