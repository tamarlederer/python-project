from tkinter.colorchooser import askcolor
import imageio
import cv2
import numpy as np
from tkinter.simpledialog import askstring

class MyImage:
    def __init__(self, path, nameWindow):
        self.nameWindow = nameWindow
        self.path = path
        self.image = imageio.imread(self.path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        self.image = cv2.resize(self.image, (1000, 600))
        self.show()

    # ------------------עיבודים------------------
    def adjust_brightness(self):
        value = 50
        self.image = np.clip(self.image + value, 0, 255).astype(np.uint8)
        self.show()

    def adjust_contrast(self):
        value = 1.5
        self.image = np.clip((value * (self.image - 127) + 127), 0, 255).astype(np.uint8)
        self.show()

    def add_tint(self):
        color = askcolor()[0]
        if color:
            overlay = np.full(self.image.shape, color, dtype='uint8')
            self.image = cv2.addWeighted(self.image, 0.5, overlay, 0.5, 0)
            self.show()

    def blur_image(self):
        kernel_size = 3
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.show()

    def sharpen_image(self):
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.show()

        # ----------------------------------------

    def show(self):
        cv2.imshow(self.nameWindow, self.image)

    # שינוי גוון בלחיצה ימנית בעכבר
    def change_random_color(self):
        def change_random_color_event(event, x, y, flags, param):
            if event == cv2.EVENT_RBUTTONDOWN and flags & cv2.EVENT_FLAG_RBUTTON:
                red_change = np.random.randint(-50, 50)
                green_change = np.random.randint(-50, 50)
                blue_change = np.random.randint(-50, 50)

                self.image[:, :, 0] = np.clip(self.image[:, :, 0] + red_change, 0, 255)  # Red channel
                self.image[:, :, 1] = np.clip(self.image[:, :, 1] + green_change, 0, 255)  # Green channel
                self.image[:, :, 2] = np.clip(self.image[:, :, 2] + blue_change, 0, 255)  # Blue channel
                self.show()

        cv2.setMouseCallback(self.nameWindow, change_random_color_event)

    # ציור מלבן
    def draw_rec(self):
        def draw_rec_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                cv2.rectangle(self.image, (ix, iy), (x, y), (50, 120, 225), 5)
                self.show()

        cv2.setMouseCallback(self.nameWindow, draw_rec_event)

    # ציור עיגול
    def draw_circ(self):
        def draw_circ_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                self.radius = max(abs(x - ix), abs(y - iy))
                cv2.circle(self.image, (ix, iy), self.radius, (0, 255, 255), 5)
                self.show()

        cv2.setMouseCallback(self.nameWindow, draw_circ_event)

    # ציור קו
    def draw_line(self):
        def draw_line_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                cv2.line(self.image, (ix, iy), (x, y), (0, 200, 0), 5)
                self.show()

        cv2.setMouseCallback(self.nameWindow, draw_line_event)

    # ציור משולש
    def draw_polygon(self):
        def draw_polygon_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                pts = np.array([[ix, iy], [x, y], [ix + (x - ix), iy]], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(self.image, [pts], True, (255, 0, 0), 5)
                self.show()

        cv2.setMouseCallback(self.nameWindow, draw_polygon_event)

    # הוספת טקסט
    def add_text(self):
        text = askstring("Enter Text", "Enter the text you want to add:")
        if text:
            def add_text_event(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(self.image, text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    self.show()
        cv2.setMouseCallback(self.nameWindow, add_text_event)

    # חיתוך תמונה
    def crop_image(self):
        def crop_image_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                self.ix, self.iy = x, y
            elif event == cv2.EVENT_LBUTTONUP:
                cropped_image = self.image[self.iy:y, self.ix:x]
                if cropped_image.shape[0] > 0 and cropped_image.shape[1] > 0:
                    cv2.imshow("Cropped Image", cropped_image)

                self.show()

        cv2.setMouseCallback(self.nameWindow, crop_image_event)

    # שמירת תמונה
    def save_image(self, file_path):
        image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        imageio.imwrite(file_path, image_rgb)
        print("Image saved successfully.")
