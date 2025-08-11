import json
with open("toto.json", "r") as file:
    data =  []
    for line in file:
        try:
            line = line.strip()
            if not line:
                continue
            
            obj = json.loads(line)
            data.append(obj)
        except json.JSONDecodeError as e:
            print(f"{e}  ligne {line}")
            
        
with  open("result.json", "w") as result_file:
    json.dump(data, result_file, indent=1)