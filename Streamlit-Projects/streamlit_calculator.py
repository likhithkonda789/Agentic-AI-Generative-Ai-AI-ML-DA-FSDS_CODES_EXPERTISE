import streamlit as st


def calculate(a: float, b: float, operation: str):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    return None


def main():
    st.set_page_config(page_title="Python Calculator", page_icon="🧮")

    st.title("Python Calculator")
    st.write("Simple calculator built with Streamlit.")

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("First number", value=0.0, step=1.0, format="%.4f")
    with col2:
        b = st.number_input("Second number", value=0.0, step=1.0, format="%.4f")

    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        result = calculate(a, b, operation)
        st.subheader("Result")
        st.write(f"**{operation}** of `{a}` and `{b}` is:")
        st.success(result)


if __name__ == "__main__":
    main()

