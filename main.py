import tkinter as tk
from tkinter import Label, Entry, Frame, RIDGE, Button
import qrcode
from PIL import ImageTk
from resizeimage import resizeimage


class QR_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False, True)

        title = Label(
            self.root,
            text="QR Code Generator",
            font=("Times New Roman", 40),
            bg="#053246",
            fg="white",
            anchor="w",
        )
        title.place(x=0, y=0, relwidth=1)

        self.var_emp_code = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_department = tk.StringVar()
        self.var_designation = tk.StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_Frame.place(x=50, y=100, width=500, height=380)

        emp_title = Label(
            emp_Frame,
            text="Employee Details",
            font=("goudy oldstyle", 20),
            bg="#053246",
            fg="white",
            anchor="w",
        )
        emp_title.place(x=0, y=0, relwidth=1)

        labels = ["Employee ID", "Name", "Department", "Designation"]
        entries = [
            self.var_emp_code,
            self.var_name,
            self.var_department,
            self.var_designation,
        ]

        for i in range(len(labels)):
            label = Label(
                emp_Frame,
                text=labels[i],
                font=("Times New Roman", 15, "bold"),
                bg="white",
            )
            label.place(x=20, y=60 + i * 40)

            entry = Entry(
                emp_Frame,
                font=("Times New Roman", 15),
                textvariable=entries[i],
                bg="lightyellow",
            )
            entry.place(x=200, y=60 + i * 40)

        btn_generate = Button(
            emp_Frame,
            text="QR Generate",
            command=self.generate,
            font=("Times New Roman", 18, "bold"),
            bg="#2196f3",
            fg="white",
        )
        btn_generate.place(x=90, y=250, width=200, height=30)

        btn_clear = Button(
            emp_Frame,
            text="Clear",
            font=("Times New Roman", 18, "bold"),
            bg="#607d8b",
            fg="white",
            command=self.clear_fields,
        )
        btn_clear.place(x=300, y=250, width=120, height=30)

        self.msg = ""
        self.lbl_msg = Label(
            emp_Frame,
            text=self.msg,
            font=("Times New Roman", 20),
            bg="white",
            fg="green",
        )
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=600, y=100, width=250, height=380)

        qr_title = Label(
            qr_Frame,
            text="Employee QR Code",
            font=("goudy oldstyle", 20),
            bg="#053246",
            fg="white",
            anchor="w",
        )
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(
            qr_Frame,
            text="No QR Available",
            font=("Times New Roman", 15),
            bg="#3f51b5",
            fg="white",
            bd=1,
            relief=RIDGE,
        )
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def generate(self):
        if any(
            [
                self.var_designation.get() == "",
                self.var_emp_code.get() == "",
                self.var_department.get() == "",
                self.var_name.get() == "",
            ]
        ):
            self.msg = "All Fields are Required!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (
                f"Employee ID: {self.var_emp_code.get()}\n"
                f"Employee Name: {self.var_name.get()}\n"
                f"Department: {self.var_department.get()}\n"
                f"Designation: {self.var_designation.get()}"
            )
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save(f"Employee_QR/Emp_{self.var_emp_code.get()}.png")

            self.qr_image = ImageTk.PhotoImage(
                file=f"Employee_QR/Emp_{self.var_emp_code.get()}.png"
            )
            self.qr_code.config(image=self.qr_image)

            self.msg = "QR Generated Successfully!!"
            self.lbl_msg.config(text=self.msg, fg="green")

    def clear_fields(self):
        self.var_emp_code.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        self.msg = ""
        self.lbl_msg.config(text=self.msg, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    obj = QR_Generator(root)
    root.mainloop()
