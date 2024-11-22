import streamlit as st

def calculate_efficiency(v_terminal, i_load, v_field, i_field, armature_resistance):
    power_output = v_terminal * i_load
    power_input = (v_terminal + i_load * armature_resistance) * i_load + (v_field * i_field)
    efficiency = (power_output / power_input) * 100
    return power_output, power_input, efficiency

st.title("DC Shunt Generator Efficiency Calculator")

st.markdown('''
This tool calculates the efficiency of a DC shunt generator at various loads. 
Input the terminal voltage, load current, field voltage, field current, and armature resistance.
''')

v_terminal = st.number_input('Enter the terminal voltage (V_terminal) in volts:', min_value=0.0)
i_load = st.number_input('Enter the load current (I_load) in amperes:', min_value=0.0)
v_field = st.number_input('Enter the field voltage (V_field) in volts:', min_value=0.0)
i_field = st.number_input('Enter the field current (I_field) in amperes:', min_value=0.0)
armature_resistance = st.number_input('Enter the armature resistance (Ω):', min_value=0.0)

if st.button('Calculate Efficiency'):
    power_output, power_input, efficiency = calculate_efficiency(v_terminal, i_load, v_field, i_field, armature_resistance)
    st.write(f'Output Power: {power_output:.2f} W')
    st.write(f'Input Power: {power_input:.2f} W')
    st.write(f'Efficiency: {efficiency:.2f} %')