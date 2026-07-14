"""
parser_helper.py
------------------
Criterio 3: helper del analizador sintactico para Streamlint.
Se encarga UNICAMENTE de correr ANTLR (lexer + parser) sobre un
archivo ya validado y regresar el arbol sintactico.

La validacion del archivo (extension, existencia, contenido) vive
en validator_helper.py -- este modulo no valida nada, solo parsea.

Requiere que ExprLexer.py y ExprParser.py ya esten generados con:
    antlr4 -Dlanguage=Python3 -visitor Expr.g4
"""

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from ExprLexer import ExprLexer
from ExprParser import ExprParser


class StreamlintErrorListener(ErrorListener):
    """Junta los errores lexicos y sintacticos que ANTLR va reportando,
    en vez de solo imprimirlos en consola, para poder mostrarlos
    despues de forma ordenada desde app.py."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"[Linea {line}:{column}] {msg}")


class StreamlintParserHelper:

    @staticmethod
    def parse(file_path: str):
        """
        Ejecuta el analisis lexico y sintactico de un archivo .cs
        usando el lexer/parser generados por ANTLR a partir de Expr.g4.

        Regresa una tupla (arbol, errores):
          - arbol: nodo raiz (ProgramContext) o None si hubo errores
          - errores: lista de strings con los errores encontrados
        """
        input_stream = FileStream(file_path, encoding="utf-8")

        error_listener = StreamlintErrorListener()

        lexer = ExprLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        token_stream = CommonTokenStream(lexer)

        parser = ExprParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.program()

        if error_listener.errors:
            return None, error_listener.errors

        return tree, []
