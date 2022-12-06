# Compiladores-DiscreMath

Construção de um analisador léxico e sintático utilizando Python Lex-Yacc (PLY) para segunda nota da disciplina de Compiladores (ECOM06) da Universidade Federal de Itajubá (UNIFEI).

## O que é DiscreMath?

É uma linguagem de programação voltada para operações de matemática discreta e álgebra relacional, como seleção e projeção, oferecendo também suporte para operações de conjuntos, como união, interseção e diferença.

## Requisitos Mínimos e Instalação

Nossa linguagem foi criada e testada utilizando:
 - Python 3.10 (verifique a versão no prompt de comando).
 ```bash
python --version
```

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os requisitos.
- Ply 3.11
- Biblioteca numpy 1.22.3
- Biblioteca pandas 1.4.2
```bash
pip install -r requirements.txt
```

## Utilização

Clone este repositório e, para utilizar a linguagem, por favor escreva os programas com extensão `.dmath` na mesma pasta em que estiver o arquivo `discremath.exe`, que é o executável do compilador.

Caso possua uma versão diferente do Python daquela mencionada:
- Rode o comando para instalar o auto-py-to-exe
```bash
pip install auto-py-to-exe
```
- No terminal, execute o comando
```bash
auto-py-to-exe
```
- Irá abrir uma interface gráfica, você deve escolher o caminho do arquivo `discremath.py` e pedir para convertê-lo em `.exe`
- 
- Será gerado o `.exe` dentro da pasta output criada pelo programa. Basta copiar o arquivo para a pasta onde estará seus programas `.dmath`

## Execução

- Primeira maneira:
Para rodar um programa escrito na linguagem DiscreMath você pode usar diretamente:
```bash
discremath {nome_programa}.dmath
```

- Segunda maneira:
Se houver problemas com o compilador `.exe`, você pode compilar os seus programas `.dmath` assim:
```bash
python sintatica.py {nome_programa}.dmath
```
```bash
python {nome_programa}.py
```

## <img src="https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/30/000000/external-developer-coding-kiranshastry-lineal-color-kiranshastry-1.png"/> Time
* Camila Motta Renó (<img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> https://github.com/kcami)
* Stéfany Coura Coimbra (<img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> https://github.com/stefanycoimbra)
* Ytalo Ysmaicon Gomes (<img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> https://github.com/ysmaicon)
