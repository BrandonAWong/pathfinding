import tkinter as tk
import pygame

def start_grid(start, end):
    pygame.init()
    pygame.display.set_caption("Grid")
    screen = pygame.display.set_mode((800,400))
    surface = pygame.Surface((20,20))
    surface.fill("White")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # use two loops create row + columns based on row, column turn part of the blocks blue
        screen.blit(surface,(10,10))
        pygame.display.update()
        clock.tick(60)


def click_submit():
    start_entry = start.get()
    end_entry = end.get()       
    if(len(end_entry) > 0 and len(start_entry) > 0):
        root.destroy()
        start_grid(start_entry, end_entry)
    else:
        error = False
        error_label = tk.Label(bottom_frame, fg = "red", text = "Check Input")
        error_label.pack()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady = 5)

bottom_frame = tk.Frame(root, height = 3)
bottom_frame.pack(side = "bottom", pady = 5)

mid_frame = tk.Frame(root)
mid_frame.pack(side = "bottom", pady = 5)

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

