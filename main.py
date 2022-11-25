import ply.lex as lex
from ply import yacc

saidas = []

def add_lista_saida(t, erro):
   saidas.append((t.lineno, t.lexpos, t.type, t.value, erro))

# Palavras reservadas do compilador
reserved = {
   'INICIO' : 'source',
   'FIM' : 'sink',
   'IF' : 'if',
   'ELSE' : 'else',
   'WHILE' : 'while',
   'INTERSECCAO' : 'inter',
   'UNIAO' : 'uni',
   'DIFERENCA' : 'dif',
   'SELECAO' : 'sel',
   'PROJECAO' : 'proj',
   'ENTRADA': 'input',
   'SAIDA': 'print',
   'TIPO_INT' : 'int_t',
   'TIPO_CHAR' : 'char_t',
   'TIPO_ARRAY' : 'array_t',
   'TIPO_MATRIZ' : 'matriz_t',
   'TIPO_DOUBLE' : 'double_t',
   'TIPO_BOOLEAN' : 'boolean_t',
   'TIPO_STRING' : 'string_t',
   'TIPO_PREMISSA' : 'premissa_t'
}

# Lista para os nomes dos tokens. Esta parte é sempre requerida pela Biblioteca PLY
tokens = [
                                                      #Operadores Aritméticos
   'MAIS' ,                #+
   'MENOS' ,               #-
   'MULTIPLICACAO',        #*
   'DIVISAO',              #/
   'MODULO',               #%
   'PRODUTO_CARTESIANO',   #x

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
   'IGUAL',              #==
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
   'MATRIZ',       #matriz
   'VARIAVEL'      #nome da variavel

                                                      #Atribuição
   'ATRIBUICAO',     #=

   #Para a criação dos RegEx (para verificar as compatibilidades) com o PLY,as verificações tem que ter uma "chamada" pelo token, é padrão
   'IGNORE',      #Ignorar tabulação e espaço

   'numero_mf',   #numero mal formado
   'string_mf',   #string mal formada

] + list(reserved.keys()) #concatenação com as palavras reservadas para verificação

#Regras de expressão regular (RegEx) para tokens simples

t_INICIO        = r'source'
t_FIM           = r'sink'
t_IF            = r'if'
t_ELSE          = r'else'
t_WHILE         = r'while'
t_INTERSECCAO   = r'inter'
t_UNIAO         = r'uni'
t_DIFERENCA     = r'dif'
t_SELECAO       = r'sel'
t_PROJECAO      = r'proj'
t_ENTRADA       = r'input'
t_SAIDA         = r'print'
t_TIPO_INT      = r'int_t'
t_TIPO_CHAR     = r'char_t'
t_TIPO_ARRAY    = r'array_t'
t_TIPO_MATRIZ   = r'matriz_t'
t_TIPO_DOUBLE   = r'double_t'
t_TIPO_BOOLEAN  = r'boolean_t'
t_TIPO_STRING   = r'string_t'
t_TIPO_PREMISSA = r'premissa_t'

t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO  = r'/'
t_MODULO = r'\%'
t_PRODUTO_CARTESIANO = r'x'
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
t_IGUAL = r'\=\='
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

t_ATRIBUICAO = r'\='

t_IGNORE = r'\s|\t' #ignora espaço e tabulação

#Regras de expressão regular (RegEx) para tokens mais "complexos"

def t_STRING(t):
    r'("[^"]{2,}")'
    return add_lista_saida(t,f"Nenhum")

def t_string_mf(t):
    r'("[^"]{2,})'
    return add_lista_saida(t,f"String mal formada")

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return add_lista_saida(t,f"Numero mal formado")

def t_DOUBLE(t):
    r'(\d*\.\d*)|(\d+\.\d*)'
    return add_lista_saida(t,f"Nenhum")

def t_INT(t):
    r'\d+'
    max = (len(t.value))
    if (max > 15):
        return add_lista_saida(t,f"Tamanho do Numero maior que o suportado")
        t.value = 0
    else:
        t.value = int(t.value)
        return add_lista_saida(t,f"Nenhum")

def t_BOOLEAN(t):
    r'\0|1'
    return add_lista_saida(t, f"Nenhum")

def t_CHAR(t):
    r'\"(\w|\+|\-|\*|/|\%)\"'
    return add_lista_saida(t, f"Nenhum")

def t_PREMISSA(t):
    r'\(\w\,\w\)'
    return add_lista_saida(t, f"Nenhum")

def t_VARIAVEL(t):
    r'[a-zA-Z](\w)*'
    return add_lista_saida(t, f"Nenhum")

#Regra para quebra de linhas
def t_QUEBRA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append((t.lineno,t.lexpos,t.type,t.value, f'Caracter nao reconhecido por esta linguagem'))
    t.lexer.skip(1)

#Análise Sintática

def p_empty(p):
    'empty :'
    pass

def p_fim_de_instrucao(p):
    'end : PONTO_E_VIRGULA'
    p[0]=p[1]

def p_valTipo(p):
    '''valTipo : TIPO_INT
               | TIPO_STRING
               | TIPO_BOOLEAN
               | TIPO_LITERAL
               | TIPO DOUBLE
    '''
    p[0]=p[1]

def p_array(p):
    '''array : INICIA_COLCHETES valTipo VIRGULA valTipo TERMINA_COLCHETES
             | INICIA_COLCHETES valTipo TERMINA_COLCHETES
    '''

def p_matrix(p):
    '''matrix : COMECO_DELIMITADOR_CHAVES array VIRGULA array FINAL_DELIMITADOR_CHAVES
              | CCOMECO_DELIMITADOR_CHAVES array FINAL_DELIMITADOR_CHAVES
              | COMECO_DELIMITADOR_CHAVES FINAL_DELIMITADOR_CHAVES
    '''
                 #  | while_codigo
                 #  | atribuicao end
                 #  | entrada end
                 #  | saida end

def p_conjunto(p):
    '''conjunto : VARIAVEL opConj VARIAVEL
                | VARIAVEL opConj ARRAY
                | ARRAY opConj VARIAVEL
                | ARRAY opConj ARRAY
    '''

def p_aritmetica(p):
    '''aritmetica: VARIAVEL opArit VARIAVEL
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
    ''' unario: opUna VARIAVEL
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

def p_digitos(p): # numeros que podemos fazer operacoes
    '''digitos : INT | DOUBLE
    '''

def p_opRel(p):
    '''opRel : IGUAL 
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
               | ABRE-PARENTESES
               | FECHA-PARENTESES
               | INICIA-COLCHETES
               | TERMINA-COLCHETES
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

def p_type_int(p):
    '''type_int : TIPO_INT
    '''

def p_type_string(p):
    '''type_string : TIPO_STRING
    '''

def p_type_boolean(p):
    '''type_boolean : TIPO_BOOLEAN
    '''

def p_type_literal(p):
    '''type_literal : TIPO_LITERAL
    '''

def p_type_double(p):
    '''type_double : TIPO_DOUBLE
    '''

def p_entrada(p):
    '''entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''

def p_saida(p):
    '''saida : SAIDA ABRE_PARENTESES STRING FECHA_PARENTESES
             | SAIDA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
             | SAIDA ABRE_PARENTESES QUEBRA_LINHA FECHA_PARENTESES
    '''
    if t[1].isdigit(): #valor da string
        print(t[1])
    elif t[1] == '\n': #quebra linha
        print('\n')
    else:              #nome da variavel
        print(t[1].value) #???

def p_codigo(p):
    '''codigo   : condicional
                | atribuicao end
                | entrada end
                | saida end
                | while
    '''

def p_lista_codigo(p):
    #lista_codigo
    '''lista_codigo : codigo PONTO_E_VIRGULA
                    | empty
    '''

def p_main(p):
    '''
    main: INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM
    '''

def p_declaracao(p):
    '''declaracao : type_int VARIAVEL 
                  |  type_string VARIAVEL
                  |  type_boolean VARIAVEL
                  |  type_literal VARIAVEL
                  |  type_double VARIAVEL
    '''

def p_atribuicao(p):
    '''atribuicao :  type_int VARIAVEL ATRIBUICAO INT
                  |  type_string VARIAVEL ATRIBUICAO STRING
                  |  type_boolean VARIAVEL ATRIBUICAO BOOLEAN
                  |  type_literal VARIAVEL ATRIBUICAO LITERAL
                  |  type_double VARIAVEL ATRIBUICAO DOUBLE
    '''

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
    errossintaticos.append(p)
    print("ERRO: ",p)

data = 'source{}sink'

lexer = lex.lex()
lexer.input(data)

#Léxica
#for tok in lexer:
#    print(tok)
#for retorno in saidas:
#    print(retorno)

#Sintática
parser = yacc.yacc()
result = parser.parse(data)
print(result)

