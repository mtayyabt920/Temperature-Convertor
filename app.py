import streamlit as st
import convertor as conv
from convertor import celsius_to_farenheit

st.title("🌡️ Convertor App")
temperature = st.number_input("Enter Temperature")

conversion = st.radio("Select Conversion:",[
                      "Celsius -> Fahrenheit",
                      "Fahrenheit -> Celsius",
                      "Kelvin -> Celsius",
                      "Kelvin -> Fahrenheit",
                      "Kelvin -> Celsius",
                      "Kelvin -> Fahrenheit",])

result = None
unit = ""

if conversion == "Celsius -> Fahrenheit":
    result = conv.celsius_to_farenheit(temperature)
    unit = "F"
elif conversion == "Fahrenheit -> Celsius":
    result = conv.farenheit_to_celsius(temperature)
    unit = "C"
elif conversion == "Kelvin -> Celsius":
    result = conv.kelvin_to_celsius(temperature)
    unit = "C"
elif conversion == "Celsius -> Kelvin":
    result = conv.celsius_to_kelvin(temperature)
    unit = "K"
elif conversion == "Fahrenheit -> Kelvin":
    result = conv.farenheit_to_kelvin(temperature)
    unit = "K"
elif conversion == "Kelvin -> Fahrenheit":
    result = conv.kelvin_to_farenheit(temperature)
    unit = "F"

if result is not None:
    st.success(f"Converted Temperature: {result:.2f}")  # shows 37.00 °F

