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
            System.out.println();
        }
    }
    '''

lexer = lex.lex()

import ply.yacc as yacc

def p_program(p):
    '''
    program : PUBLIC CLASS IDENTIFIER LBRACE main_method RBRACE
    '''
    p[0] = ('program', p[3], p[5])

def p_main_method(p):
    '''
    main_method : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN close
    '''
    p[0] = ('main_method', p[9], p[11])

def p_close(p):
    '''
    close : LBRACE system_out RBRACE
    '''
    p[0] = ('close', p[2])

def p_system_out(p):
    '''
    system_out : SYSOUT LPAREN RPAREN SEMICOLON
    '''
    p[0] = ('system_out',)

def p_error(p):
    print(f"Error de sintaxis {p}")

parser = yacc.yacc()

def analize_code(code):

    lexer.input(code)
    tokens = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value, tok.lineno, tok.lexpos))
    return tokens


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        tokens = analize_code(code)
    return render_template('index.html', tokens = tokens)

if __name__ == '__main__':
    app.run(debug=True)
