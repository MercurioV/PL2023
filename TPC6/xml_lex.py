import ply.lex as lex

states = (
    ("taga", "exclusive"),
    ("tagf", "exclusive")
)

tokens = (
    'ATAG',
    'ATAGF',
    'FTAG',
    'NOME_TAG',
    'VALOR'
)

def t_ATAGF(t):
    r'\</'
    t.lexer.begin('tagf')
    return t

def t_ATAG(t):
    r'\<'
    t.lexer.begin('taga')
    return t

def t_taga_tagf_FTAG(t):
    r'\>'
    t.lexer.begin('INITIAL')
    return t

def t_taga_NOME_TAG(t):
    r'\w+'
    t.lexer.variables.append(t.value)
    return t

def t_tagf_NOME_TAG(t):
    r'\w+'
    if len(t.lexer.variables) == 0:
        print("Erro - nenhuma tag foi aberta!")
    else:
        nt = t.lexer.variables.pop(-1)
        if nt != t.value:
            print(f"Erro - esperado valor {nt}, mas foi lido valor {t.value}")

    return t

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_VALOR(t):
    r'[^<]+'
    return t

t_ANY_ignore = ' \t'



def t_ANY_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.variables = list()

lexer.input("""
<pessoa>
    <nome>Maria</nome>
    <idade>32</idade>
</pessoa>
""")

while tok := lexer.token():
    print(tok)

print(lexer.variables)