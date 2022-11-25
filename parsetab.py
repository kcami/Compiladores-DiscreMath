
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_PARENTESES AND ARRAY ASPAS ATRIBUICAO BOOLEAN CHAR COMECO_DELIMITADOR_CHAVES DIFERENCA DIFERENTE DIVISAO DOUBLE DOUBLEAND_BITWISE DOUBLEOR_BITWISE ELSE ENTRADA FECHA_PARENTESES FIM FINAL_DELIMITADOR_CHAVES IF IGNORE IGUAL INICIA_COLCHETES INICIO INT INTERSECCAO MAIOR MAIOR_OU_IGUAL MATRIZ MENOR MENOR_OU_IGUAL MODULO MULTIPLICACAO NOT OR PONTO PONTO_E_VIRGULA PREMISSA PRODUTO_CARTESIANO PROJECAO QUEBRA_LINHA SAIDA SELECAO SOMA STRING SUBTRACAO TERMINA_COLCHETES TILNOT_BITWISE TIPO_ARRAY TIPO_BOOLEAN TIPO_CHAR TIPO_DOUBLE TIPO_INT TIPO_MATRIZ TIPO_PREMISSA TIPO_STRING UNIAO VARIAVEL VIRGULA WHILE numero_mf string_mfempty :end : PONTO_E_VIRGULAvalTipo : TIPO_INT\n               | TIPO_STRING\n               | TIPO_BOOLEAN\n               | TIPO_DOUBLE\n    array : INICIA_COLCHETES valTipo VIRGULA valTipo TERMINA_COLCHETES\n             | INICIA_COLCHETES valTipo TERMINA_COLCHETES\n    matrix : COMECO_DELIMITADOR_CHAVES array VIRGULA array FINAL_DELIMITADOR_CHAVES\n              | COMECO_DELIMITADOR_CHAVES array FINAL_DELIMITADOR_CHAVES\n              | COMECO_DELIMITADOR_CHAVES FINAL_DELIMITADOR_CHAVES\n    conjunto : VARIAVEL opConj VARIAVEL\n                | VARIAVEL opConj ARRAY\n                | ARRAY opConj VARIAVEL\n                | ARRAY opConj ARRAY\n    aritmetica : VARIAVEL opArit VARIAVEL\n                  | VARIAVEL opArit digitos\n                  | digitos opArit VARIAVEL\n                  | digitos opArit digitos\n    logico : VARIAVEL opLog VARIAVEL\n              | VARIAVEL opLog digitos\n              | VARIAVEL opLog relacional\n              | digitos opLog VARIAVEL\n              | digitos opLog digitos\n              | digitos opLog relacional\n              | relacional opLog VARIAVEL\n              | relacional opLog digitos\n              | relacional opLog relacional\n     unario : opUna VARIAVEL\n               | opUna digitos\n               | opUna relacional\n               | opUna BOOLEAN\n               | VARIAVEL\n               | digitos\n               | relacional\n               | BOOLEAN\n    relacional : VARIAVEL opRel VARIAVEL\n                  | VARIAVEL opRel digitos\n                  | VARIAVEL opRel STRING\n                  | VARIAVEL opRel CHAR\n                  | digitos opRel digitos\n                  | digitos opRel VARIAVEL\n                  | digitos opRel STRING\n                  | digitos opRel CHAR\n                  | STRING opRel STRING\n                  | STRING opRel VARIAVEL\n                  | STRING opRel CHAR\n                  | STRING opRel digitos\n                  | CHAR opRel VARIAVEL\n                  | CHAR opRel digitos\n                  | CHAR opRel STRING\n                  | CHAR opRel CHAR\n    digitos : INT \n               | DOUBLE\n    opRel : IGUAL \n             | MAIOR_OU_IGUAL\n             | MENOR_OU_IGUAL\n             | MAIOR\n             | MENOR\n             | DIFERENTE\n    opArit : SOMA \n             | SUBTRACAO\n             | MULTIPLICACAO\n             | DIVISAO\n             | MODULO\n             | PRODUTO_CARTESIANO\n    opLog : AND \n             | OR\n             | DOUBLEAND_BITWISE\n             | DOUBLEOR_BITWISE\n    opUna : TILNOT_BITWISE \n             | NOT\n    opConj : INTERSECCAO \n              | UNIAO\n              | DIFERENCA\n    simbEsp : PONTO\n               | VIRGULA\n               | ABRE_PARENTESES\n               | FECHA_PARENTESES\n               | INICIA_COLCHETES\n               | TERMINA_COLCHETES\n               | PONTO_E_VIRGULA\n    comProg : COMECO_DELIMITADOR_CHAVES\n               | FINAL_DELIMITADOR_CHAVES\n    bloProg : INICIO\n               | FIM\n    type_int : TIPO_INT\n    type_boolean : TIPO_BOOLEAN\n    type_string : TIPO_STRING\n    type_double : TIPO_DOUBLE\n    entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES\n    saida : SAIDA ABRE_PARENTESES STRING FECHA_PARENTESES\n             | SAIDA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES\n             | SAIDA ABRE_PARENTESES QUEBRA_LINHA FECHA_PARENTESES\n    codigo   : condicional\n                | atribuicao end\n                | entrada end\n                | saida end\n                | while\n    lista_codigo : codigo PONTO_E_VIRGULA\n                    | empty\n    \n    main : INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM\n    declaracao : type_int VARIAVEL \n                  | type_string VARIAVEL\n                  | type_boolean VARIAVEL\n                  | type_double VARIAVEL\n    atribuicao : type_int VARIAVEL ATRIBUICAO INT\n                  | type_string VARIAVEL ATRIBUICAO STRING\n                  | type_boolean VARIAVEL ATRIBUICAO BOOLEAN\n                  | type_double VARIAVEL ATRIBUICAO DOUBLE\n    comparacao : relacional opLog relacional\n                  | relacional opLog logico\n                  | relacional opLog unario\n                  | logico opLog relacional\n                  | logico opLog logico\n                  | logico opLog unario\n                  | unario opLog unario\n                  | unario opLog relacional\n                  | unario opLog logico\n                  | relacional\n                  | unario\n                  | logico\n    condicional : IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES\n                   | IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES ELSE COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES\n    while : ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES\n    '
    
_lr_action_items = {'$end':([0,1,],[-1,0,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'empty':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> empty","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','main.py',217),
  ('end -> PONTO_E_VIRGULA','end',1,'p_fim_de_instrucao','main.py',221),
  ('valTipo -> TIPO_INT','valTipo',1,'p_valTipo','main.py',225),
  ('valTipo -> TIPO_STRING','valTipo',1,'p_valTipo','main.py',226),
  ('valTipo -> TIPO_BOOLEAN','valTipo',1,'p_valTipo','main.py',227),
  ('valTipo -> TIPO_DOUBLE','valTipo',1,'p_valTipo','main.py',228),
  ('array -> INICIA_COLCHETES valTipo VIRGULA valTipo TERMINA_COLCHETES','array',5,'p_array','main.py',233),
  ('array -> INICIA_COLCHETES valTipo TERMINA_COLCHETES','array',3,'p_array','main.py',234),
  ('matrix -> COMECO_DELIMITADOR_CHAVES array VIRGULA array FINAL_DELIMITADOR_CHAVES','matrix',5,'p_matrix','main.py',238),
  ('matrix -> COMECO_DELIMITADOR_CHAVES array FINAL_DELIMITADOR_CHAVES','matrix',3,'p_matrix','main.py',239),
  ('matrix -> COMECO_DELIMITADOR_CHAVES FINAL_DELIMITADOR_CHAVES','matrix',2,'p_matrix','main.py',240),
  ('conjunto -> VARIAVEL opConj VARIAVEL','conjunto',3,'p_conjunto','main.py',248),
  ('conjunto -> VARIAVEL opConj ARRAY','conjunto',3,'p_conjunto','main.py',249),
  ('conjunto -> ARRAY opConj VARIAVEL','conjunto',3,'p_conjunto','main.py',250),
  ('conjunto -> ARRAY opConj ARRAY','conjunto',3,'p_conjunto','main.py',251),
  ('aritmetica -> VARIAVEL opArit VARIAVEL','aritmetica',3,'p_aritmetica','main.py',255),
  ('aritmetica -> VARIAVEL opArit digitos','aritmetica',3,'p_aritmetica','main.py',256),
  ('aritmetica -> digitos opArit VARIAVEL','aritmetica',3,'p_aritmetica','main.py',257),
  ('aritmetica -> digitos opArit digitos','aritmetica',3,'p_aritmetica','main.py',258),
  ('logico -> VARIAVEL opLog VARIAVEL','logico',3,'p_logico','main.py',262),
  ('logico -> VARIAVEL opLog digitos','logico',3,'p_logico','main.py',263),
  ('logico -> VARIAVEL opLog relacional','logico',3,'p_logico','main.py',264),
  ('logico -> digitos opLog VARIAVEL','logico',3,'p_logico','main.py',265),
  ('logico -> digitos opLog digitos','logico',3,'p_logico','main.py',266),
  ('logico -> digitos opLog relacional','logico',3,'p_logico','main.py',267),
  ('logico -> relacional opLog VARIAVEL','logico',3,'p_logico','main.py',268),
  ('logico -> relacional opLog digitos','logico',3,'p_logico','main.py',269),
  ('logico -> relacional opLog relacional','logico',3,'p_logico','main.py',270),
  ('unario -> opUna VARIAVEL','unario',2,'p_unario','main.py',274),
  ('unario -> opUna digitos','unario',2,'p_unario','main.py',275),
  ('unario -> opUna relacional','unario',2,'p_unario','main.py',276),
  ('unario -> opUna BOOLEAN','unario',2,'p_unario','main.py',277),
  ('unario -> VARIAVEL','unario',1,'p_unario','main.py',278),
  ('unario -> digitos','unario',1,'p_unario','main.py',279),
  ('unario -> relacional','unario',1,'p_unario','main.py',280),
  ('unario -> BOOLEAN','unario',1,'p_unario','main.py',281),
  ('relacional -> VARIAVEL opRel VARIAVEL','relacional',3,'p_relacional','main.py',285),
  ('relacional -> VARIAVEL opRel digitos','relacional',3,'p_relacional','main.py',286),
  ('relacional -> VARIAVEL opRel STRING','relacional',3,'p_relacional','main.py',287),
  ('relacional -> VARIAVEL opRel CHAR','relacional',3,'p_relacional','main.py',288),
  ('relacional -> digitos opRel digitos','relacional',3,'p_relacional','main.py',289),
  ('relacional -> digitos opRel VARIAVEL','relacional',3,'p_relacional','main.py',290),
  ('relacional -> digitos opRel STRING','relacional',3,'p_relacional','main.py',291),
  ('relacional -> digitos opRel CHAR','relacional',3,'p_relacional','main.py',292),
  ('relacional -> STRING opRel STRING','relacional',3,'p_relacional','main.py',293),
  ('relacional -> STRING opRel VARIAVEL','relacional',3,'p_relacional','main.py',294),
  ('relacional -> STRING opRel CHAR','relacional',3,'p_relacional','main.py',295),
  ('relacional -> STRING opRel digitos','relacional',3,'p_relacional','main.py',296),
  ('relacional -> CHAR opRel VARIAVEL','relacional',3,'p_relacional','main.py',297),
  ('relacional -> CHAR opRel digitos','relacional',3,'p_relacional','main.py',298),
  ('relacional -> CHAR opRel STRING','relacional',3,'p_relacional','main.py',299),
  ('relacional -> CHAR opRel CHAR','relacional',3,'p_relacional','main.py',300),
  ('digitos -> INT','digitos',1,'p_digitos','main.py',304),
  ('digitos -> DOUBLE','digitos',1,'p_digitos','main.py',305),
  ('opRel -> IGUAL','opRel',1,'p_opRel','main.py',309),
  ('opRel -> MAIOR_OU_IGUAL','opRel',1,'p_opRel','main.py',310),
  ('opRel -> MENOR_OU_IGUAL','opRel',1,'p_opRel','main.py',311),
  ('opRel -> MAIOR','opRel',1,'p_opRel','main.py',312),
  ('opRel -> MENOR','opRel',1,'p_opRel','main.py',313),
  ('opRel -> DIFERENTE','opRel',1,'p_opRel','main.py',314),
  ('opArit -> SOMA','opArit',1,'p_opArit','main.py',318),
  ('opArit -> SUBTRACAO','opArit',1,'p_opArit','main.py',319),
  ('opArit -> MULTIPLICACAO','opArit',1,'p_opArit','main.py',320),
  ('opArit -> DIVISAO','opArit',1,'p_opArit','main.py',321),
  ('opArit -> MODULO','opArit',1,'p_opArit','main.py',322),
  ('opArit -> PRODUTO_CARTESIANO','opArit',1,'p_opArit','main.py',323),
  ('opLog -> AND','opLog',1,'p_opLog','main.py',327),
  ('opLog -> OR','opLog',1,'p_opLog','main.py',328),
  ('opLog -> DOUBLEAND_BITWISE','opLog',1,'p_opLog','main.py',329),
  ('opLog -> DOUBLEOR_BITWISE','opLog',1,'p_opLog','main.py',330),
  ('opUna -> TILNOT_BITWISE','opUna',1,'p_opUna','main.py',334),
  ('opUna -> NOT','opUna',1,'p_opUna','main.py',335),
  ('opConj -> INTERSECCAO','opConj',1,'p_opConj','main.py',339),
  ('opConj -> UNIAO','opConj',1,'p_opConj','main.py',340),
  ('opConj -> DIFERENCA','opConj',1,'p_opConj','main.py',341),
  ('simbEsp -> PONTO','simbEsp',1,'p_simbEsp','main.py',345),
  ('simbEsp -> VIRGULA','simbEsp',1,'p_simbEsp','main.py',346),
  ('simbEsp -> ABRE_PARENTESES','simbEsp',1,'p_simbEsp','main.py',347),
  ('simbEsp -> FECHA_PARENTESES','simbEsp',1,'p_simbEsp','main.py',348),
  ('simbEsp -> INICIA_COLCHETES','simbEsp',1,'p_simbEsp','main.py',349),
  ('simbEsp -> TERMINA_COLCHETES','simbEsp',1,'p_simbEsp','main.py',350),
  ('simbEsp -> PONTO_E_VIRGULA','simbEsp',1,'p_simbEsp','main.py',351),
  ('comProg -> COMECO_DELIMITADOR_CHAVES','comProg',1,'p_comProg','main.py',355),
  ('comProg -> FINAL_DELIMITADOR_CHAVES','comProg',1,'p_comProg','main.py',356),
  ('bloProg -> INICIO','bloProg',1,'p_bloProg','main.py',360),
  ('bloProg -> FIM','bloProg',1,'p_bloProg','main.py',361),
  ('type_int -> TIPO_INT','type_int',1,'p_type_int','main.py',365),
  ('type_boolean -> TIPO_BOOLEAN','type_boolean',1,'p_type_boolean','main.py',369),
  ('type_string -> TIPO_STRING','type_string',1,'p_type_string','main.py',373),
  ('type_double -> TIPO_DOUBLE','type_double',1,'p_type_double','main.py',377),
  ('entrada -> ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES','entrada',4,'p_entrada','main.py',381),
  ('saida -> SAIDA ABRE_PARENTESES STRING FECHA_PARENTESES','saida',4,'p_saida','main.py',385),
  ('saida -> SAIDA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES','saida',4,'p_saida','main.py',386),
  ('saida -> SAIDA ABRE_PARENTESES QUEBRA_LINHA FECHA_PARENTESES','saida',4,'p_saida','main.py',387),
  ('codigo -> condicional','codigo',1,'p_codigo','main.py',397),
  ('codigo -> atribuicao end','codigo',2,'p_codigo','main.py',398),
  ('codigo -> entrada end','codigo',2,'p_codigo','main.py',399),
  ('codigo -> saida end','codigo',2,'p_codigo','main.py',400),
  ('codigo -> while','codigo',1,'p_codigo','main.py',401),
  ('lista_codigo -> codigo PONTO_E_VIRGULA','lista_codigo',2,'p_lista_codigo','main.py',405),
  ('lista_codigo -> empty','lista_codigo',1,'p_lista_codigo','main.py',406),
  ('main -> INICIO COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES FIM','main',5,'p_main','main.py',412),
  ('declaracao -> type_int VARIAVEL','declaracao',2,'p_declaracao','main.py',416),
  ('declaracao -> type_string VARIAVEL','declaracao',2,'p_declaracao','main.py',417),
  ('declaracao -> type_boolean VARIAVEL','declaracao',2,'p_declaracao','main.py',418),
  ('declaracao -> type_double VARIAVEL','declaracao',2,'p_declaracao','main.py',419),
  ('atribuicao -> type_int VARIAVEL ATRIBUICAO INT','atribuicao',4,'p_atribuicao','main.py',423),
  ('atribuicao -> type_string VARIAVEL ATRIBUICAO STRING','atribuicao',4,'p_atribuicao','main.py',424),
  ('atribuicao -> type_boolean VARIAVEL ATRIBUICAO BOOLEAN','atribuicao',4,'p_atribuicao','main.py',425),
  ('atribuicao -> type_double VARIAVEL ATRIBUICAO DOUBLE','atribuicao',4,'p_atribuicao','main.py',426),
  ('comparacao -> relacional opLog relacional','comparacao',3,'p_comparacao','main.py',430),
  ('comparacao -> relacional opLog logico','comparacao',3,'p_comparacao','main.py',431),
  ('comparacao -> relacional opLog unario','comparacao',3,'p_comparacao','main.py',432),
  ('comparacao -> logico opLog relacional','comparacao',3,'p_comparacao','main.py',433),
  ('comparacao -> logico opLog logico','comparacao',3,'p_comparacao','main.py',434),
  ('comparacao -> logico opLog unario','comparacao',3,'p_comparacao','main.py',435),
  ('comparacao -> unario opLog unario','comparacao',3,'p_comparacao','main.py',436),
  ('comparacao -> unario opLog relacional','comparacao',3,'p_comparacao','main.py',437),
  ('comparacao -> unario opLog logico','comparacao',3,'p_comparacao','main.py',438),
  ('comparacao -> relacional','comparacao',1,'p_comparacao','main.py',439),
  ('comparacao -> unario','comparacao',1,'p_comparacao','main.py',440),
  ('comparacao -> logico','comparacao',1,'p_comparacao','main.py',441),
  ('condicional -> IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES','condicional',7,'p_condicional','main.py',445),
  ('condicional -> IF ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES ELSE COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES','condicional',11,'p_condicional','main.py',446),
  ('while -> ABRE_PARENTESES comparacao FECHA_PARENTESES COMECO_DELIMITADOR_CHAVES lista_codigo FINAL_DELIMITADOR_CHAVES','while',6,'p_while','main.py',450),
]