import streamlit as st

from calculator import add, divide, multiply, subtract

st.title("Simple Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

operation = st.selectbox(
    "Choose Operation",
    ["Add", "Subtract", "Multiply", "Divide"],
)

if st.button("Calculate"):

    if operation == "Add":
        result = add(num1, num2)

    elif operation == "Subtract":
        result = subtract(num1, num2)

    elif operation == "Multiply":
        result = multiply(num1, num2)

    else:
        try:
            result = divide(num1, num2)
        except ValueError as e:
            st.error(e)
            st.stop()

    st.success(f"Result = {result}")
