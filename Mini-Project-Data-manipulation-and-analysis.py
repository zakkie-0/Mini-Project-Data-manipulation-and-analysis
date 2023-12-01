from json import load, dump

json_path = "Mini-Project-Data-manipulation-and-analysis/Tasks.json"

with open(json_path, 'r') as file:

    print(f"{'Title':<30}{'description':<20}{'status':>25}{'category':>40}{'id':>25}".upper())

    tasks_content = load(file)

    for each_record in tasks_content:
        print(f"{each_record['Title']:<30}{each_record['description']:<39}{each_record['status']:<38}{each_record['category']:<30}{each_record['id']:>3}")


