import customtkinter
import tkinter as tk
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def open_image():
    """Opens an image file and displays it in a new window."""

    # Open the file dialog to select the image file.
    filename = customtkinter.filedialog.askopenfilename(title="Select Image File...")

    # If the user selected a file, open it and display it.
    if filename:
        # Store the file path in a variable.
        image_file_path = filename

       # Update the file path in a different Python file.
        with open("path/to/file.txt", "r+") as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                if line.startswith("image_file_path =  "):
                    break

                lines[i] = f"image_file_path = {image_file_path}\n"

                f.seek(0)
                f.writelines(lines)

        print(image_file_path)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frame, text="OCR", font=("Arial",24))
lable.pack(pady=12, padx=10)

# Bind the open_image() function to the Open Image button's command option.
button = customtkinter.CTkButton(master=frame, text="Open Image", command=open_image)
button.pack(pady=12, padx=10)

# Start the mainloop.
root.mainloop()
