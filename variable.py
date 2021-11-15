POVIS_URL = "http://povis.postech.ac.kr/irj/portal"
departments = [
    "GEDU",
    "MATH",
    "PHYS",
    "CHEM",
    "LIFE",
    "MECH",
    "CSED",
    "IMEN",
    "AMSE",
    "EECE",
    "CHEB",
]

departments_kr = [
    "인문사회학부",
    "수학과",
    "물리학과",
    "화학과",
    "생명과학과",
    "기계공학과",
    "컴퓨터공학과",
    "산업경영공학과",
    "신소재공학과",
    "전자전기공학과",
    "화학공학과",
]

times = [
    "09:30 ~ 10:45", "11:00 ~ 12:15",
    "12:30 ~ 13:45", "14:00 ~ 15:15",
    "15:30 ~ 16:45", "17:00 ~ 18:15",
    "19:00 ~ 19:50", "20:00 ~ 20:50"
]

days = ["MON", "TUE", "WED", "THU", "FRI"]
days_kr = ["월", "화", "수", "목", "금"]


def day_kr(day):
    if day == "MON":
        return "월"
    elif day == "TUE":
        return "화"
    elif day == "WED":
        return "수"
    elif day == "THU":
        return "목"
    elif day == "FRI":
        return "금"
