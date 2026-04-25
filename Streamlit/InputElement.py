import streamlit as st

st.title("Input Your Information", anchor=False)
st.divider()

name = st.text_input("Enter your name")

st.write("Your name is: ", name)

st.divider()

# age = st.number_input("Enter your age")
age = st.number_input("Enter your age", value=None, placeholder="Type your age")

# print(type(age))

st.write("Your age is: ", age)

st.divider()

password = st.text_input("Enter your password", type="password")

st.write("Your password is: ", password)

# pressed = st.button("Enter to confirm")
pressed = st.button("Enter to confirm", type="primary")

if pressed:
    st.write(f"Your name is {name} and your age is {age}")

# selected = st.selectbox("Choose your profession", ("Student", "Employee", "Businessman"))
# selected = st.selectbox("Choose your profession", ("Student", "Employee", "Businessman"), index=None)
selected = st.selectbox("Choose your profession", ("Student", "Employee", "Businessman"), index=None, accept_new_options=True)

# print(type(selected))
st.write("You selected ", selected)