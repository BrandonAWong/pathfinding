import tkinter as tk
import grid.py

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady = 5)

bottom_frame = tk.Frame(root, height = 3)
bottom_frame.pack(side = "bottom", pady = 5)

mid_frame = tk.Frame(root)
mid_frame.pack(side = "bottom", pady = 5)


def click_submit():
    start_entry = start.get()
    end_entry = end.get()       
    if(len(end_entry) > 0 and len(start_entry) > 0):
        run(start_entry, end_entry)
        root.destroy()

start = tk.Entry(frame, width = 8)
start.pack(side = "left", padx = 6)

start_label = tk.Label(frame, text = "Enter starting point")
start_label.pack(side = "right")

end = tk.Entry(mid_frame, width = 8)
end.pack(side = "left")

end_label = tk.Label(mid_frame, text = "Enter ending point")
end_label.pack(side = "right")

submit_button = tk.Button(bottom_frame,
                        text = "SUBMIT",
                        fg= "green",
                        width = 10,
                        command = click_submit)
submit_button.pack()

root.mainloop()

