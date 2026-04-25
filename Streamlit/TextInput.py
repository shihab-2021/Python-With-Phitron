import streamlit as st

# st.write("Hello World")
# st.title("My first Streamlit web app")
st.title("My first Streamlit web app", anchor=False)
st.header("Content 1", divider=True)
st.subheader("Content 1 Subheader")
st.text("Hello World")

st.markdown(":red[**Hello**] *world*")
st.markdown(":green[**Hello**] *world*")
st.markdown(":red-background[:green[**Hello**] *world*]")

