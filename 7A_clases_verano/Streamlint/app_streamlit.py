import os
import tempfile

import streamlit as st

from validator_helper import StreamlintValidatorHelper
from parser_helper import StreamlintParserHelper
from semantic_analyzer import StreamlintSemanticAnalyzer


st.set_page_config(
    page_title="Streamlint",
    layout="wide"
)

st.title("Streamlint")
st.write("Analizador Léxico, Sintáctico y Semántico para C#")

archivo = st.file_uploader(
    "Selecciona un archivo",
    type=["cs"]
)

if archivo:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".cs") as tmp:
        tmp.write(archivo.read())
        ruta = tmp.name

    try:
        # ===== Información del archivo =====
        st.subheader("Información del archivo")
        st.write("Nombre:", archivo.name)
        st.write("Tamaño:", archivo.size, "bytes")

        valido, mensaje = StreamlintValidatorHelper.validate_file(ruta)

        if not valido:
            st.error(mensaje)

        else:
            st.success(mensaje)

            # ===== Código fuente =====
            st.subheader("Código fuente")

            with open(ruta, "r", encoding="utf-8") as f:
                codigo = f.read()

            st.code(codigo, language="csharp")

            # ===== Parsing (léxico + sintáctico en una sola pasada) =====
            arbol, errores, tokens, arbol_texto = StreamlintParserHelper.parse(ruta)

            # ===== Análisis Léxico =====
            st.subheader("Análisis Léxico")

            if tokens:
                st.dataframe(tokens, width="stretch")
            else:
                st.warning("No se encontraron tokens.")

            # ===== Análisis Sintáctico =====
            st.subheader("Análisis Sintáctico")

            if errores:
                for e in errores:
                    st.error(e)

            else:
                st.success("Sin errores sintácticos")
                st.text(arbol_texto)

                # ===== Análisis Semántico =====
                st.subheader("Análisis Semántico")

                analizador = StreamlintSemanticAnalyzer()
                analizador.visit(arbol)
                errores_sem = analizador.get_errors()

                if errores_sem:
                    st.dataframe(errores_sem, width="stretch")
                else:
                    st.success("Sin errores semánticos")

    finally:
        os.remove(ruta)