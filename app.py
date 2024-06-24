from flask import Flask, request, render_template
import ply.lex as lex
import ply.yacc as yacc

app = Flask(__name__)

reserved = {
    'public': 'PUBLIC',
    'class': 'CLASS',
    'static': 'STATIC',
    'void': 'VOID',
    'main': 'MAIN',
    'String': 'STRING'
}

tokens = [
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'STRING_LITERAL',
    'SYSOUT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NUMBER',
    'DOT'
] + list(reserved.values());

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_DOT = r'\.'

def t_SYSOUT(t):
    r'System\.out\.println'
    return t

def t_STRING_LITERAL(t):
    r'\".*?\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.type = 'NUMBER'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


data = '''
    public class HolaMundo {
        public static void main(String[] args) {
            System.out.println("");
        }
    }
    '''


def p_program(p):
    '''
    program : PUBLIC CLASS IDENTIFIER LBRACE main_method RBRACE
    '''
    p[0] = ('program', p[3], p[5])

def p_main_method(p):
    '''
    main_method : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN process
    '''
    p[0] = ('main_method', p[9], p[11])

def p_process(p):
    '''
    process : LBRACE statements RBRACE
    '''
    p[0] = ('process', p[2])

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = ('statements', p[1])
    else:
        p[0] = ('statements', p[1], p[2])

def p_statement(p):
    '''statement : SYSOUT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('statement', p[3])

def p_expression(p):
    '''
    expression : type_exp
               | expression PLUS type_exp
               | expression MINUS type_exp
               | expression TIMES type_exp
               | expression DIVIDE type_exp
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('multiple', p[2], p[1], p[3])

def p_type_exp(p):
    '''
    type_exp : STRING_LITERAL
             | NUMBER
             | IDENTIFIER
    '''

    p[0] = ('type_exp', p[1])

error_message = None

def p_error(p):
    global error_message
    if p:
        error_message = f"Error de sintaxis en '{p.value}'"
    else:
        error_message = "Error de sintaxis: Fin inesperado de entrada"

    raise SyntaxError(error_message)

def analize_code(code):
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer.input(code)
    tokens = []
    global error_message
    error_message = None

    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value, tok.lineno, tok.lexpos))
        result = parser.parse(code)
    except SyntaxError as e:
        error_message = str(e)
        result = None

    return tokens, result



@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    result = None
    if request.method == 'POST':
        code = request.form['code']
        tokens, result = analize_code(code)
    return render_template('index.html', tokens=tokens, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
