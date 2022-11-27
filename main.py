import ply.lex as lex
import ast
from ply import yacc
from declarations import *

saidas = []

def add_lista_saida(t, erro):
   saidas.append((t.lineno, t.lexpos, t.type, t.value, erro))

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
   'AND',                  #&
   'OR',                   #|
   'DOUBLEAND_BITWISE',    #&&
   'DOUBLEOR_BITWISE',     #||

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
t_AND = r'\&'
t_OR = r'\|'
t_DOUBLEAND_BITWISE = r'\&&'
t_DOUBLEOR_BITWISE = r'\|\|'

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

#Regras de expressão regular (RegEx) para tokens mais "complexos"

def t_STRING(t):
    r'("[^"]{2,}")'
    if t.value in reserved: #Check for reserved words
        t.type = reserved[t.value]
    add_lista_saida(t,f"String mal formada")
    return t

def t_string_mf(t):
    r'("[^"]{2,})'
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    add_lista_saida(t,f"Numero mal formado")
    return t 

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    add_lista_saida(t,f"Variavel mal formada")
    return t

def t_BOOLEAN(t):
    r'(True)|(False)'
    t.value = bool(t.value)
    add_lista_saida(t,f"Nenhum")
    return t;

def t_DOUBLE(t):
    r'[+-]?(\d*\.\d*)|(\d+\.\d*)'
    t.value = float(t.value)
    add_lista_saida(t,f"Nenhum")
    return t

def t_INT(t):
    r'[+-]?\d+'
    max = (len(t.value))
    if (max > 15):
        add_lista_saida(t,f"Tamanho do Numero maior que o suportado")
        t.value = 0
    else:
        t.value = int(t.value)
        add_lista_saida(t,f"Nenhum")
    return t

def t_CHAR(t):
    r'\"(\w|\+|\-|\*|/|\%)\"'
    add_lista_saida(t, f"Nenhum")
    return t

def t_PREMISSA(t):
    r'\(\w\,\w\)'
    add_lista_saida(t, f"Nenhum")
    return t

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved: #Check for reserved words
        t.type = reserved[t.value]
    return t

def t_simbolo_invalido(t):
    r'[@#$&'']+'
    add_lista_saida(t,f"simbolo invalido")
    return t

#Regra para quebra de linhas
def t_QUEBRA_LINHA(t):
    r'\\n'
    t.lexer.lineno += len(t.value)
    return t

precedence = (
    ('left','ABRE_PARENTESES','FECHA_PARENTESES'),
    ('left','AND','OR'),
    ('left','MAIOR','MENOR', 'MAIOR_OU_IGUAL', 'MENOR_OU_IGUAL', 'IGUAL_IGUAL', 'DIFERENTE'),
    ('left','SOMA','SUBTRACAO'),
    ('left','MULTIPLICACAO','DIVISAO'),
    ('right', 'UMINUS', 'TILNOT_BITWISE', 'NOT'),
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
    pass

def p_fim_de_instrucao(p):
    '''end : PONTO_E_VIRGULA
    '''

def p_valTipo(p):
    '''valTipo : INT
               | STRING
               | BOOLEAN
               | CHAR
               | DOUBLE
    ''' 
    p[0] = p[1]
    
def p_lista_array(p):
    '''lista_array : INICIA_COLCHETES array TERMINA_COLCHETES
                   | INICIA_COLCHETES empty TERMINA_COLCHETES
    '''
    p[0]=[p[1]]

def p_array(p):
    '''array : valTipo VIRGULA array
             | valTipo
    '''
    if(len(p)>=2):
        p[0]=[p[1], p[3]]
    else:
        p[0]=p[1]

def p_matrix(p):
    '''matrix : COMECO_DELIMITADOR_CHAVES array VIRGULA array FINAL_DELIMITADOR_CHAVES
              | COMECO_DELIMITADOR_CHAVES array FINAL_DELIMITADOR_CHAVES
              | COMECO_DELIMITADOR_CHAVES FINAL_DELIMITADOR_CHAVES
    '''
    if(len(p)>=2):
        p[0]={p[2],p[4]}
    elif(len(p)==1):
        p[0]={p[2]}
    else:
        p[0]={}

def p_conjunto(t):
    '''conjunto : VARIAVEL opConj VARIAVEL
                | VARIAVEL opConj array
                | array opConj VARIAVEL
                | array opConj array
    '''

def p_aritmetica(t):
    '''aritmetica : VARIAVEL opArit VARIAVEL
                  | VARIAVEL opArit digitos
                  | digitos opArit VARIAVEL
                  | digitos opArit digitos
    '''

def p_logico(p):
    '''logico : VARIAVEL opLog VARIAVEL
              | VARIAVEL opLog digitos
              | VARIAVEL opLog relacional
              | digitos opLog VARIAVEL
              | digitos opLog digitos
              | digitos opLog relacional
              | relacional opLog VARIAVEL
              | relacional opLog digitos
              | relacional opLog relacional
    '''
    
def p_unario(p): 
    ''' unario : opUna VARIAVEL
               | opUna digitos
               | opUna relacional
               | opUna BOOLEAN
               | VARIAVEL
               | digitos
               | relacional
               | BOOLEAN
    '''

def p_relacional(p):
    '''relacional : VARIAVEL opRel VARIAVEL
                  | VARIAVEL opRel digitos
                  | VARIAVEL opRel STRING
                  | VARIAVEL opRel CHAR
                  | digitos opRel digitos
                  | digitos opRel VARIAVEL
                  | digitos opRel STRING
                  | digitos opRel CHAR
                  | STRING opRel STRING
                  | STRING opRel VARIAVEL
                  | STRING opRel CHAR
                  | STRING opRel digitos
                  | CHAR opRel VARIAVEL
                  | CHAR opRel digitos
                  | CHAR opRel STRING
                  | CHAR opRel CHAR
    '''

def p_digitos(p): #Números que podemos fazer operações ??
    '''digitos : INT 
               | DOUBLE
    '''

def p_opRel(p):
    '''opRel : IGUAL_IGUAL 
             | MAIOR_OU_IGUAL
             | MENOR_OU_IGUAL
             | MAIOR
             | MENOR
             | DIFERENTE
    '''      

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
             | DOUBLEAND_BITWISE
             | DOUBLEOR_BITWISE
    '''

def p_opUna(p):
    '''opUna : TILNOT_BITWISE 
             | NOT
    '''

def p_opConj(p):
    '''opConj : INTERSECCAO 
              | UNIAO
              | DIFERENCA
              | PRODUTO_CARTESIANO
    '''

def p_simbEsp(p):
    '''simbEsp : PONTO
               | VIRGULA
               | ABRE_PARENTESES
               | FECHA_PARENTESES
               | INICIA_COLCHETES
               | TERMINA_COLCHETES
               | PONTO_E_VIRGULA
    '''

def p_comProg(p):
    '''comProg : COMECO_DELIMITADOR_CHAVES
               | FINAL_DELIMITADOR_CHAVES
    '''

def p_bloProg(p):
    '''bloProg : INICIO
               | FIM
    '''

def p_types(p):
    '''type : TIPO_INT
            | TIPO_DOUBLE
            | TIPO_STRING
            | TIPO_CHAR
            | TIPO_BOOLEAN
    '''
    p[0] = p[1]

def p_entrada(t):
    '''entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    if(verify(t[3]) != None):
        tmp = input()
        try:
            tmp = ast.literal_eval(tmp)
        except:
            pass
        change(t[3], tmp)

def p_saida_string(t):
    '''saida_string : SAIDA ABRE_PARENTESES STRING FECHA_PARENTESES
                    | SAIDA ABRE_PARENTESES QUEBRA_LINHA FECHA_PARENTESES
    '''
    tmp = t[3]
    if tmp != "\\n":
        print(tmp.replace('"',''))
    else:
        print('\n')

def p_saida(t):
    '''
        saida_variavel : SAIDA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    tmp = t[3]
    if verify(tmp) != None:
        try:
            print(verify(tmp).replace('"',''))
        except:
            print(verify(tmp))
    else:
        raise Exception("(!) Variavel " + str(variable) + " nao existe")

def p_codigo(p):
   '''codigo    : condicional
                | atribuicao end
                | entrada end
                | saida_variavel end
                | saida_string end
                | declaracao end
                | conjunto end
                | while
    '''

def p_lista_codigo(p):
    '''lista_codigo : codigo lista_codigo
                    | empty
    '''
    
def p_main(p):
    '''main : INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM
    '''

def p_declaracao(p):
    '''declaracao : type VARIAVEL
    '''
    p[0] = add(p[1], p[2])

def p_expression_parenthesis(p):
    'expression : ABRE_PARENTESES expression FECHA_PARENTESES'
    p[0] = p[2]

def p_expression_uminus(p):
    '''expression : SUBTRACAO expression %prec UMINUS
    '''
    p[0] = -p[2]

def p_expressao(p):
    '''expression : valTipo
                  | VARIAVEL
    '''
    p[0] = p[1]

def p_binary_operators(p):
    '''expression : expression opArit expression
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
            if p[2] == '+':
                p[0] = vl1 + vl2
            elif p[2] == '-':
                p[0] = vl1 - vl2
            elif p[2] == '*':
                p[0] = vl1 * vl2
            elif p[2] == '/':
                p[0] = vl1 / vl2
            else:
                raise Exception("(!) Sinal invalido")
    except:
        if(type(p[1]) != type(p[3])):
                raise Exception ("(!) Operacao com tipos distintos")
        else:
            if p[2] == '+':
                p[0] = p[1] + p[3]
            elif p[2] == '-':
                p[0] = p[1] - p[3]
            elif p[2] == '*':
                p[0] = p[1] * p[3]
            elif p[2] == '/':
                p[0] = p[1] / p[3]
            else:
                raise Exception("(!) Sinal invalido")

def p_atribuicao(p):
    '''atribuicao : VARIAVEL IGUAL expression
                  | VARIAVEL IGUAL valTipo
    '''           
    p[0] = change(p[1], p[3])

def p_comparacao(p):
    '''comparacao : ABRE_PARENTESES comparacao FECHA_PARENTESES
    '''

def p_comparacao_relacional(p):
    '''comparacao : relacional opLog relacional
                  | relacional opLog logico
                  | relacional opLog unario
                  | logico opLog relacional
                  | logico opLog logico
                  | logico opLog unario
                  | unario opLog unario
                  | unario opLog relacional
                  | unario opLog logico
                  | relacional
                  | unario
                  | logico
    '''

def p_condicional(t):
    '''condicional : IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
                   | IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES ELSE COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''
    if(t[3]):
        t[0] = t[6]
    else:
        if(len(t) > 8): #with else
            t[0] = t[10]

def p_while(p):
    '''while : ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''

errossintaticos = []
def p_error(p):
    if p:
        errossintaticos.append(p)
        print("ERRO: ",p)

data = open('entrada.txt', 'r')
#\\n é o quebra linha pq o primeiro \ é pra dizer que o próximo \ tem q ser considera hahHAHAhahaha

text = ""
for linha in data:
    text += linha

lexer = lex.lex()
lexer.input(text)

#Léxica

for tok in lexer:
    print(tok)

#Sintática

parser = yacc.yacc(start = 'main')
result = parser.parse(text)
print("\nResult: " + str(result))



        

