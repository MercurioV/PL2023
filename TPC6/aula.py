import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PAROPEN',
    'PARCLOSE'
)
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PAROPEN = r'\('
t_PARCLOSE = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Ilegal caracter {t.value[0]}")
    t.lexer().skip(1)

t_ignore = " \n\t"

lexer = lex.lex()
data = '''
    3 + 4 * 10
    + -20 *2
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)