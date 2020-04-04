import os
import glob
import json
import re
import markdown
import csv

def all_folder( dir ):
    return [dI for dI in os.listdir(dir) if os.path.isdir(os.path.join(dir,dI))]

def get_plain_text(text):
    text = text.replace("<br>", " ")
    text = text.replace("<*>", " ")
    # todo: remove links only, i.e. matcher for []()
    pattern = r'\[|\]|\(|\)'
    text = re.sub(pattern, ' ', text)
    return text

def get_html(text):
    text = text.replace("<*>", "<br> * ")
    text = markdown.markdown(text)
    return text

raw_data_dir = "../raw_data"
sources = all_folder(raw_data_dir)

gen_dir = "../generated_jsons"
all_q_list = []

csv_file = open('../data.csv', 'w')
csv_writer = csv.writer(csv_file)
head_f = True

for source in sources:

    source_dir = raw_data_dir + "/" + source
    source_info_json = json.load(open(source_dir + "/info.json","r"))
    #print(source_info_json)

    que_ps = source_dir + "/question/*.json"
    qs_dir = sorted(glob.glob(que_ps), key=lambda f: int(re.sub('\D', '', f)))
    
    for q_dir in qs_dir:
        q_json = json.load(open(q_dir,"r"))
        #print(q_json["question"])
        gen_q = {}
        gen_q["generated_id"] = source_info_json["short_name"] + "_q_" + q_json["manual_id"]
        gen_q.update(q_json)
        gen_q["answer_plain"] = get_plain_text(q_json["answer"])
        gen_q["answer_html"] = get_html(q_json["answer"])
        gen_q["source_short_name"] = source_info_json["short_name"]
        gen_q["source_full_name"] = source_info_json["full_name"]
        gen_q["source_questions_url"] = source_info_json["source_url"]
        gen_q["source_logo_url"] = source_info_json["logo_url"]

        all_q_list.append(gen_q)

        if(head_f):
            csv_writer.writerow(gen_q.keys())
            head_f = False
        csv_writer.writerow(gen_q.values())

        q_gen_dir = gen_dir + "/" + source_info_json["short_name"] + "_question_" + q_json["manual_id"] + ".json"

        with open(q_gen_dir, 'w', encoding='utf-8') as f:
            json.dump(gen_q, f, ensure_ascii=False, indent=4)

csv_file.close()
#print(all_q_list)
all_q_dir = "../data.json"
with open(all_q_dir, 'w', encoding='utf-8') as f:
    json.dump(all_q_list, f, ensure_ascii=False, indent=4)