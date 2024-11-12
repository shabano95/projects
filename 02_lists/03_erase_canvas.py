import tkinter as tk

class EraserCanvas:
    def __init__(self, master, canvas_width, canvas_height, cell_size):
        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.cell_size = cell_size
        
        # Create the canvas
        self.canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # Create the grid of blue cells
        self.grid = []
        for row in range(0, canvas_height, cell_size):
            grid_row = []
            for col in range(0, canvas_width, cell_size):
                rect = self.canvas.create_rectangle(col, row, col + cell_size, row + cell_size, fill="blue")
                grid_row.append(rect)
            self.grid.append(grid_row)

        # Create the eraser (a small rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, cell_size, cell_size, fill="white", outline="black")
        
        # Bind mouse events to control eraser movement
        self.canvas.bind("<B1-Motion>", self.move_eraser)
        self.canvas.bind("<ButtonRelease-1>", self.clear_eraser)

    def move_eraser(self, event):
        # Get the position of the mouse pointer
        x = event.x // self.cell_size * self.cell_size
        y = event.y // self.cell_size * self.cell_size

        # Move the eraser to the new position
        self.canvas.coords(self.eraser, x, y, x + self.cell_size, y + self.cell_size)

        # Erase cells by changing their color to white
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        # Get the coordinates of the top-left corner of the eraser
        row = y // self.cell_size
        col = x // self.cell_size
        
        # Check the cells that are covered by the eraser and set them to white
        for i in range(row, row + 1):
            for j in range(col, col + 1):
                self.canvas.itemconfig(self.grid[i][j], fill="white")

    def clear_eraser(self, event):
        # Optional: Reset the eraser to its original size
        self.canvas.coords(self.eraser, 0, 0, self.cell_size, self.cell_size)

# Create the Tkinter window
root = tk.Tk()

# Set up the canvas dimensions and cell size
canvas_width = 400
canvas_height = 400
cell_size = 40

# Create the EraserCanvas instance
eraser_canvas = EraserCanvas(root, canvas_width, canvas_height, cell_size)

# Start the Tkinter event loop
root.mainloop()
