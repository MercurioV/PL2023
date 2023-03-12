import re
import json
def CSVtoJSON(csvfilename):
    f = open(f"tpc4/{csvfilename}.csv", "r")
    first = True
    campos = []
    listaData = []
    for line in f.readlines():
        line = line.replace('\n','')
        data = line.split(",")
        if(first):
            campos = ["Número","Nome","Curso","Notas{3,5}::media"]
            first = False
        else:
            contador = 0
            parejas = dict()
            for campo in campos:
                if "{" not in campo and not campo == "":
                    parejas[campo]=data[contador]
                    contador+=1
                else:
                    operation = ""
                    if "::" in campo:
                        fullcampo = campo
                        campo = fullcampo.split("::")[0]
                        operation = fullcampo.split("::")[1]
                    campoDiv = campo.split("{")
                    campoName = campoDiv[0]
                    campoDiv[1] = campoDiv[1].replace('}','')
                    if("," in campoDiv[1]):
                        limites = [int(campoDiv[1].split(",")[0]),int(campoDiv[1].split(",")[1])]
                    else:
                        limites = [int(campoDiv[1].replace("}","")),int(campoDiv[1].replace("}",""))]
                    lista = []
                    inside = True
                    while  inside:

                        if(contador==len(data)):
                            inside = False
                        elif(data[contador].isdigit()):
                            lista.append(int(data[contador]))
                            contador+=1
                        elif(not data[contador].isdigit()):
                            inside = False
                    if(len(lista)<limites[0] or len(lista)>limites[1]):
                        print("Invalid length for a list")
                        break
                    else:
                        if(operation == ""):
                            print({campoName:lista})
                            parejas.append({campoName:lista})
                        elif operation == "sum":
                            parejas[campoName]=sum(lista)
                        elif operation == "media":
                            parejas[campoName]=(sum(lista)/len(lista))

                            
            listaData.append(parejas)
    jsonString = json.dumps(listaData, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False).encode('utf-8')
    jsonFile = open(f"tpc4/{csvfilename}.json", "w")
    jsonFile.write(jsonString.decode())
    jsonFile.close()
    print(listaData)

CSVtoJSON("alunos3")
