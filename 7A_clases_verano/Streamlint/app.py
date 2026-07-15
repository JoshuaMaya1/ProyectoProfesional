"""
app.py
-------
Punto de entrada de Streamlint.

Flujo (Criterio 3 - inyeccion del helper):
    1. validator_helper -> revisa que el archivo sea procesable
    2. parser_helper     -> corre el lexer y el parser de ANTLR
    3. semantic_analyzer -> revisa reglas semanticas basicas
    4. se imprime un reporte

Uso:
    python app.py archivo.cs
"""

import sys

from validator_helper import StreamlintValidatorHelper
from parser_helper import StreamlintParserHelper
from semantic_analyzer import StreamlintSemanticAnalyzer



def main(archivo: str) -> None:
    print("=== Streamlint ===")
    print(f"Analizando: {archivo}\n")

    # 1. Validacion de archivo
    es_valido, mensaje = StreamlintValidatorHelper.validate_file(archivo)
    if not es_valido:
        print(f"[Validacion] {mensaje}")
        print("Analisis abortado.")
        return
    print(f"[Validacion] {mensaje}")

    # 2. Analisis lexico + sintactico
    arbol, errores_sintacticos = StreamlintParserHelper.parse(archivo)

    if errores_sintacticos:
        print("\n[Lexico/Sintactico] Se encontraron errores:")
        for error in errores_sintacticos:
            print(f"  -> {error}")
        return

    print("[Lexico/Sintactico] Sin errores.")

    # 3. Analisis semantico
    analizador = StreamlintSemanticAnalyzer()
    analizador.visit(arbol)
    errores_semanticos = analizador.get_errors()

    if errores_semanticos:
        print("\n[Semantico] Se encontraron errores:")
        for error in errores_semanticos:
            print(f"  -> {error}")
    else:
        print("[Semantico] Sin errores. El codigo es coherente.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python app.py archivo.cs")
        sys.exit(1)

    main(sys.argv[1])
