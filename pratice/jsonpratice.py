import json # import json module
from name import *
import io ,sys
# with statement

with open('world3.json') as json_file:
    json_data = json.load(json_file)

    success =0
    failed =[]
    print("총 나라 개수:"+str(len(english)))
    for e,i in enumerate(english):
        for d in json_data["features"]:
            if i==d["properties"]["NAME"]:
                success +=1
                d["properties"]["NAME"]=korean[e]
                break
            if d==json_data["features"][len(json_data["features"])-1]:
                failed.append(i)

    print("성공 몇개",success)
    print("failed",failed)

with open('world5.json', 'w',encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t",ensure_ascii = False)
