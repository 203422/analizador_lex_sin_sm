
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASS DIVIDE DOT IDENTIFIER LBRACE LBRACKET LPAREN MAIN MINUS NUMBER PLUS PUBLIC RBRACE RBRACKET RPAREN SEMICOLON STATIC STRING STRING_LITERAL SYSOUT TIMES VOID\n    program : PUBLIC CLASS IDENTIFIER LBRACE main_method RBRACE\n    \n    main_method : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN process\n    \n    process : LBRACE statements RBRACE\n    statements : statement\n                  | statement statementsstatement : SYSOUT LPAREN expression RPAREN SEMICOLON\n    expression : type_exp\n               | expression PLUS type_exp\n               | expression MINUS type_exp\n               | expression TIMES type_exp\n               | expression DIVIDE type_exp\n    \n    type_exp : STRING_LITERAL\n             | NUMBER\n             | IDENTIFIER\n    '
    
_lr_action_items = {'PUBLIC':([0,5,],[2,6,]),'$end':([1,9,],[0,-1,]),'CLASS':([2,],[3,]),'IDENTIFIER':([3,15,25,32,33,34,35,],[4,16,30,30,30,30,30,]),'LBRACE':([4,17,],[5,19,]),'STATIC':([6,],[8,]),'RBRACE':([7,18,20,21,23,24,36,],[9,-2,23,-4,-3,-5,-6,]),'VOID':([8,],[10,]),'MAIN':([10,],[11,]),'LPAREN':([11,22,],[12,25,]),'STRING':([12,],[13,]),'LBRACKET':([13,],[14,]),'RBRACKET':([14,],[15,]),'RPAREN':([16,26,27,28,29,30,37,38,39,40,],[17,31,-7,-12,-13,-14,-8,-9,-10,-11,]),'SYSOUT':([19,21,36,],[22,22,-6,]),'STRING_LITERAL':([25,32,33,34,35,],[28,28,28,28,28,]),'NUMBER':([25,32,33,34,35,],[29,29,29,29,29,]),'PLUS':([26,27,28,29,30,37,38,39,40,],[32,-7,-12,-13,-14,-8,-9,-10,-11,]),'MINUS':([26,27,28,29,30,37,38,39,40,],[33,-7,-12,-13,-14,-8,-9,-10,-11,]),'TIMES':([26,27,28,29,30,37,38,39,40,],[34,-7,-12,-13,-14,-8,-9,-10,-11,]),'DIVIDE':([26,27,28,29,30,37,38,39,40,],[35,-7,-12,-13,-14,-8,-9,-10,-11,]),'SEMICOLON':([31,],[36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'main_method':([5,],[7,]),'process':([17,],[18,]),'statements':([19,21,],[20,24,]),'statement':([19,21,],[21,21,]),'expression':([25,],[26,]),'type_exp':([25,32,33,34,35,],[27,37,38,39,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PUBLIC CLASS IDENTIFIER LBRACE main_method RBRACE','program',6,'p_program','app.py',84),
  ('main_method -> PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN process','main_method',11,'p_main_method','app.py',90),
  ('process -> LBRACE statements RBRACE','process',3,'p_process','app.py',96),
  ('statements -> statement','statements',1,'p_statements','app.py',101),
  ('statements -> statement statements','statements',2,'p_statements','app.py',102),
  ('statement -> SYSOUT LPAREN expression RPAREN SEMICOLON','statement',5,'p_statement','app.py',109),
  ('expression -> type_exp','expression',1,'p_expression','app.py',114),
  ('expression -> expression PLUS type_exp','expression',3,'p_expression','app.py',115),
  ('expression -> expression MINUS type_exp','expression',3,'p_expression','app.py',116),
  ('expression -> expression TIMES type_exp','expression',3,'p_expression','app.py',117),
  ('expression -> expression DIVIDE type_exp','expression',3,'p_expression','app.py',118),
  ('type_exp -> STRING_LITERAL','type_exp',1,'p_type_exp','app.py',128),
  ('type_exp -> NUMBER','type_exp',1,'p_type_exp','app.py',129),
  ('type_exp -> IDENTIFIER','type_exp',1,'p_type_exp','app.py',130),
]
