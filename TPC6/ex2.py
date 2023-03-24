import ply.lex as lex

tokens = (
    'BOOLEAN',
    'DOUBLE',
    'NUMBER',
    'STRING',
    'OPENBRACKET',
    'CLOSINGBRACKET',
    'COMMA'
)

t_BOOLEAN = r'True|False'
t_DOUBLE = r'-?\d+(\.)\d*'
t_NUMBER = r'-?\d+'
t_OPENBRACKET = r'\['
t_CLOSINGBRACKET = r'\]'
t_COMMA = r'\,'
t_STRING = r'\w+'

t_ignore = " \n\t"

lexer = lex.lex()
data = '[ 1,5, palavra, False ,3.14, 0, fim]'

lexer.input(data)

while tok := lexer.token():
    print(tok)