country_code = {
    "Iceland": {"code": "354", "capital": "Reykjavik"},
    "Ireland": {"code": "353", "capital": "Dublin"},
    "Azerbaijan": {"code": "994", "capital": "Baku"},
}


def getstr_keyval(x):
    if not isinstance(x, dict):
        return str(x)

    my_str = ""
    for key, val in x.items():
        my_str += " " + str(key) + ": " + getstr_keyval(val)
    return my_str


for country, values in country_code.items():
    print(country, getstr_keyval(values))
