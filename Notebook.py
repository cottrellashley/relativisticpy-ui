import streamlit as st
import sympy as smp
import relativisticpy as rel

st.set_page_config(layout="wide")

def main():
    st.title("RelativisticPy Code exe")

    # Define a key for the session state
    if 'execute_clicked' not in st.session_state:
        st.session_state.execute_clicked = False


    # Input area for user to type their equation
    user_input = st.text_area("Type code here", height=500)

    if st.button('Execute'):
        # Set the state to indicate the button was clicked
        st.session_state.execute_clicked = True

    # Check if the execute button was clicked
    if st.session_state.execute_clicked:
        workbook = rel.Workbook()
        workbook.reset()
        

        if user_input is not None:
            textsplit = user_input.splitlines()
            text = "\n".join(textsplit)

            result = workbook.expr(text)
        
        if result:
            if not isinstance(result, list):
                latex_result = smp.latex(smp.simplify((result)))
                st.latex(latex_result)
            elif hasattr(result[-1], 'components'):
                if result[-1].scalar:
                    latex_result = smp.latex(smp.simplify(list(result[-1].components)[0]))
                    st.latex(latex_result)
                else:
                    latex_result = smp.latex(smp.simplify(result[-1].components))
                    st.latex(latex_result)
            else:
                latex_result = smp.latex(smp.simplify(result[-1]))
                st.latex(latex_result)
        else:
            st.text("No output generated.")

        # Reset the state after processing
        st.session_state.execute_clicked = False

        # Optional: You can also clear the text area after processing
        user_input = ""

if __name__ == "__main__":
    main()


