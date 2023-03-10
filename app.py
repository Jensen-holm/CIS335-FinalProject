from cam.cam import WebCam


def main():
    return WebCam(
        on=True,
        face_box=True
    ).mainloop()


if __name__ == "__main__":
    main()
