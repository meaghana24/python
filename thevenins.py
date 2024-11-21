import streamlit as st

def compute_thevenins(vth, rth, rl):
    il = vth / (rth + rl)
    pl = il**2 * rl
    return il, pl


st.title("Thevenin's Theorem")

tab1, tab2 = st.tabs(["Compute", "Explain"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            vth = st.number_input("Enter Thevenin Voltage (Vth)", value=10.0)
            rth = st.number_input("Enter Thevenin Resistance (Rth)", value=5.0)
            rl = st.number_input("Enter Load Resistance (Rl)", value=2.5)

    with col2:
        with st.container(border=True):
            il, pl = compute_thevenins(vth, rth, rl)
            st.write("Thevenin's Theorem Results:")
            st.write(f"Load Current (Il) = {il:.2f} A")
            st.write(f"Load Power (Pl) = {pl:.2f} W")

with tab2:
    st.latex(r'''V_{Th} = \frac{V_1R_2}{R_1 + R_2}''')
    st.latex(r'''R_{Th} = \frac{R_1R_2}{R_1 + R_2}''')
    st.write("Thevenin's Theorem states that any two-terminal network composed of voltage sources, current sources, and resistors can be replaced by an equivalent circuit consisting of a voltage source (Thevenin voltage, Vth) and a series resistor (Thevenin resistance, Rth).")
    st.write("The load current (Il) and load power (Pl) can be calculated as:")
    st.latex(r'''I_L = \frac{V_{Th}}{R_{Th} + R_L}''')
    st.latex(r'''P_L = I_L^2R_L''')
    st.write("Where Vth is the Thevenin voltage, Rth is the Thevenin resistance, and Rl is the load resistance.")