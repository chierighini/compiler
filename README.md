# compiler

A "compiler" written in python for educational purposes

## Language rules

1. Lines should end with a `;`
2. Blocks should be delimited by `{}`
3. Reserved words: `if, else, for, while`
4. Operators: `+,-,*,/,=,++,&&,||,!` 

Esse documento deve servir como guia para produzir a especificação do projeto de compilador, o qual poderá (deverá) ser atualizado no andamento do semestre. Para a primeira entrega, os elementos esperados são:

1. Informações gerais (nome da linguagem criada/adaptada, nome da linguagem usada para o compilador, nome da linguagem destino)

- A linguagem criada é uma linguagem baseada em C (ponto e vírgula para terminar linhas, colchetes para delimitar blocos, etc)
- A linguagem usada no compilador é python
- A linguagem de destino será python

2. Descrição do problema a ser tratado como exemplo entre origem e destino (nome do algoritmo e duas implementações: linguagem de origem e destino)

- Algoritmo de Dijkstra

3. Funcionalidades da linguagem de origem, quando criada ou adaptada

- Variáveis (atribuição, alteração e leitura) e constantes (atribuição e leitura);
- Operadores aritméticos (+,-,*,/)
- Instruções condicionais e blocos de repetição (if, else-if, else, for, break, continue);
- Não inclui recursos de orientação a objeto;
- Não inclui construção de funções e suporte a recursão.

4. Especificação das regras para obtenção dos símbolos léxicos

- Os símbolos são obtidos fazendo a separação por espaços de cada elemento na linha.
- Quase todas as tags são geradas a partir do código, utilizando as palavras reservadas, colocadas num dicionário a partir do arquivo `reserved.json`.
- A tag [VALUE] é utilizada para valores numéricos.
- A tag [VARIABLE] é utilizada quando nenhum dos casos acima são verdadeiros.

5. Representação léxica atual do problema na linguagem de origem

```['VARIABLE', 'OPERATOR', 'VALUE', 'LINE_END', 'VARIABLE', 'OPERATOR', 'VALUE', 'LINE_END', 'VARIABLE', 'OPERATOR', 'VALUE', 'DELIM', 'VARIABLE', 'OPERATOR', 'VALUE', 'RES_WORD', 'VARIABLE', 'OPERATOR', 'VALUE', 'DELIM', 'VARIABLE', 'OPERATOR', 'VALUE', 'LINE_END', 'DELIM', 'DELIM']```

