import streamlit as st
from api_calling import note_generator
from PIL import Image

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

    pressed = st.button("Click the button to initiate AI", type="primary")


if pressed:
    if not images:
        st.error("Please upload at least one image to proceed!")
    if not selected_option:
        st.error("Please select a difficulty level to proceed!")

    if images and selected_option:
        # note
        with st.container(border=True):
            st.subheader("Note Summary")
            st.markdown("This is the summary of your notes")

            note_summary = note_generator(images)
            st.markdown(note_summary)

        # Audio trancription
        with st.container(border=True):
            st.subheader("Audio Transcription")
            st.markdown("This is the transcription of your audio")

        # quiz generation
        with st.container(border=True):
            st.subheader(f"Quiz Generation ({selected_option})")
            st.markdown("This is the quiz generated from your notes")