names = []

declare_value_type =    { 
                        "int_t" : "int = 0",
                        "string_t" : "str = 0", 
                        "char_t" :  "chr = 0",
                        "boolean_t" : "bool = False",
                        "double_t" : "float = 0.0",
                        "array_t" : "any = []",
                        "matrix_t" : "any = [[]]"
                        }

def add_variable(variable):
    if(len(names) > 0):
        if variable not in names:
            names.append(variable)
        else:
            raise Exception("(!) Variavel " + str(variable) + " ja existente")
    else:
            names.append(variable)

def verify_for_operation(variable):
    if(len(names) > 0):
        if variable not in names:
            return False
        else:
            return True
    else:
        return False