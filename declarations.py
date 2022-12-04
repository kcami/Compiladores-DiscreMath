names = {}

# init_value_type =   { 
#                     "int_t" : 0,
#                     "string_t" : '""', 
#                     "char_t" :  '""',
#                     "boolean_t" : False,
#                     "double_t" : 0.0
#                     }

declare_value_type =    { 
                        "int_t" : "int = 0",
                        "string_t" : "str = 0", 
                        "char_t" :  "chr = 0",
                        "boolean_t" : "bool = False",
                        "double_t" : "float = 0.0",
                        "array_t" : "any = []",
                        "matrix_t" : "any = [[]]"
                        }

# def add(type, variable):
#     if(len(names) > 0):
#         if variable not in names.keys():
#             names[variable] = [type, init_value_type[type]]
#         else:
#             raise Exception("(!) Variavel " + str(variable) + " ja existente")
#     else:
#             names[variable] = [type, init_value_type[type]]
#     #print('names:' + str(names))

# def change(variable, value):
#     if(len(names) > 0):
#         if variable not in names.keys():
#             raise Exception("(!) Variavel " + str(variable) + " nao existe")
#         else:
#             print(type(names[variable][1]))
#             print(type(value))
#             if(type(names[variable][1]) == type(value)):
#                 if names[variable][0] != "char_t":
#                     names[variable][1] = value
#                 elif len(value) == 1:
#                     names[variable][1] = value
#                 else:
#                     raise Exception("(!) Valor do tipo incompativel")
#             else:
#                 raise Exception("(!) Valor do tipo incompativel")
#     else:
#         raise Exception("(!) Variavel " + str(variable) + " nao existe")
#     #print('names:' +str(names))

# def verify(variable):
#     if(len(names) > 0):
#         if variable not in names.keys():
#             raise Exception("(!) Variavel " + str(variable) + " nao existe")
#             return None
#         else:
#             return names[variable][1]
#     else:
#         raise Exception("(!) Variavel " + str(variable) + " nao existe")
#         return None

def verify_for_operation(variable):
    if(len(names) > 0):
        if variable not in names.keys():
            raise Exception("(!) Variavel " + str(variable) + " nao existe")
        else:
            return type(names[variable][1])
    else:
        raise Exception("(!) Variavel " + str(variable) + " nao existe")
    #print('names:' +str(names))