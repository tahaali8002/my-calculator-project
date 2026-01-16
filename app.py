import streamlit as st
# This line "imports" the math recipes from your logic.py file
from logic import add, subtract, multiply, divide

st.title("My Robot Calculator 🤖")

# Input Handling: Getting two numbers from the user
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Operation Selection: A dropdown menu
choice = st.selectbox("What math should we do?", ["Addition", "Subtraction", "Multiplication", "Division"])

# Logic Development: Connecting the buttons to the brain
if st.button("Calculate"):
    if choice == "Addition":
        result = add(num1, num2)
    elif choice == "Subtraction":
        result = subtract(num1, num2)
    elif choice == "Multiplication":
        result = multiply(num1, num2)
    elif choice == "Division":
        result = divide(num1, num2)

    # Result Display: Showing the answer clearly
    if isinstance(result, str):
        st.error(result)  # Shows red if there is an error
    else:
        st.success(f"The answer is: {result}") # Shows green for a good answer