import streamlit as st
import sympy as sp
from relativisticpy import Workbook
from Constants.ExportMarkdown import MarkdownFiles
import openai

passcode = st.text_input("Enter a Open AI api-Key", type="password")

openai.api_key = passcode

w = Workbook()

def key_exists(key, dict):
    """ Get boolean determining whether key exists """
    return bool(dict.get(key))

def openaicall(message):
    model_engine = "gpt-3.5-turbo"
    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{'role' : 'user', 'content' : message}]
    )
    st.write(completions.choices[0].message.content)

def generate_input_field_test(index, radio):
    label = f"Cell {index}"
    placeholder = f"Type your equation {index} here:"
    key = str(index)
    value = st.text_input(label=label, key=key, placeholder=placeholder)
    if key_exists(index, cache):
        if isinstance(cache[index], (sp.Basic, sp.MutableDenseNDimArray, sp.Expr)):
            st.latex(cache[index])
        else:
            st.write(cache[index])
    else:
        if not radio:
            if value:
                st.markdown(MarkdownFiles["EquationOutputStyle"], unsafe_allow_html=True)
                answer = w.expr(value)
                if answer != None:
                    st.latex(sp.latex(answer))
                cache[index] = answer
        else:
            if value:
                openaicall(value)
    return value

def main():
    index = 1
    while True:
        agree = st.checkbox('Open AI', key=str(index) + 'widget')
        value = generate_input_field_test(index, agree)
        if not value:
            break
        index += 1

cache = {}
main()