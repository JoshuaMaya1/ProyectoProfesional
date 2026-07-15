from antlr4 import FileStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener

from ExprLexer import ExprLexer
from ExprParser import ExprParser


class StreamlintErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"[Línea {line}:{column}] {msg}")


def nombre_token(lexer, tipo):
    """Devuelve un nombre legible para el tipo de token sin tronar
    si el índice no existe en symbolicNames/literalNames. No usa
    getVocabulary() porque no todas las versiones del runtime de
    antlr4 lo traen; symbolicNames y literalNames sí siempre existen
    como atributos de la clase generada."""

    simbolicos = lexer.symbolicNames
    literales = lexer.literalNames

    nombre = None

    if 0 <= tipo < len(simbolicos):
        nombre = simbolicos[tipo]

    if (not nombre or nombre == "<INVALID>") and 0 <= tipo < len(literales):
        nombre = literales[tipo]

    if not nombre or nombre == "<INVALID>":
        nombre = f"TIPO_{tipo}"

    return nombre


class StreamlintParserHelper:

    @staticmethod
    def parse(file_path):

        input_stream = FileStream(file_path, encoding="utf-8")

        error_listener = StreamlintErrorListener()

        lexer = ExprLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        token_stream = CommonTokenStream(lexer)

        # ---------- obtener TODOS los tokens ----------
        token_stream.fill()

        lista_tokens = []

        for token in token_stream.tokens:

            if token.type == Token.EOF:
                continue

            lista_tokens.append({
                "Token": nombre_token(lexer, token.type),
                "Lexema": token.text,
                "Línea": token.line,
                "Columna": token.column
            })

        # volver a usar el mismo stream para el parser
        token_stream.seek(0)

        parser = ExprParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.program()

        if error_listener.errors:
            return None, error_listener.errors, lista_tokens, None

        return tree, [], lista_tokens, tree.toStringTree(recog=parser)