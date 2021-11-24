import csv,yaml, time
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
timestamp = time.strftime('%H-%M-%S')
filename = "skills-"+date+"-"+timestamp+".yaml"
datetime = {
"date": date + " " + time.strftime('%H:%M:%S')
}


# Assumes csv file with these columns in this order:
# skills,category,group,Plant doctors,Extension workers,Agri-dealer employees,Foundation,Practitioner,Advanced
# column 0 = text
# column 1 = text
# columns 2 onwards = boolean

with open('Agriculture Skills Framework Analysis-20211124.csv',mode='r') as csv_file:
    datareader = csv.reader(csv_file, delimiter=",", quotechar='"')
    result = list()
    result.append(datetime)
#    type_index = -1
#    child_fields_index = -1

    for row_index, row in enumerate(datareader):

        if row_index == 0:
    # let's do this once here - set the items for the dict
            data_headings = ["title", "category", "roles", "levels", "description"]
            #for heading_index, heading in enumerate(row):
            #    fixed_heading = heading.lower().replace(" ", "_").replace("-", "")
            #    data_headings.append(fixed_heading)
        else:
            content = dict()
            roles = []
            levels = []
            for cell_index, cell in enumerate(row):
                #print(row)
                if cell_index == 0:
                    content[data_headings[0]] = cell # Set title

                if cell_index == 1:
                    cell=cell.capitalize()
                    content[data_headings[1]] = cell # Set category

                if cell_index == 3 and cell == "1":
                    roles.append('Plant doctors')
                if cell_index == 4 and cell == "1":
                    roles.append('Extension workers')
                if cell_index == 5 and cell == "1":
                    roles.append('Agri-dealer employees')

                if cell_index == 6 and cell == "1":
                    levels.append('Foundation')
                if cell_index == 7 and cell == "1":
                    levels.append('Practitioner')
                if cell_index == 8 and cell == "1":
                    levels.append('Advanced')

                if cell_index == 5 and roles == []:
                    roles.append('NO ROLE')
                if cell_index == 8 and levels == []:
                    levels.append('NO LEVELS')

                if cell_index == 12 and cell !="":
                    content[data_headings[4]] = cell # Description
                if cell_index == 12 and cell == "":
                    content[data_headings[4]] = "Description not yet defined"

                content[data_headings[2]] = roles
                content[data_headings[3]] = levels




            result.append(content)
            print(content[data_headings[0]])
            roles=[]
            levels=[]

        #print(result)

        file = open(filename,"w")
        yaml.dump(result,file)
        file.close()
#csv=
#print (yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}))
