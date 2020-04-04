# todo: validate jsons
# for now just adding literally basic test
import json 
  
f = open("../data.json","r") 
all_qs = json.load(f)
test_pass = True
for q in all_qs: 
    test_pass &= (q["generated_id"].find(q["manual_id"]) != -1)
    if (q["generated_id"].find(q["manual_id"]) != -1) == False:
        print("Problem with JSON : " + q["generated_id"])
f.close()

if(test_pass):
    print("Tests Passed")
else:
    print("Tests Failed")