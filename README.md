# CompilerConstruction
Interview assignment for compiler costruction


The given grammar contains tokens, x (NAME), n (INTEGER) and literals +,-,*,/,=. It also consists of a reserved word 'print'.
At the lex stage of the interpreter, the input string is divided into corresponding tokens.
The lexer filters tokens with defined regular expressions and functions. Also, the x (NAME) is required to be an identifier and also not be any reserved word in the grammar.
After the lex stage, the interpreter enters into yacc stage where parsing takes place. The given grammar has been made unambiguous to assist in LR Shift Reduce Parsing.
