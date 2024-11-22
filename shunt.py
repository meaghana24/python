import streamlit as st

st.title("2305A21L14-PS9")
def Gen_Eff(V,CL,IL,K,Rsh,Ra):

    Ish = V/Rsh
    Ia = K*IL-Ish
    CU_L = Ish**2*Rsh+Ia**2*Ra
    Eff = (K*V*IL)/(K*V*IL+CL+CU_L)*100
    
    return Eff,CU_L
st.sidebar.header("Input Parameters")
    
V = st.sidebar.number_input("Voltage (V)", min_value=1.0, value=220.0)
CL = st.sidebar.number_input("Core Losses (CL) in Watts", min_value=0.0, value=10.0)
IL = st.sidebar.number_input("Full Load Current (IL) in Amps", min_value=0.0, value=10.0)
K = st.sidebar.number_input("Loading on Generator (K)", min_value=0.0, value=1.0)
Rsh = st.sidebar.number_input("Shunt Field Resistance (Rsh)", min_value=1.0, value=100.0)
Ra = st.sidebar.number_input("Armature Resistance (Ra)", min_value=1.0, value=1.5)

    
compute= st.button("compute")
Eff, CU_L = Gen_Eff(V, CL, IL, K, Rsh, Ra)
st.subheader("Results")
st.write(f"Efficiency of DC Shunt Generator: {Eff:.2f}%")
st.write(f"Copper Losses (CU_L): {CU_L:.2f} Watts")