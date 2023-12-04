# Import json load and dump
from json import load, dump

# path for json file
json_path = "Mini-Project-Data-manipulation-and-analysis/Tasks.json"


def print_statistics():

    with open(json_path, 'r') as read_file:
        tasks_content = load(read_file)
        total_number_completed_tasks = 0
        total_number_of_incomplete = 0

        for each_record in tasks_content:
            if each_record['status'] == "complete":
                total_number_completed_tasks += 1
            if each_record['status'] == "incomplete":
                total_number_of_incomplete += 1
    print(f"No. of All tasks: {len(tasks_content)}")
    print(f"No. of Completed Tasks: {total_number_completed_tasks}")
    print(f"Percentage: {
          int((total_number_completed_tasks/len(tasks_content)) * 100)} %")
    print(f"No. of incomplete tasks: {total_number_of_incomplete}")


# print_statistics()
print("Good Day! welcome to basic data file handling in python. ")
user_command = input(
"""
    To add a new task type '1'. 
    To mark record as complete type '2'. 
    To delete a task type '3'. 
    To view the statistics type '4'.
    
    command: """)

user_is_using = True

while user_is_using:
    with open(json_path, 'r') as file:
        collection = load(file)
    
    if user_command == "1":

        with open(json_path, 'w') as file   :

            title = input("Title: ")
            description = input("description: ")
            category = input("category")

            collection.append(
                {
                    "Title": title, "description": description, "status": "incomplete", "category": category , "id":len(collection) + 1
                }
            )

            dump(collection,file)

    print(collection)
