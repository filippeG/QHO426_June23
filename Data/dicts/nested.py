def short_pattern():
    pattern = {"sequence":"101", "occurences":5}
    return pattern


def medium_pattern():
    pattern = {"sequence" : "111000", "occurrences":25}
    return pattern


def long_pattern():
    pattern = {"sequence":"11001100110011001100", "occurrances":50}
    return pattern


def pattern(s,p):
    return {"sequences":s, "occurrances":0}


def run():
    print("Analyzing Patterns ...")
    d = {"short pattern":short_pattern(), "medium pattern": medium_pattern(), "long pattern": long_pattern()}
    for k,v in d.items():
        print(f"{k}:{v}")
run()





