names = {}

def add(variable):
    if(len(names) > 0):
        if variable not in names.keys():
            names[variable] = 0
        else:
            print("! Variavel " + str(variable) + " ja existente")
    else:
        names[variable] = 0
    #print('names:' +str(names))

def change(variable, value):
    if(len(names) > 0):
        if variable not in names.keys():
            print("(!) Variavel " + str(variable) + " nao existe")
        else:
            names[variable] = value
    else:
        print("(!) Variavel " + str(variable) + " nao existe")
    #print('names:' +str(names))

def verify(variable):
    if(len(names) > 0):
        if variable not in names.keys():
            print("(!) Variavel " + str(variable) + " nao existe")
            return None
        else:
            return names[variable]
    else:
        print("(!) Variavel " + str(variable) + " nao existe")
        return None
    