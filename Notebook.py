import streamlit as st
import sympy as smp
import relativisticpy as rel

st.set_page_config(layout="wide")

pl_holer = """
# ============================================ BLACK HOLE SOLUTION ============================================

Coordinates := [t, r, theta, phi]

# Define the metric tensor components: we define a general spherically symmetric tensor
G_{mu}_{nu} := [[-A(r),0,0,0], [0,B(r),0,0], [0,0,r**2,0], [0,0,0,r**2*sin(theta)**2]]

# Now we have defined the metric above, we can call any individual component of the Ricci tensor itself (as it is metric dependent)
eq0 = Ric_{mu:0}_{nu:0}
eq1 = Ric_{mu:1}_{nu:1}
eq2 = Ric_{mu:2}_{nu:2}

# We construct a simplified equation from the Ricci components as follows
eq5 = (eq0*B(r) + eq1*A(r))*(r*B(r))

# We call the dsolve method which is a differential equation solver
solutionB = dsolve(eq5, B(r)) # returns B(r) = C1/A(r)

# We know the solution of B(r) = C1/A(r) so we substitute it in the third Ricci equation we have available to us
eq6 = simplify(subs(eq2, B(r), C1/A(r)))

# Finally set the answers as A and B
A = dsolve(eq6, A(r))

A

# DOES NOT WORK FROM THIS POINT ON => COMMENTED OUT --- FIX COMMING 

# B = 1/A

# Output the answer as latex, if you wish: (remove latex method if you do not)
# [[-A,0,0,0], [0,B,0,0], [0,0,r**2,0], [0,0,0,r**2*sin(theta)**2]]


# ============================================ K-SCALAR COMPUTATION ============================================

Coordinates := [t, r, theta, phi]
g_{mu}_{nu} := [[-(1 - (2 * G * M) / (c**2*r)), 0, 0, 0],[0, 1 / (1 - (2 * G * M) / (c**2*r)), 0, 0],[0, 0, r**2, 0],[0, 0, 0, r**2 * sin(theta) ** 2]]

Gamma^{a}_{c}_{f} = (1/2)*g^{a}^{b}*(d_{c}*g_{b}_{f} + d_{f}*g_{b}_{c} - d_{b}*g_{c}_{f})

Riemann^{a}_{m}_{b}_{n} = d_{b}*Gamma^{a}_{n}_{m} + Gamma^{a}_{b}_{l}*Gamma^{l}_{n}_{m} - d_{n}*Gamma^{a}_{b}_{m} - Gamma^{a}_{n}_{l}*Gamma^{l}_{b}_{m}

Ricci_{m}_{n} = Riemann^{a}_{m}_{a}_{n}

TempOne^{a}^{f}^{h}^{i} = g^{i}^{d}*(g^{h}^{c}*(g^{f}^{b}*Riemann^{a}_{b}_{c}_{d}))

TempTwo_{a}_{f}_{h}_{i} = g_{a}_{n}*Riemann^{n}_{f}_{h}_{i}

S = TempOne^{a}^{f}^{h}^{i}*TempTwo_{a}_{f}_{h}_{i}

S
"""

def main():
    st.title("RelativisticPy (Beta-Release) Playground")

    # Define a key for the session state
    if 'execute_clicked' not in st.session_state:
        st.session_state.execute_clicked = False


    # Input area for user to type their equation
    user_input = st.text_area("Type code here", height=500, value=pl_holer)

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


