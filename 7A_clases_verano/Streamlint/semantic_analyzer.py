"""
semantic_analyzer.py
---------------------
Analisis semantico basico sobre el arbol que entrega parser_helper.py.
El arbol sintactico por si solo no sabe si el programa "tiene sentido"
(ver seccion "Reglas semanticas" del informe); aqui se revisan las
reglas que SI se pueden validar sin ejecutar el codigo:

  - Clases duplicadas
  - Herencia de si misma
  - Interfaces duplicadas
  - Atributos duplicados dentro de la misma clase
  - Nombre de constructor distinto al nombre de la clase

Requiere que el proyecto se haya generado con la bandera -visitor:
    antlr4 -Dlanguage=Python3 -visitor Expr.g4
"""

from ExprVisitor import ExprVisitor


class StreamlintSemanticAnalyzer(ExprVisitor):

    def __init__(self):
        self.declared_classes = set()
        self.declared_interfaces = set()
        self.errors = []
        self._clase_actual = None
        self._campos_clase_actual = set()

    # ---------- Clases ----------

    def visitClassDeclaration(self, ctx):
        nombre_clase = ctx.IDENTIFIER().getText()

        if nombre_clase in self.declared_classes:
            self.errors.append(
                f"Error semantico: la clase '{nombre_clase}' ya fue declarada."
            )
        else:
            self.declared_classes.add(nombre_clase)

        if ctx.inheritanceList():
            padres = [n.getText() for n in ctx.inheritanceList().qualifiedName()]
            if nombre_clase in padres:
                self.errors.append(
                    f"Error semantico: la clase '{nombre_clase}' no puede heredar de si misma."
                )

        # guardamos el contexto de la clase actual para validar
        # constructores y atributos, y lo restauramos al salir
        # (soporta anidamiento aunque el lenguaje no lo pida)
        clase_anterior = self._clase_actual
        campos_anteriores = self._campos_clase_actual
        self._clase_actual = nombre_clase
        self._campos_clase_actual = set()

        self.visitChildren(ctx)

        self._clase_actual = clase_anterior
        self._campos_clase_actual = campos_anteriores
        return None

    def visitInterfaceDeclaration(self, ctx):
        nombre_interfaz = ctx.IDENTIFIER().getText()

        if nombre_interfaz in self.declared_interfaces:
            self.errors.append(
                f"Error semantico: la interfaz '{nombre_interfaz}' ya fue declarada."
            )
        else:
            self.declared_interfaces.add(nombre_interfaz)

        return self.visitChildren(ctx)

    # ---------- Miembros ----------

    def visitFieldDeclaration(self, ctx):
        nombre_campo = ctx.IDENTIFIER().getText()

        if nombre_campo in self._campos_clase_actual:
            self.errors.append(
                f"Error semantico: el atributo '{nombre_campo}' ya fue declarado "
                f"en la clase '{self._clase_actual}'."
            )
        else:
            self._campos_clase_actual.add(nombre_campo)

        return self.visitChildren(ctx)

    def visitConstructorDeclaration(self, ctx):
        nombre_constructor = ctx.IDENTIFIER().getText()

        if self._clase_actual and nombre_constructor != self._clase_actual:
            self.errors.append(
                f"Error semantico: el constructor '{nombre_constructor}' debe "
                f"llamarse igual que la clase '{self._clase_actual}'."
            )

        return self.visitChildren(ctx)

    def get_errors(self):
        return self.errors
