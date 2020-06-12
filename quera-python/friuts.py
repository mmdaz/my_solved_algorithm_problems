def fruits(tuple_of_fruits):
    res = {}
    for f in tuple_of_fruits:
        if f['shape'] == "sphere" and 300 <= f["mass"] <= 600 and 100 <= f["volume"] <= 500:
            if res.get(f["name"]):
                res[f["name"]] = res[f["name"]] + 1
            else:
                res[f["name"]] = 1

    return res

