'''
Camila Motta Reno - 2019003833
Stefany Coura Coimbra - 2019008562
Ytalo Ysmaicon Gomes - 2019000223s
'''
from ply import yacc
from declarations import *
import ply.lex as lex
import sys
import os

# Variáveis auxiliares
ident = '''
    '''
exemplo = 0

# Palavras reservadas do compilador
reserved = {
   'source' : 'INICIO',
   'sink' : 'FIM',
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'False:':  'FALSE',
   'True' : 'TRUE',
   'inter' : 'INTERSECCAO',
   'uni' : 'UNIAO',
   'dif' : 'DIFERENCA',
   'sel' : 'SELECAO',
   'proj' : 'PROJECAO',
   'carte' : 'PRODUTO_CARTESIANO',
   'input' : 'ENTRADA',
   'print' : 'SAIDA',
   'int_t' : 'TIPO_INT',
   'char_t' : 'TIPO_CHAR',
   'array_t' : 'TIPO_ARRAY',
   'matrix_t' : 'TIPO_MATRIX',
   'double_t' : 'TIPO_DOUBLE',
   'boolean_t' : 'TIPO_BOOLEAN',
   'string_t' : 'TIPO_STRING',
   'premissa_t' : 'TIPO_PREMISSA'
}

# Lista para os nomes dos tokens. Esta parte é sempre requerida pela Biblioteca PLY
tokens = [
                                                      #Operadores Aritméticos
   'SOMA' ,                #+
   'SUBTRACAO' ,           #-
   'MULTIPLICACAO',        #*
   'DIVISAO',              #/
   'MODULO',               #%

                                                      #Operadores Lógicos
   'AND_BITWISE',         #&
   'OR_BITWISE',          #|
   'AND',                 #&&
   'OR',                  #||

                                                      #Operadores Unários
   'TILNOT_BITWISE',       #~
   'NOT',                  #!

                                                      #Operadores Relacionais
   'MENOR',              #<
   'MAIOR',              #>
   'MENOR_OU_IGUAL',     #<=
   'MAIOR_OU_IGUAL',     #>=
   'IGUAL_IGUAL',        #==
   'DIFERENTE',          #!=

                                                      #Simbolos Especiais
   'PONTO',                   #.
   'VIRGULA',                 #,
   'PONTO_E_VIRGULA',         #;
   'ASPAS',                   #"
   'INICIA_COLCHETES',        #[
   'TERMINA_COLCHETES',       #]
   'ABRE_PARENTESES',         #(
   'FECHA_PARENTESES',        #)

                                                      #Blocos de Comandos
   'COMECO_DELIMITADOR_CHAVES',         #{
   'FINAL_DELIMITADOR_CHAVES',          #}

                                                      #Identificadores
   'INT',          #int
   'DOUBLE',       #double
   'STRING',       #string
   'BOOLEAN',      #boolean
   'CHAR',         #char
   'PREMISSA',     #premissa
   'ARRAY',        #array
   'MATRIX',       #matrix
   'VARIAVEL',     #nome da variavel

                                                      #Atribuição
   'IGUAL',   #=
   
   'QUEBRA_LINHA', #\n

   #Para a criação dos RegEx (para verificar as compatibilidades) com o PLY,as verificações tem que ter uma "chamada" pelo token, é padrão
   'IGNORE',      #Ignorar tabulação e espaço

   'numero_mf',   #numero mal formado
   'string_mf',   #string mal formada
   'variavel_mf'  #variavel mal formada

] + list(reserved.values()) #concatenação com as palavras reservadas para verificação

#Regras de expressão regular (RegEx) para tokens simples

t_INICIO                = r'source'
t_FIM                   = r'sink'
t_IF                    = r'if'
t_ELSE                  = r'else'
t_WHILE                 = r'while'
t_INTERSECCAO           = r'inter'
t_UNIAO                 = r'uni'
t_DIFERENCA             = r'dif'
t_SELECAO               = r'sel'
t_PROJECAO              = r'proj'
t_PRODUTO_CARTESIANO    = r'carte'
t_ENTRADA               = r'input'
t_SAIDA                 = r'print'
t_TIPO_INT              = r'int_t'
t_TIPO_CHAR             = r'char_t'
t_TIPO_ARRAY            = r'array_t'
t_TIPO_MATRIX           = r'matrix_t'
t_TIPO_DOUBLE           = r'double_t'
t_TIPO_BOOLEAN          = r'boolean_t'
t_TIPO_STRING           = r'string_t'
t_TIPO_PREMISSA         = r'premissa_t'

t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO  = r'/'
t_MODULO = r'\%'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_AND_BITWISE = r'\&'
t_OR_BITWISE = r'\|'

t_TILNOT_BITWISE = r'\~'
t_NOT = r'\!'

t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MENOR_OU_IGUAL = r'\<\='
t_MAIOR_OU_IGUAL = r'\>\='
t_IGUAL_IGUAL = r'\=\='
t_DIFERENTE = r'\!\='

t_VIRGULA = r'\,'
t_PONTO = r'\.'
t_PONTO_E_VIRGULA = r'\;'
t_ASPAS = r'\"'
t_ABRE_PARENTESES  = r'\('
t_FECHA_PARENTESES  = r'\)'
t_INICIA_COLCHETES = r'\['
t_TERMINA_COLCHETES = r'\]'
t_COMECO_DELIMITADOR_CHAVES = r'\{'
t_FINAL_DELIMITADOR_CHAVES = r'\}'
t_IGUAL = r'\='

t_IGNORE = r' \t' #ignora espaço e tabulação

def t_QUEBRA_LINHA(t):
    r'"\n"'
    t.lexer.lineno += len(t.value)
    return t

def t_STRING(t):
    r'("[^"]{2,}")'
    if t.value in reserved: #Check for reserved words
        t.type = reserved[t.value]
    return t

def t_string_mf(t):
    r'("[^"]{2,})'
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return t 

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    return t

def t_BOOLEAN(t):
    r'(True)|(False)'
    if t.value == "True":
        t.value = bool(True)
    else:
        t.value = bool(False)
    
    return t

def t_DOUBLE(t):
    r'[+-]?(\d*\.\d*)|(\d+\.\d*)'
    t.value = float(t.value)
    
    return t

def t_INT(t):
    r'[+-]?\d+'
    max = (len(t.value))
    if (max > 15):
        
        t.value = 0
    else:
        t.value = int(t.value)
        
    return t

def t_CHAR(t):
    r'\"(\w|\+|\-|\*|/|\%)\"'
    return t

def t_PREMISSA(t):
    r'\(\w\,\w\)'
    return t

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved: #Check for reserved words
        t.type = reserved[t.value]
    return t

def t_simbolo_invalido(t):
    r'[@#$'']+'
    return t

precedence = (
    ('left','ABRE_PARENTESES','FECHA_PARENTESES'),
    ('left','AND','OR'),
    ('left','MAIOR','MENOR', 'MAIOR_OU_IGUAL', 'MENOR_OU_IGUAL', 'IGUAL_IGUAL', 'DIFERENTE'),
    ('left','SOMA','SUBTRACAO'),
    ('left','MULTIPLICACAO', 'DIVISAO'),
    ('right', 'UMINUS', 'TILNOT_BITWISE', 'NOT'),
    ('left', 'IF', 'ELSE')
)

#Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append((t.lineno,t.lexpos,t.type,t.value, f'Caracter nao reconhecido por esta linguagem'))
    t.lexer.skip(1)

#Análise Sintática

def p_empty(p): 
    '''empty :
    '''
    p[0] = ""

def p_fim_de_instrucao(p): 
    '''end : PONTO_E_VIRGULA
    '''

def p_types(p):
    '''type : TIPO_INT
            | TIPO_DOUBLE
            | TIPO_STRING
            | TIPO_CHAR
            | TIPO_BOOLEAN
    '''
    p[0] = p[1]

def p_valTipo(p): 
    '''valTipo : INT
               | STRING
               | BOOLEAN
               | CHAR
               | DOUBLE
    ''' 
    p[0] = p[1]

def p_digitos(p): 
    '''digitos : INT 
               | DOUBLE
    '''

def p_main(p): 
    '''main : INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM
    '''
    file = open(f"{arquivo}.py", "w")
    file.write(f"{p[3]}")
    file.close()

def p_codigo(p): 
    '''codigo   : condicional
                | atribuicao end
                | entrada end
                | saida_variavel end
                | saida_string end
                | declaracao end
                | conjunto end
                | while
    '''
    p[0] = p[1]

def p_lista_codigo(p): 
    '''lista_codigo : codigo lista_codigo
                    | empty
    '''
    if(len(p) == 2):
        p[0] = f''
    else:
        if p[2] == "":
            p[0] = f'{p[1]}'
        else:
            p[0] = f'{p[1]}'+f'\n'+f'{p[2]}' 

def p_declaracao(p): 
    '''declaracao : type VARIAVEL
    '''
    tmp = declare_value_type[p[1]]
    p[0] = f"{p[2]}: {tmp}" 

def p_atribuicao(p): 
    '''atribuicao : VARIAVEL IGUAL expression
                  | VARIAVEL IGUAL valTipo
    '''        
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_entrada(p): 
    '''entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    p[0] = f"{p[3]} = type({p[3]}) (input())"

def p_saida_string(p): 
    '''saida_string : SAIDA ABRE_PARENTESES STRING FECHA_PARENTESES
                    | SAIDA ABRE_PARENTESES QUEBRA_LINHA FECHA_PARENTESES
                    | SAIDA ABRE_PARENTESES CHAR FECHA_PARENTESES
    '''
    if len(p) == 5:
        p[0] = f'print({p[3]}, end="")'
    else:
        p[0] = f'print("\\n")'

    #tmp = t[3]
    #if tmp != "\\n":
    #    print(tmp.replace('"',''))
    #else:
    #    print('\n')

def p_saida(p): 
    '''saida_variavel : SAIDA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    p[0] = f'print({p[3]}, end="")'
    
    #tmp = t[3]
    #if verify(tmp) != None:
    #    try:
    #        print(verify(tmp).replace('"',''))
    #    except:
    #        print(verify(tmp))
    #else:
    #    raise Exception("(!) Variavel " + str(variable) + " nao existe")

def p_array(p): 
    '''array : valTipo VIRGULA array
             | valTipo
    '''
    if(len(p) >= 2):
        p[0]=f"{[p[1], p[3]]}"
    else:
        p[0]=f"{p[1]}"

def p_lista_array(p): 
    '''lista_array : INICIA_COLCHETES array TERMINA_COLCHETES
                   | INICIA_COLCHETES empty TERMINA_COLCHETES
    '''
    p[0]=f"[{p[1]}]"

def p_matrix(p):
    '''matrix : COMECO_DELIMITADOR_CHAVES array VIRGULA array FINAL_DELIMITADOR_CHAVES
              | COMECO_DELIMITADOR_CHAVES array FINAL_DELIMITADOR_CHAVES
              | COMECO_DELIMITADOR_CHAVES FINAL_DELIMITADOR_CHAVES
    '''
    if(len(p) >= 2):
        p[0]=f"{p[2],p[4]}"
    elif(len(p) == 1):
        p[0]=f"{p[2]}"
    else:
        p[0]=f""

def p_opRel(p):
    '''opRel : IGUAL_IGUAL 
             | MAIOR_OU_IGUAL
             | MENOR_OU_IGUAL
             | MAIOR
             | MENOR
             | DIFERENTE
    '''      
    p[0] = p[1]

def p_opArit(p):
    '''opArit : SOMA 
              | SUBTRACAO
              | MULTIPLICACAO
              | DIVISAO
              | MODULO
    '''
    p[0] = p[1]

def p_opLog(p):
    '''opLog : AND 
             | OR
             | AND_BITWISE
             | OR_BITWISE
    '''
    
def p_opConj(p):
    '''opConj : INTERSECCAO 
              | UNIAO
              | DIFERENCA
              | PRODUTO_CARTESIANO
    '''

def p_conjunto(p):
    '''conjunto : VARIAVEL opConj VARIAVEL
                | VARIAVEL opConj array
                | array opConj VARIAVEL
                | array opConj array
    '''

def p_comparacao_parenteses(p): 
    '''comparacao : ABRE_PARENTESES comparacao FECHA_PARENTESES
    '''
    p[0] = f"({p[2]})"

def p_comparacao_solo(t):
    '''comparacao : relacional
    '''
    t[0] = t[1]

def p_logico(p): 
    '''comparacao : comparacao AND comparacao
                  | comparacao OR comparacao
    '''
    if(p[2] == "&&"):
        p[0] = f"{p[1]} and {p[3]}"
    elif(p[2] == "||"):
        p[0] = f"{p[1]} or {p[2]}"
    else:
        raise Exception("(!) Operacao invalida")

def p_relacional_options(p): 
    '''relacional : VARIAVEL
                  | valTipo
    '''
    p[0] = f"{p[1]}"

def p_relacional(p): 
    '''relacional : relacional opRel relacional
    '''
    try: 
        try:
            tmp1 = verify_for_operation(p[1])
            vl1 = names[p[1]][1]
        except:
            tmp1 = type(p[1])
            vl1 = p[1]
        try:
            tmp2 = verify_for_operation(p[3])
            vl2 = names[p[3]][1]
        except:
            tmp2 = type(p[3])
            vl2 = p[3]
        if(tmp1 != tmp2):
            raise Exception ("(!) Operacao com tipos distintos")
        else:
            if(type(p[1]) == str and type(p[3]) == str):
                if(p[2] == '=='):
                    p[0] = f"{p[1]} == {p[3]}"
                elif(p[2] == '>='):
                    p[0] = f"{p[1]} >= {p[3]}"
                elif(p[2] == '<='):
                    p[0] = f"{p[1]} <= {p[3]}"
                elif(p[2] == '>'):
                    p[0] = f"{p[1]} > {p[3]}"
                elif(p[2] == '<'):
                    p[0] = f"{p[1]} < {p[3]}"
                elif(p[2] == '!='):
                    p[0] = f"{p[1]} != {p[3]}"
                else:
                    raise Exception("(!) Operador invalido")
            else:
                if(p[2] == '=='):
                    p[0] = f"{vl1} == {vl2}"
                elif(p[2] == '>='):
                    p[0] = f"{vl1} >= {vl2}"
                elif(p[2] == '<='):
                    p[0] = f"{vl1} <= {vl2}"
                elif(p[2] == '>'):
                    p[0] = f"{vl1} > {vl2}"
                elif(p[2] == '<'):
                    p[0] = f"{vl1} < {vl2}"
                elif(p[2] == '!='):
                    p[0] = f"{vl1} != {vl2}"
                else:
                    raise Exception("(!) Operador invalido")
    except:
        if(type(p[1]) != type(p[3])):
                raise Exception ("(!) Operacao com tipos distintos")
        else:
            if(p[2] == '=='):
                p[0] = f"{p[1]} == {p[3]}"
            elif(t[2] == '>='):
                p[0] = f"{p[1]} >= {p[3]}"
            elif(p[2] == '<='):
                p[0] = f"{p[1]} <= {p[3]}"
            elif(p[2] == '>'):
                p[0] = f"{p[1]} > {p[3]}"
            elif(p[2] == '<'):
                p[0] = f"{p[1]} < {p[3]}"
            elif(p[2] == '!='):
                p[0] = f"{p[1]} != {p[3]}"
            else:
                raise Exception("(!) Operador invalido")

def p_expression_parenthesis(p):
    '''expression : ABRE_PARENTESES expression FECHA_PARENTESES
    '''
    p[0] = f"({p[2]})"

def p_expression_uminus(p):
    '''expression : SUBTRACAO expression %prec UMINUS
    '''
    p[0] = -p[2]
    
def p_expressao_valor(p):
    '''expression : valTipo
                  | VARIAVEL
    '''
    p[0] = f"{p[1]}"

def p_binary_operators(p):
    '''expression : expression opArit expression %prec SOMA
    '''
    if p[2] == '+':
        p[0] = f"{p[1]} + {p[3]}"
    elif p[2] == '-':
        p[0] = f"{p[1]} - {p[3]}"
    elif p[2] == '*':
        p[0] = f"{p[1]} * {p[3]}"
    elif p[2] == '/':
        p[0] = f"{p[1]} / {p[3]}"
    elif p[2] == '%':
        p[0] = f"{p[1]} % {p[3]}"
    else:
        raise Exception("(!) Sinal invalido")

def p_condicional(p): 
    '''condicional : IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
                   | IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES ELSE COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''

    tmp1 = p[6].replace("\n", ident)
    tmp2 = p[10].replace("\n", ident)

    if(len(p) == 8):
        p[0] = f'''if {p[3]}:{ident}{tmp1}'''
    else:
        p[0] = f'''if {p[3]}:{ident}{tmp1}\nelse:{ident}{tmp2}''' 

def p_while(p): 
    '''while : WHILE ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''
    
    tmp = p[6].replace("\n", ident)

    p[0] = f'''while {p[3]}:{ident}{tmp}'''

errossintaticos = []
def p_error(p):
    if(p):
        errossintaticos.append(p)
        print("ERRO: ",p)

data = open(sys.argv[1], 'r')

text = ""
for linha in data:
    text += linha

lexer = lex.lex()
lexer.input(text)
arquivo, extensao = os.path.splitext(sys.argv[1])

#Léxica
fileTokens = open(f"tokens{exemplo}.txt", "w")
fileTokens.write(f"( TOKEN, 'palavra/simbolo' )\n")
for tok in lexer:
    tok = (f"( {tok.type}, '{tok.value}' )").replace("LexToken","")
    fileTokens.write(f"{tok}\n")
    
fileTokens.close()

#Sintática
parser = yacc.yacc(start = 'main')
result = parser.parse(text)