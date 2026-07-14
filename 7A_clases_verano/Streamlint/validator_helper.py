"""
validator_helper.py
--------------------
Criterio 4: valida el archivo de entrada ANTES de mandarlo al
analizador lexico/sintactico (parser_helper.py).

Se separo en su propio helper porque son responsabilidades distintas:
  - validator_helper.py -> el archivo es correcto para procesarse
  - parser_helper.py    -> ejecutar ANTLR sobre un archivo ya valido
"""

import os

EXTENSION_VALIDA = ".cs"
TAMANIO_MAXIMO_BYTES = 5 * 1024 * 1024  # 5 MB, evita archivos gigantes por error


class StreamlintValidatorHelper:

    @staticmethod
    def validate_file(file_path: str):
        """
        Regresa (es_valido: bool, mensaje: str). Valida, en orden:
          1. Que el archivo exista y sea un archivo (no carpeta).
          2. Que la extension sea .cs (ver informe, seccion
             "Extension de archivo o forma de escritura").
          3. Que no este vacio.
          4. Que no exceda un tamanio razonable.
          5. Que sea texto legible en UTF-8 (descarta binarios).
        """

        if not os.path.exists(file_path):
            return False, f"El archivo '{file_path}' no existe."

        if not os.path.isfile(file_path):
            return False, f"'{file_path}' no es un archivo."

        _, extension = os.path.splitext(file_path)
        if extension.lower() != EXTENSION_VALIDA:
            return False, (
                f"Extension no permitida: '{extension}'. "
                f"Streamlint solo procesa archivos {EXTENSION_VALIDA}"
            )

        tamanio = os.path.getsize(file_path)
        if tamanio == 0:
            return False, "El archivo esta vacio."

        if tamanio > TAMANIO_MAXIMO_BYTES:
            return False, "El archivo excede el tamanio maximo permitido (5 MB)."

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                f.read()
        except UnicodeDecodeError:
            return False, "El archivo contiene bytes no validos (no es texto UTF-8/.cs)."

        return True, "Archivo valido."
