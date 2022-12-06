'''
Camila Motta Reno - 2019003833
Stefany Coura Coimbra - 2019008562
Ytalo Ysmaicon Gomes - 2019000223
'''
import ply.lex as lex
import sys
import os

import warnings
warnings.filterwarnings("ignore")

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
   'ponens' : 'MODUS_PONENS',
   'tolens' : 'MODUS_TOLENS',
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

                                                      #Comentários
   'COMENTARIO_LINHA',  

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
t_MODUS_PONENS          = r'ponens'
t_MODUS_TOLENS          = r'tolens'
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

def t_COMENTARIO_LINHA(t):
     r'\$.*\$'
     return(t)
     
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
    r'([0-9]+[a-z]+)|([@#%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@#%&*]+)'
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
    r'[@#'']+'
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

arquivo, extensao = os.path.splitext(sys.argv[1])

data = open(sys.argv[1], 'r')

text = ""
for linha in data:
    text += linha

lexer = lex.lex(errorlog=lex.NullLogger())
lexer.input(text)

#Geração de tokens
with open(f"./tokens/tokens_{arquivo}.txt", "w") as fileTokens, open(f"./erros/erros_{arquivo}.txt", "w") as file1:
        fileTokens.write(f"( TOKEN, 'palavra/simbolo' )\n")
        for tok in lexer:
            tok = (f"( {tok.type}, '{tok.value}' )").replace("LexToken","")
            fileTokens.write(f"{tok}\n")
        fileTokens.close()
        file1.write(f"( TOKEN, 'palavra/simbolo' )\n")
        for tok in lexer:
            tok = (f"( {tok.type}, '{tok.value}' )").replace("LexToken","")
            file1.write(f"{tok}\n")
        file1.close()
