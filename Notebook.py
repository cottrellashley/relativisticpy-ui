import streamlit as st
import sympy as smp
import relativisticpy as rel
from relativisticpy.symengine import Basic

st.set_page_config(layout="wide")

pl_holer_ = """

Coordinates := [ t, r, theta, phi ]
g_{mu}_{nu} := [
                    [-(1 - (2 * G * M) / (c**2*r)), 0, 0, 0],
                    [0, 1 / (1 - (2 * G * M) / (c**2*r)), 0, 0],
                    [0, 0, r**2, 0],
                    [0, 0, 0, r**2 * sin(theta) ** 2]
                ]

Gamma^{a}_{c}_{f} := (1/2)*g^{a}^{b}*(d_{c}*g_{b}_{f} + d_{f}*g_{b}_{c} - d_{b}*g_{c}_{f})

Riemann^{a}_{m}_{b}_{n} := d_{b}*Gamma^{a}_{n}_{m} + Gamma^{a}_{b}_{l}*Gamma^{l}_{n}_{m} - d_{n}*Gamma^{a}_{b}_{m} - Gamma^{a}_{n}_{l}*Gamma^{l}_{b}_{m}

Ricci_{m}_{n} := Riemann^{a}_{m}_{a}_{n}

TempOne^{a}^{f}^{h}^{i} := g^{i}^{g}*(g^{h}^{c}*(g^{f}^{b}*Riemann^{a}_{b}_{c}_{g}))

TempTwo_{a}_{f}_{h}_{i} := g_{a}_{n}*Riemann^{n}_{f}_{h}_{i}

S := TempOne^{a}^{f}^{h}^{i}*TempTwo_{a}_{f}_{h}_{i}

simplify(S)

"""

def main(pl_holer):
    st.title("RelativisticPy (Beta-Release) Playground")

    # Define a key for the session state
    if 'execute_clicked' not in st.session_state:
        st.session_state.execute_clicked = False


    # Input area for user to type their equation
    user_input = st.text_area("Type code here", height=500, value=pl_holer)

    if st.button('Execute'):
        # Set the state to indicate the button was clicked
        st.session_state.execute_clicked = True

    tick = st.checkbox(label="Display Latex")

    # Check if the execute button was clicked
    if st.session_state.execute_clicked:
        workbook = rel.Workbook()
        workbook.reset()
        

        if user_input is not None:
            textsplit = user_input.splitlines()
            text = "\n".join(textsplit)
            result = workbook.expr(text)

        # Split the screen into 2 columns for Output1 and Output2
        col1, col2 = st.columns(2)

        # Output1 on the left
        with col1:
            st.write('##### Latex Output')
            if tick:
                st.latex(text)

        # Output2 on the right
        with col2:
            st.write('##### Computed Output')
            if result != None:
                if hasattr(result, 'components'):
                    latex_result = smp.latex(result.components)
                    st.latex(latex_result)
                elif isinstance(result, Basic):
                    latex_result = smp.latex(result)
                    st.latex(latex_result)
                elif isinstance(result, list):
                    latex_result = smp.latex(result[-1])
                    st.latex(latex_result)
                elif isinstance(result, Basic):
                    error_message = result
                    st.error(body=error_message, icon="🚨")
            else:
                st.text("No output generated.")

            # Reset the state after processing
            st.session_state.execute_clicked = False

            # Optional: You can also clear the text area after processing
            user_input = ""

if __name__ == "__main__":
    main(pl_holer_)

