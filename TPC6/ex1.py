import ply.lex as lex

tokens = (
    'WORD',
    'COMMA',
    'DOT',
    'QUESTIONMARK',
    'EXCLAMATIONMARK'
)

t_WORD = r'([aA-zZ])+'
t_COMMA = r'\,'
t_DOT = r'\.'
t_QUESTIONMARK = r'\¿|\?'
t_EXCLAMATIONMARK = r'\¡|\!'

t_ignore = " \n\t"


lexer = lex.lex()
data = '''
    ¡¿ Hola, me llamo mercu.?!
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)
