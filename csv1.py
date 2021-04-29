import csv



def get_group_id(group_name):
    with open('group.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row["name"]: row["id"] for row in reader}
        return data[group_name]
        
