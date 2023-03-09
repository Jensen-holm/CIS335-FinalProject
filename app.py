import streamlit as st
import cv2


def main():
    st.title("Webcam Live Feed")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    video_capture = cv2.VideoCapture(0)

    while run:
        _, frame = video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    video_capture.release()


if __name__ == "__main__":
    main()
