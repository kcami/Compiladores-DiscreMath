import ply.lex as lex
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
   'CHAR',         #char
   'BOOLEAN',      #boolean
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
    add_lista_saida(t,f"Nenhum")
    return t

def t_string_mf(t):
    r'("[^"]{2,})'
    add_lista_saida(t,f"String mal formada")
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    add_lista_saida(t,f"Numero mal formado")
    return t 

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    add_lista_saida(t,f"Variavel mal formada")
    return t

def t_DOUBLE(t):
    r'(\d*\.\d*)|(\d+\.\d*)'
    add_lista_saida(t,f"Nenhum")
    return t

def t_INT(t):
    r'\d+'
    max = (len(t.value))
    if (max > 15):
        add_lista_saida(t,f"Tamanho do Numero maior que o suportado")
        t.value = 0
    else:
        t.value = int(t.value)
        add_lista_saida(t,f"Nenhum")
    return t

def t_BOOLEAN(t):
    r'\0|1'
    add_lista_saida(t, f"Nenhum")
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
               | DOUBLE
               | CHAR
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
              | PRODUTO_CARTESIANO
    '''

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
            | TIPO_PREMISSA
    '''

def p_entrada(p):
    '''entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''

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
        print(verify(tmp))
    #else:
    #    p_error(t[3])

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
    '''
    main : INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM
    '''

def p_declaracao(p):
    '''declaracao : type VARIAVEL
    '''
    p[0] = add(p[2])


def p_atribuicao(p):
    '''atribuicao : VARIAVEL IGUAL valTipo
    '''
    p[0] = change(p[1],p[3])
    #falta fazer verificacao de tipo em declarations

def p_comparacao(p):
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

def p_condicional(p):
    '''condicional : IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
                   | IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES ELSE COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''

def p_while(p):
    '''while : ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES
    '''

errossintaticos = []
def p_error(p):
    if p:
        errossintaticos.append(p)
        print("ERRO: ",p)

data = '''
       source { 
            int_t c;
            c = 5;
            print(c);
            print("ab");
            print(\\n);
        }sink
       '''
#\\n é o quebra linha pq o primeiro \ é pra dizer que o próximo \ tem q ser considera hahHAHAhahaha

lexer = lex.lex()
lexer.input(data)

#Léxica

for tok in lexer:
    print(tok)

#Sintática

parser = yacc.yacc(start = 'main')
result = parser.parse(data)
print("\nResult: " + str(result))



        

