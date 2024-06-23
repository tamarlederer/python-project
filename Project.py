from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import im


class MyWindow:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("800x600+200+100")
        self.win.title("My project")
        self.img = None
        self.selected_shape = ''
        self.processing = ''
        background_image = Image.open("תמונה2.jpg")
        background_photo = ImageTk.PhotoImage(background_image)

        # הוספת רקע כתמונה
        background_label = Label(self.win, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # הגדרת איקונים לכפתורים
        icon_image = Image.open("upload_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon1 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("crop_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon2 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("text_fields_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon3 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("category_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon4 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("save_as_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon5 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("exit_to_app_24dp_FILL0_wght400_GRAD0_opsz24.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon6 = ImageTk.PhotoImage(icon_image)
        # הגדרת כפתורים
        self.btn1 = Button(self.win, text="     add image      ", relief="raised", bg='black', fg='white',
                           command=self.open_file_dialog,
                           image=self.icon1, compound=LEFT)
        self.btn2 = Button(self.win, text="         crop image             ", bg='black', fg='white', image=self.icon2,
                           compound=LEFT, command=self.crop_image)
        self.btn3 = Button(self.win, text="  add text to the image           ", bg='black', fg='white',
                           image=self.icon3,
                           compound=LEFT, command=self.text)
        self.btn4 = Button(self.win, text="       add a shape to the image         ", bg='black', fg='white',
                           image=self.icon4,
                           compound=LEFT, command=self.draw)
        self.btn5 = Button(self.win, text="                      save as                                   ",
                           bg='black', fg='white', image=self.icon5, compound=LEFT)
        self.btn6 = Button(self.win,
                           text="                             exit                                            ",
                           bg='black', fg='white', image=self.icon6, compound=LEFT)
        # הגדרת כפתורי צורות
        self.circle_btn = Button(self.win, text="Circle", bg='aqua', command=lambda: self.set_shape("circle"))
        self.polygon_btn = Button(self.win, text="Polygon", bg='aqua', command=lambda: self.set_shape("polygon"))
        self.line_btn = Button(self.win, text="Line", bg='aqua', command=lambda: self.set_shape("line"))
        self.triangle_btn = Button(self.win, text="Triangle", bg='aqua', command=lambda: self.set_shape("triangle"))
        # הגדרת כפתורי עיבוד
        self.adjust_brightness = Button(self.win, text="adjust_brightness", bg='purple',
                                        command=lambda: self.set_processing("adjust_brightness"))
        self.adjust_contrast = Button(self.win, text="adjust_contrast", bg='purple',
                                      command=lambda: self.set_processing("adjust_contrast"))
        self.add_tint = Button(self.win, text="add_tint", bg='purple', command=lambda: self.set_processing("add_tint"))
        self.blur_image = Button(self.win, text="blur_image", bg='purple',
                                 command=lambda: self.set_processing("blur_image"))
        self.sharpen_image = Button(self.win, text="sharpen_image", bg='purple',
                                    command=lambda: self.set_processing("sharpen_image"))

        self.positions()
        self.win.mainloop()

    # בחירת צורה
    def set_shape(self, shape):
        self.selected_shape = shape
        if self.selected_shape == "circle":
            self.img.draw_circ()
        elif self.selected_shape == "polygon":
            self.img.draw_polygon()
        elif self.selected_shape == "line":
            self.img.draw_line()
        elif self.selected_shape == "triangle":
            self.img.draw_rec()
        else:
            print("No shape selected.")

    # בחירת עיבוד
    def set_processing(self, processing):
        self.processing = processing
        if self.processing == "adjust_brightness":
            self.img.adjust_brightness()
        elif self.processing == "adjust_contrast":
            self.img.adjust_contrast()
        elif self.processing == "add_tint":
            self.img.add_tint()
        elif self.processing == "blur_image":
            self.img.blur_image()
        elif self.processing == "sharpen_image":
            self.img.sharpen_image()
        else:
            print("No shape processing.")

    # קביעת מיקומים
    def positions(self):
        self.btn1.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.btn2.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.btn3.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.btn4.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.btn5.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.btn6.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.btn6.config(command=self.close_window)
        self.btn5.config(command=self.save_image)

    # העלאת תמונה
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        print("Selected file:", file_path)
        self.img = im.MyImage(file_path, "image")
        self.img.change_random_color()

        self.adjust_brightness.grid(row=2, column=0)
        self.adjust_contrast.grid(row=4, column=0)
        self.add_tint.grid(row=6, column=0)
        self.blur_image.grid(row=8, column=0)
        self.sharpen_image.grid(row=10, column=0)

    # ------------------עיבודים----------------------

    def adjust_brightness(self):
        if self.image:
            value = simpledialog.askinteger("Input", "Enter brightness value (-100 to 100):", minvalue=-100,
                                            maxvalue=100)
            if value is not None:
                self.image.adjust_brightness(value)
        else:
            messagebox.showerror("Error", "No image loaded!")

    def adjust_contrast(self):
        if self.image:
            value = simpledialog.askfloat("Input", "Enter contrast value (1.0 to 3.0):", minvalue=1.0, maxvalue=3.0)
            if value is not None:
                self.image.adjust_contrast(value)
        else:
            messagebox.showerror("Error", "No image loaded!")

    def add_tint(self):
        if self.image:
            self.image.add_tint()
        else:
            messagebox.showerror("Error", "No image loaded!")

    def blur_image(self):
        if self.image:
            value = simpledialog.askinteger("Input", "Enter kernel size (odd number, e.g., 3, 5, 7):", minvalue=1)
            if value is not None and value % 2 != 0:
                self.image.blur_image(value)
            else:
                messagebox.showerror("Error", "Kernel size must be an odd number!")
        else:
            messagebox.showerror("Error", "No image loaded!")

    def sharpen_image(self):
        if self.image:
            self.image.sharpen_image()
        else:
            messagebox.showerror("Error", "No image loaded!")

    # --------------------------------------

    # הגדרת מיקומי כפתורי צורה
    def draw(self):
        self.circle_btn.grid(row=2, column=6)
        self.polygon_btn.grid(row=4, column=6)
        self.line_btn.grid(row=6, column=6)
        self.triangle_btn.grid(row=8, column=6)

    # הוספת טקסט
    def text(self):
        self.img.add_text()

    # חיתוך תמונה
    def crop_image(self):
        self.img.crop_image()

    # שמירת תמונה
    def save_image(self):
        if self.img is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.img.save_image(file_path)
                print("Image saved successfully.")
            else:
                print("Save operation canceled.")
        else:
            print("No image loaded.")

    # סגירת החלונית
    def close_window(self):
        self.win.destroy()


m = MyWindow()
