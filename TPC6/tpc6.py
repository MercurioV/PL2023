import ply.lex as lex

states = (
    ("assigment", "exclusive"),
    ("program", "exclusive"),
    ("condition", "exclusive"),
)

tokens = (
    'LINECOMMENT',
    'MULTILINECOMMENT',
    'TYPE',
    'VARIABLENAME',
    'PUNTOCOMA',
    'FUNCTION',
    'FUNCTIONNAME',
    'ASSIGMENT',
    'VALUE',
    'CONDITIONAL',
    'PARAMETER',
    'CONDITION',
    'OPENBRACKET',
    'PROGRAM',
    'PROGRAMNAME',
    'IN',
    'FOR',
    'RANGE',
    'CLOSEBRACKET',
    'MULTIPLICATION',
    'SUM',
    'SUB',
    'DIVISION',
    'COMA',
    'ARRAY_TYPE_VARIABLE',
    'ARRAY',
    'ARRAY_ELEMENT_VALUE'
)
def t_ignore_LINECOMMENT(t):
    r'//(.)*(\n)?'

def t_ignore_MULTILINECOMMENT(t):
    r'(/\*)(.|\n|\r)*(\*\/)'

def t_FUNCTION(t):
    r'function'
    return t

def t_FOR(t):
    r'for'
    return t

def t_PROGRAM(t):
    r'program'
    t.lexer.begin('program')
    return t

def t_TYPE(t):
    r'int|string|double|boolean'
    return t

def t_ARRAY_TYPE_VARIABLE(t):
    r'[aA-zZ]+\[\d+\]'
    return t

def t_assigment_ARRAY_ELEMENT_VALUE(t):
    r'[aA-zZ]+\[\w+\]'
    return t

def t_assigment_ARRAY(t):
    r'\{(\d+\,|\d+)+\}'
    return t

def t_IN(t):
    r'in'
    return t

def t_RANGE(t):
    r'\[\d+..\d+\]'
    return t

def t_CONDITIONAL(t):
    r'while|if|else|elif'
    t.lexer.begin('condition')
    return t

def t_condition_PARAMETER(t):
    r'([aA-zZ]+|\d+)'
    return t

def t_condition_CONDITION(t):
    r'\<|\>|=='
    return t

def t_ANY_ASSIGMENT(t):
    r'='
    t.lexer.begin('assigment')
    return t

def t_assigment_VALUE(t):
    r'\d+|\w+'
    return t

def t_assigment_MULTIPLICATION(t):
    r'\*'
    return t

def t_assigment_SUM(t):
    r'\+'
    return t

def t_assigment_SUB(t):
    r'\-'
    return t

def t_assigment_DIVISION(t):
    r'\/'
    return t

def t_ANY_FUNCTIONNAME(t):
    r'([aA-zZ]+)\(.+\)'
    return t

def t_program_PROGRAMNAME(t):
    r'[aA-zZ]+'
    return t

def t_VARIABLENAME(t):
    r'[aA-zZ]+'
    return t

def t_ANY_PUNTOCOMA(t):
    r'\;'
    t.lexer.begin('INITIAL')
    return t

def t_ANY_COMA(t):
    r'\,'
    t.lexer.begin('INITIAL')
    return t

def t_ANY_OPENBRACKET(t):
    r'\{'
    t.lexer.begin('INITIAL')
    return t

def t_CLOSEBRACKET(t):
    r'\}'
    return t

t_ANY_ignore = " \n\t"

def t_ANY_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.variables = list()

lexer.input("""
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
""")

while tok := lexer.token():
    print(tok)
