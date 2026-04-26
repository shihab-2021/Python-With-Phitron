import streamlit as st

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    if images:
        if len(images)>3:
            st.error("Upaload at max 3 images!")
        else:
            st.subheader("Uploaded Images")

            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    # difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    if selected_option:
        st.markdown(f"You selected **{selected_option}** as dificulty of your quiz")
    else:
        st.error("You must select a difficulity!")

    pressed = st.button("Click the button to initiate AI", type="primary")