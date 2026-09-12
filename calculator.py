import tkinter as tk
import math

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title('Calculator')
root.configure(bg="#0F1115")

frame_bottom = tk.Frame(root,borderwidth=5,relief=tk.GROOVE,bg="#0F1115")
frame_bottom.place(x=0, y=0, relwidth=1, relheight=1)

frame_bottom.columnconfigure((0, 1, 2, 3), weight=1)
frame_bottom.rowconfigure(0, weight=3)
frame_bottom.rowconfigure((1, 2, 3, 4, 5), weight=1)
frame_bottom.rowconfigure(6, weight=1)

frame_center = tk.Frame(frame_bottom,borderwidth=5,relief=tk.GROOVE,bg="#171D27")
frame_center.grid(column=0,row=0,columnspan=4,sticky="nsew",padx=10,pady=10)

button_AC = tk.Button(frame_bottom, text="AC", bg="red", fg="white",font=('Arial', 15))
button_AC.grid(column=0, row=1, sticky="nsew", padx=10, pady=10)

button_Delet = tk.Button(frame_bottom, text="⌫", bg="#464A4F", fg="white", font=('Arial', 15))
button_Delet.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")

button_dar = tk.Button(frame_bottom, text="%", bg="#464A4F", fg="white", font=('Arial', 15))
button_dar.grid(column=2, row=1, padx=10, pady=10, sticky="nsew")

button_jazr = tk.Button(frame_bottom, text="√", bg="#464A4F", fg="white", font=('Arial', 15))
button_jazr.grid(column=3, row=1, padx=10, pady=10, sticky="nsew")

button_7 = tk.Button(frame_bottom, text="7", bg="#171D27", fg="white", font=('Arial', 15))
button_7.grid(column=0, row=2, padx=10, pady=10, sticky="nsew")

button_8 = tk.Button(frame_bottom, text="8", bg="#171D27", fg="white", font=('Arial', 15))
button_8.grid(column=1, row=2, padx=10, pady=10, sticky="nsew")

button_9 = tk.Button(frame_bottom, text="9", bg="#171D27", fg="white", font=('Arial', 15))
button_9.grid(column=2, row=2, padx=10, pady=10, sticky="nsew")

button_tag = tk.Button(frame_bottom, text="÷", bg="orange", fg="white", font=('Arial', 15))
button_tag.grid(column=3, row=2, padx=10, pady=10, sticky="nsew")

button_4 = tk.Button(frame_bottom, text="4", bg="#171D27", fg="white", font=('Arial', 15))
button_4.grid(column=0, row=3, padx=10, pady=10, sticky="nsew")

button_5 = tk.Button(frame_bottom, text="5", bg="#171D27", fg="white", font=('Arial', 15))
button_5.grid(column=1, row=3, padx=10, pady=10, sticky="nsew")

button_6 = tk.Button(frame_bottom, text="6", bg="#171D27", fg="white", font=('Arial', 15))
button_6.grid(column=2, row=3, padx=10, pady=10, sticky="nsew")

button_zarb = tk.Button(frame_bottom, text="×", bg="orange", fg="white", font=('Arial', 15))
button_zarb.grid(column=3, row=3, padx=10, pady=10, sticky="nsew")

button_1 = tk.Button(frame_bottom, text="1", bg="#171D27", fg="white", font=('Arial', 15))
button_1.grid(column=0, row=4, padx=10, pady=10, sticky="nsew")

button_2 = tk.Button(frame_bottom, text="2", bg="#171D27", fg="white", font=('Arial', 15))
button_2.grid(column=1, row=4, padx=10, pady=10, sticky="nsew")

button_3 = tk.Button(frame_bottom, text="3", bg="#171D27", fg="white", font=('Arial', 15))
button_3.grid(column=2, row=4, padx=10, pady=10, sticky="nsew")

button_menha = tk.Button(frame_bottom, text="-", bg="orange", fg="white", font=('Arial', 15))
button_menha.grid(column=3, row=4, padx=10, pady=10, sticky="nsew")

button_0 = tk.Button(frame_bottom, text="0", bg="#171D27", fg="white", font=('Arial', 15))
button_0.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky="nsew")

button_dat = tk.Button(frame_bottom, text=".", bg="#171D27", fg="white", font=('Arial', 15))
button_dat.grid(column=2, row=5, padx=10, pady=10, sticky="nsew")

button_plus = tk.Button(frame_bottom, text="+", bg="orange", fg="white", font=('Arial', 15))
button_plus.grid(column=3, row=5, padx=10, pady=10, sticky="nsew")

button_mos = tk.Button(frame_bottom, text="=", bg="blue", fg="white", font=('Arial', 15))
button_mos.grid(column=0, row=6, columnspan=4, sticky="nsew", padx=10, pady=10)

label_input = tk.Label(frame_center,bg="#171D27",fg="white",font=('Arial', 20))
label_input.place(x=1030, y=130, anchor="e")

label_result = tk.Label(frame_center,bg="#171D27",fg="gray",font=('Arial', 10))
label_result.place(relx=0.98, rely=0.75, anchor="e")

def click(value):
    text = label_input.cget("text")

    if value == "AC":
        label_input.config(text="")
        label_result.config(text="")

    elif value == "⌫":
        label_input.config(text=text[:-1])

    elif value == "=":
        try:
            result = eval(text.replace("×", "*").replace("÷", "/"))
            label_result.config(text=str(result))
        except:
            label_result.config(text="Error")

    elif value == "%":
        try:
            label_result.config(text=str(float(text) / 100))
        except:
            label_result.config(text="Error")

    elif value == "√":
        try:
            label_result.config(text=str(math.sqrt(float(text))))
        except:
            label_result.config(text="Error")

    else:
        label_input.config(text=text + value)

buttons = {button_AC: "AC",button_Delet: "⌫",button_dar: "%",button_jazr: "√",button_7: "7",button_8: "8",button_9: "9",button_tag: "÷",button_4: "4",button_5: "5",button_6: "6",button_zarb: "×",button_1: "1",button_2: "2",button_3: "3",button_menha: "-",button_0: "0",button_dat: ".",button_plus: "+",button_mos: "="}

for button, value in buttons.items():
    button.config(command=lambda value=value: click(value))

root.mainloop()
