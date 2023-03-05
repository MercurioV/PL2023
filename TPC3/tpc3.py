import re

def openFile(nameOfFile):
    dic = []
    file = open(nameOfFile)
    for line in file.readlines():
        line_array = line.split('::')
        if not line_array[0] == '\n':
            lineParsed = {
                    "processos" : int(line_array[0]),
                    "fecha" : line_array[1],
                    "persoas" : {line_array[2], line_array[3],line_array[4]},
                    "relation" : line_array[5]
                }
            dic.append(lineParsed)
    return dic

def frequenciaProcessosAño(data):
    dic = dict()
    for line in data:
        year = int(line["fecha"].split('-')[0])
        processos = line["processos"]
        if(year not in dic.keys()):
            dic[year] = processos
        else:
            dic[year] += processos
    return dic

def frequenciaNomesApelidoSeculo(data):
    dic = dict()
    for line in data:
        seculo = int(line["fecha"].split('-')[0][:2])+1
        processos = line["processos"]
        if(seculo not in dic.keys()):
            dicNomes = dict()
            dicApelidos = dict()
            for persoa in line["persoas"]:
                nomeApelidos = persoa.split(' ')
                nome = nomeApelidos[0]
                apelido = nomeApelidos[-1]
                if(nome not in dicNomes.keys()):
                    dicNomes[nome]=1
                else:
                    dicNomes[nome]+=1

                if(apelido not in dicApelidos.keys()):
                    dicApelidos[apelido]=1
                else:
                    dicApelidos[apelido]+=1
            dic[seculo] = {"nomes" : dicNomes, "apelidos":dicApelidos}      
        else:
            for persoa in line["persoas"]:
                nomeApelidos = persoa.split(' ')
                nome = nomeApelidos[0]
                apelido = nomeApelidos[-1]
                if nome not in dic[seculo]["nomes"].keys():
                    dic[seculo]["nomes"][nome]=1
                else:
                    dic[seculo]["nomes"][nome]+=1

                if(apelido not in dic[seculo]["apelidos"].keys()):
                    dic[seculo]["apelidos"][apelido]=1
                else:
                    dic[seculo]["apelidos"][apelido]+=1
    for seculo in dic.keys():
        names = dic[seculo]["nomes"]
        sorted_names = sorted(names.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_names)
        print(f"Seculo: {seculo}")
        contador = 0
        print("-Nomes:")
        for i in converted_dict.keys():
            if contador >= 5:
                break
            print(f"--{i}")
            contador+=1
        ##Apelidos
        apelidos = dic[seculo]["apelidos"]
        sorted_apelidos = sorted(apelidos.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_apelidos)
        contador = 0
        print("-Apelidos:")
        for i in converted_dict.keys():
            if contador >= 5:
                break
            print(f"--{i}")
            contador+=1
    return dic

def frequenciaTiposDoRelacion(dic):
    relationsDict = dict()
    for line in dic:
        relationLine = line["relation"]
        if relationLine:
            relations = relationLine.split("   ")
            for relation in relations:
                relation = re.sub(" ","",relation)
                start = re.escape(",")
                end   = re.escape(".Proc.")
                result = re.search('%s(.*)%s' % (start, end), relation)
                if(not result == None):
                    result = result.group(1)
                    result = re.sub(".*,"," ",result)
                    result = result.split(" ")
                    for r in result:
                        if r not in relationsDict.keys():
                            relationsDict[r] = 1
                        else:
                            relationsDict[r] +=1
    return relationsDict

def passToJSON(dic):
    contador = 0
    lista = []
    for line in dic:
        import json
        if(contador>=20):
            break
        i = 1
        persoas = {}
        for persoa in line["persoas"]:
            persoas[f"persoa{i}"] = persoa
            i+=1
        lineParsed = {
                "processos" : line["processos"],
                "fecha" : line["fecha"],
                "persoas" : persoas,
                "relation" : line["relation"]
        }
        lista.append(lineParsed)
    jsonString = json.dumps(lista, indent=4, separators=(',', ': '), sort_keys=True)
    jsonFile = open("tpc3/tpc3.json", "w")
    jsonFile.write(jsonString)

    jsonFile.close()              
passToJSON(openFile("tpc3/processos.txt"))