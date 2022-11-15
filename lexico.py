import ply.lex as lex

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
   'PRODUTO_CARTESIANO' ,  #x

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
   'ASPAS',                   #"
   'INICIA_COLCHETES',        #[
   'TERMINA_COLCHETES',       #]
   'ABRE_PARENTESES',         #(
   'FECHA_PARENTESES',        #)

                                                      #Blocos de Comandos
   'COMECO_DELIMITADOR_CHAVES',         #{
   'FINAL_DELIMITADOR_CHAVES',          #}

                                                      #Identificadores
   'INT',          #inteiro
   'DOUBLE',       #double
   'STRING',       #string
   'CHAR',         #char
   'BOOLEAN',      #boolean

   'ATRIBUICAO',     #=

   #para a criação dos RegEx (para verificar as compatibilidades) com o PLY,as verificações tem que ter uma "chamada" pelo token, é padrão
   #'IGNORE',      #Ignorar tabulação e espaço

   'numero_mf',   #numero mal formado
   'string_mf',   #string mal formada

] + list(reserved.keys()) #concatenação com as palavras reservadas para verificação

#Regras de expressão regular (RegEx) para tokens simples

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO  = r'/'
t_MODULO = r'/%'
t_PRODUTO_CARTESIANO = r'/x'

t_AND = r'\&'
t_OR = r'\|'
t_DOUBLEAND_BITWISE =  r'\&&'
t_DOUBLEOR_BITWISE = r'\||2'

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
t_ASPAS = r'\"'
t_ABRE_PARENTESES  = r'\('
t_FECHA_PARENTESES  = r'\)'
t_INICIA_COLCHETES = r'\['
t_TERMINA_COLCHETES = r'\]'

t_COMECO_DELIMITADOR_CHAVES = r'\{'
t_FINAL_DELIMITADOR_CHAVES = r'\}'

t_ATRIBUICAO = r'\='

#t_IGNORE = ' \t' #ignora espaço e tabulação

#Regras de expressão regular (RegEx) para tokens mais "complexos"

def t_STRING(t):
    r'("[^"]*")'
    return add_lista_saida(t,f"Nenhum")

def t_string_mf(t):
    r'("[^"]*)'
    return add_lista_saida(t,f"String mal formada")

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return add_lista_saida(t,f"Numero mal formado")

def t_DOUBLE(t):
    # r'(\d*\.\d*)|(\d+\.\d*)'
    r'(\d*\.\d*)|(\d+\.\d*)'
    #t.value = float(t.value)
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

#Regra de tratamento de erros
def t_error(t):
    saidas.append((t.lineno,t.lexpos,t.type,t.value, f'Caracter nao reconhecido por esta linguagem'))
    t.lexer.skip(1)

data = '(5+3.3)'

lexer = lex.lex()
lexer.input(data)

for tok in lexer:
    print(tok)

for retorno in saidas:
    print(retorno)

