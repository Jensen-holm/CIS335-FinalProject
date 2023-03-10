from dataclasses import dataclass
import streamlit as st
import cv2


@dataclass
class WebCam:
    on: bool
    face_box: bool

    @property
    def is_on(self) -> bool:
        return self.on

    @property
    def is_face_box(self) -> bool:
        return self.face_box

    def mainloop(self) -> None:
        st.title("Webcam")
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)

        while self.is_on:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)

        camera.release()
