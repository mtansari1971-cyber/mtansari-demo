import streamlit as st


st.title("Streamlit Calculator")
st.write("A simple calculator built with Streamlit.")

# User inputs
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

operation = st.selectbox(
    "Select an operation",
    (
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Power (^)",
        "Modulus (%)"
    )
)


if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("Not allowed.")
            st.stop()
        result = num1 / num2

    elif operation == "Power (^)":
        result = num1 ** num2

    elif operation == "Modulus (%)":
        if num2 == 0:
            st.error("Cannot perform modulus by zero.")
            st.stop()
        result = num1 % num2

    st.success(f"Result: {result}")

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    "This calculator is built using Streamlit.\n\n"
    "Features:\n"
    "- Addition\n"
    "- Subtraction\n"
    "- Multiplication\n"
    "- Division\n"
    "- Power\n"
    "- Modulus"
)