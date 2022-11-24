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
   'TIPO_LITERAL' : 'literal_t',
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
   'LITERAL',      #literal
   'CHAR',         #char
   'BOOLEAN',      #boolean
   'PREMISSA',     #premissa
   'ARRAY',        #array
   'MATRIZ',       #matriz

                                                      #Atribuição
   'ATRIBUICAO',     #=

   #Para a criação dos RegEx (para verificar as compatibilidades) com o PLY,as verificações tem que ter uma "chamada" pelo token, é padrão
   'IGNORE',      #Ignorar tabulação e espaço

   'numero_mf',   #numero mal formado
   'literal_mf',   #string mal formada

] + list(reserved.keys()) #concatenação com as palavras reservadas para verificação

#Regras de expressão regular (RegEx) para tokens simples

t_INICIO        = r'sink'
t_FIM           = r'source'
t_IF		    = r'if'
t_ELSE          = r'else'
t_WHILE		    = r'while'
t_INTERSECCAO   = 'rinter'
t_UNIAO         = 'r/uni'
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
t_TIPO_LITERAL  = r'literal_t'
t_TIPO_PREMISSA = r'premissa_t'

t_MAIS = r'\+'
t_MENOS = r'\-'
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

def t_LITERAL(t):
    r'("[^"]{2,}")'
    return add_lista_saida(t,f"Nenhum")

def t_literal_mf(t):
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

def t_ARRAY(t):
    r'\#'
    #a fazer

def t_MATRIZ(t):
    r'\@'
    #a fazer

#Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append((t.lineno,t.lexpos,t.type,t.value, f'Caracter nao reconhecido por esta linguagem'))
    t.lexer.skip(1)

#Análise Sintática

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statement : statement
    '''

def p_statement_source(p):
    '''
    statement : INICIO COMECO_DELIMITADOR_CHAVES statements FINAL_DELIMITADOR_CHAVES FIM PONTO_E_VIRGULA
    '''

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print("ERRO: ",p)

data = '(5+3.3&2%5)' \
       '5.f' \
       '>=' \
       'x' \
       '"x"' \
       '"5"' \
       '"+"' \
       '"%"' \
       '"ab"' \
       '(a,b) ' \
       'source'

lexer = lex.lex()
lexer.input(data)

for tok in lexer:
    print(tok)

for retorno in erroslexicos:
    print(retorno)

#parser = yacc.yacc()
#result = parser.parse(data)

#print(result)
