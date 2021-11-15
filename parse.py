def parse_raw(raw_element):
    raw = raw_element
    ret = {}

    try:
        ret["id"] = raw[0].text
        ret["class"] = raw[1].text
        ret["name"] = raw[2].text
        ret["time"] = raw[10].text
        ret["room"] = raw[11].text
        ret["prof"] = raw[12].text
    except(IndexError):
        # lecture has lab time
        return {"lab": {"time": raw[0].text, "room": raw[1].text}}
    return ret
