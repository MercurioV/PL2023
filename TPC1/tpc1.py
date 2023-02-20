from prettytable import PrettyTable 

dic = []
def openFile(nameOfFile):
    file = open(nameOfFile)
    first = True
    for line in file.readlines():
        line_array = line.split(',')
        if(not first):
            lineParsed = {
                    "idade" : int(line_array[0]),
                    "sexo" : line_array[1],
                    "tensao" : int(line_array[2]),
                    "colesterol" : int(line_array[3]),
                    "batimento" : int(line_array[4]),
                    "temDoença" : int(line_array[5])
                }
            dic.append(lineParsed)
        first = False
    return dic

def distributionBySex(dic):

    dictionary = dict()
    dictionary["Hombres"] = {
            "total" : 0,
            "sick" : 0,
        }
    dictionary["Mujeres"] = {
            "total" : 0,
            "sick" : 0,
        }

    for data in dic:
        if(data["sexo"]=="M"):
            if(data["temDoença"]==1):
                dictionary["Hombres"]["sick"]+=1
            dictionary["Hombres"]["total"]+=1
        elif(data["sexo"]=="F"):
            if(data["temDoença"]==1):
                dictionary["Mujeres"]["sick"]+=1
            dictionary["Mujeres"]["total"]+=1

    return dictionary


def distributionByAge(data):
    dictionary = dict()
    dictionary["[30-34]"] = {
            "total" : 0,
            "sick" : 0,
        }
    for age in range(34,75,5):
        bottom = age+1
        top = age+5
        dictionary[f"[{bottom}-{top}]"] = {
            "total" : 0,
            "sick" : 0,
        }
    for elem in data:
        for key in dictionary.keys():
            ages = key.split('-')
            if(elem["idade"]>=int(ages[0][1:]) and elem["idade"]<=int(ages[1][:-1])):
                dictionary[key]["total"] +=1
                if(elem["temDoença"]==1):
                    dictionary[key]["sick"] +=1
    return dictionary


def distributionByColesterol(data):
    data.sort(key=lambda d: d['colesterol'])
    contador = 0
    dictionary = dict()
    maxLevel = max(data, key=lambda x:x['colesterol'])["colesterol"]
    if not maxLevel%10 ==0:
        while not maxLevel%10 ==0:
            maxLevel+=1
    for i in range(0,maxLevel,10):
        dictionary[f"[{i}-{i+9}]"] = {
            "total" : 0,
            "sick" : 0,
        }
    for key in dictionary.keys():
        for d in data:
            limits = key.split('-')
            if(d["colesterol"]>=int(limits[0][1:]) and d["colesterol"]<=int(limits[1][:-1])):
                dictionary[key]["total"] +=1
                if(d["temDoença"]==1):
                    dictionary[key]["sick"] +=1
    return dictionary

def printTabla(dictionary):
    my_table = PrettyTable()
    my_table.field_names = ["Range", "Sick", "Total"]
    for key in dictionary.keys():
        my_table.add_row([key, dictionary[key]["sick"], dictionary[key]["total"]])
    print(my_table)

print("-------------Sex-------------")
printTabla(distributionBySex(openFile("myheart.csv")))
print("-------------Age-------------")
printTabla(distributionByAge(openFile("myheart.csv")))
print("-----------Colesterol-----------")
printTabla(distributionByColesterol((openFile("myheart.csv"))))