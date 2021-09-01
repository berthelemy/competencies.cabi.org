import csv,yaml

# Assumes csv file with these columns in this order:
# skills,category,group,Plant doctors,Extension workers,Agri-dealer employees,Foundation,Practitioner,Advanced
# column 0 = text
# column 1 = text
# columns 2 onwards = boolean

with open('Agriculture-Skills-Framework-Analysis-3.3.csv',mode='r') as csv_file:
    datareader = csv.reader(csv_file, delimiter=",", quotechar='"')
    result = list()
#    type_index = -1
#    child_fields_index = -1

    for row_index, row in enumerate(datareader):

        if row_index == 0:
    # let's do this once here
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
                    content[data_headings[0]] = cell

                if cell_index == 1:
                    cell=cell.capitalize()
                    content[data_headings[1]] = cell

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

                content[data_headings[2]] = roles
                content[data_headings[3]] = levels
                content[data_headings[4]] = "Description placeholder"



            result.append(content)
            print(result)
            roles=[]
            levels=[]

        #print(result)
        file = open("skills.yaml","w")
        yaml.dump(result,file)
        file.close()
#csv=
#print (yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}))
