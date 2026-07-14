grammar Expr;


program
    : usingDirective* typeDeclaration* EOF
    ;

usingDirective
    : USING qualifiedName ';'
    ;

qualifiedName
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

typeDeclaration
    : classDeclaration
    | interfaceDeclaration
    ;

/* ---------- Clases, herencia, interfaces, clases abstractas ---------- */

classDeclaration
    : accessModifier? classModifier? CLASS IDENTIFIER inheritanceList? classBody
    ;

classModifier
    : ABSTRACT
    | SEALED
    | STATIC
    ;

inheritanceList
    : ':' qualifiedName (',' qualifiedName)*
    ;

classBody
    : '{' classMember* '}'
    ;

classMember
    : fieldDeclaration
    | constructorDeclaration
    | methodDeclaration
    ;

interfaceDeclaration
    : accessModifier? INTERFACE IDENTIFIER inheritanceList? interfaceBody
    ;

interfaceBody
    : '{' interfaceMember* '}'
    ;

interfaceMember
    : type IDENTIFIER '(' parameterList? ')' ';'
    ;

/* ---------- Atributos, constructores, metodos ---------- */

fieldDeclaration
    : accessModifier? fieldModifier* type IDENTIFIER ('=' expression)? ';'
    ;

fieldModifier
    : STATIC
    | READONLY
    | CONST
    ;

constructorDeclaration
    : accessModifier? IDENTIFIER '(' parameterList? ')' block
    ;

methodDeclaration
    : accessModifier? methodModifier* type IDENTIFIER '(' parameterList? ')' (block | ';')
    ;

methodModifier
    : STATIC
    | VIRTUAL
    | OVERRIDE
    | ABSTRACT
    ;

accessModifier
    : PUBLIC
    | PRIVATE
    | PROTECTED
    | INTERNAL
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : type IDENTIFIER
    ;

type
    : INT_T | FLOAT_T | DOUBLE_T | DECIMAL_T | BOOL_T | STRING_T | CHAR_T | VOID_T | OBJECT_T
    | IDENTIFIER
    ;

/* ---------- Bloques, instrucciones, control de flujo ---------- */

block
    : '{' statement* '}'
    ;

statement
    : localVariableDeclaration
    | assignmentStatement
    | ifStatement
    | forStatement
    | whileStatement
    | switchStatement
    | tryCatchStatement
    | returnStatement
    | expressionStatement
    ;

localVariableDeclaration
    : variableDeclarator ';'
    ;

variableDeclarator
    : type IDENTIFIER ('=' expression)?
    ;

assignmentStatement
    : (IDENTIFIER | memberAccessTarget) assignmentOperator expression ';'
    ;

memberAccessTarget
    : IDENTIFIER ('.' IDENTIFIER)+
    ;

assignmentOperator
    : '=' | '+=' | '-=' | '*=' | '/=' | '%='
    ;

ifStatement
    : IF '(' expression ')' (block | statement) (ELSE (block | statement))?
    ;

forStatement
    : FOR '(' forInit? ';' expression? ';' forUpdate? ')' (block | statement)
    ;

forInit
    : variableDeclarator
    | IDENTIFIER assignmentOperator expression
    ;

forUpdate
    : IDENTIFIER ('++' | '--')
    | IDENTIFIER assignmentOperator expression
    ;

whileStatement
    : WHILE '(' expression ')' (block | statement)
    ;

switchStatement
    : SWITCH '(' expression ')' '{' switchCase* defaultCase? '}'
    ;

switchCase
    : CASE literal ':' statement* BREAK ';'
    ;

defaultCase
    : DEFAULT ':' statement* BREAK ';'
    ;

tryCatchStatement
    : TRY block catchClause+ finallyClause?
    ;

catchClause
    : CATCH '(' type IDENTIFIER ')' block
    ;

finallyClause
    : FINALLY block
    ;

returnStatement
    : RETURN expression? ';'
    ;

expressionStatement
    : expression ';'
    ;

/* ---------- Expresiones, instanciacion de objetos, excepciones ----------
   El orden de las alternativas = precedencia (la primera listada liga
   mas fuerte). Sigue el mismo orden que usa C#:
   acceso a miembros > unario (!) > * / % > + - > relacionales
   > igualdad > && > || */

expression
    : NEW IDENTIFIER '(' argumentList? ')'              # newObject
    | THROW NEW IDENTIFIER '(' argumentList? ')'        # throwException
    | expression '.' IDENTIFIER '(' argumentList? ')'   # methodCall
    | expression '.' IDENTIFIER                         # memberAccess
    | '!' expression                                     # logicalNot
    | expression ('*' | '/' | '%') expression           # mulDiv
    | expression ('+' | '-') expression                 # addSub
    | expression ('<' | '>' | '<=' | '>=') expression    # relational
    | expression ('==' | '!=') expression                # equality
    | expression '&&' expression                        # logicalAnd
    | expression '||' expression                        # logicalOr
    | '(' expression ')'                                 # parens
    | literal                                            # literalExpr
    | IDENTIFIER                                         # variableExpr
    ;

argumentList
    : expression (',' expression)*
    ;

literal
    : INT
    | FLOAT
    | STRING
    | CHAR
    | BOOL
    | NULL_LIT
    ;

/* ============================================================
   REGLAS LEXICAS (lexer rules - MAYUSCULA)
   ============================================================ */

// Palabras clave de estructura y modificadores
CLASS       : 'class';
INTERFACE   : 'interface';
ABSTRACT    : 'abstract';
SEALED      : 'sealed';
STATIC      : 'static';
READONLY    : 'readonly';
CONST       : 'const';
VIRTUAL     : 'virtual';
OVERRIDE    : 'override';
PUBLIC      : 'public';
PRIVATE     : 'private';
PROTECTED   : 'protected';
INTERNAL    : 'internal';
NEW         : 'new';
USING       : 'using';

// Control de flujo
IF          : 'if';
ELSE        : 'else';
FOR         : 'for';
WHILE       : 'while';
SWITCH      : 'switch';
CASE        : 'case';
DEFAULT     : 'default';
BREAK       : 'break';
RETURN      : 'return';

// Excepciones
TRY         : 'try';
CATCH       : 'catch';
FINALLY     : 'finally';
THROW       : 'throw';

// Tipos primitivos
INT_T       : 'int';
FLOAT_T     : 'float';
DOUBLE_T    : 'double';
DECIMAL_T   : 'decimal';
BOOL_T      : 'bool';
STRING_T    : 'string';
CHAR_T      : 'char';
VOID_T      : 'void';
OBJECT_T    : 'object';
NULL_LIT    : 'null';

// Literales
BOOL        : 'true' | 'false';
FLOAT       : [0-9]+ '.' [0-9]+;
INT         : [0-9]+;
STRING      : '"' ( '\\' . | ~["\\\r\n] )* '"';
CHAR        : '\'' ( '\\' . | ~['\\] ) '\'';

// Identificadores (deben ir despues de las palabras clave)
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios en blanco y comentarios (se descartan, criterio de la investigacion)
WS              : [ \t\r\n]+ -> skip;
LINE_COMMENT    : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip;
