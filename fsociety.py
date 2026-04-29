import tkinter as tk
import random

# ---------------- CONFIG ----------------
PASSWORD = "Fsociety"
FONT = ("Consolas", 14)
BG = "black"
GREEN = "#00ff00"

# ---------------- MATRIX EFFECT ----------------
class MatrixEffect:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.columns = width // 15
        self.drops = [random.randint(0, height) for _ in range(self.columns)]

    def draw(self):
        self.canvas.create_rectangle(
            0, 0, self.width, self.height,
            fill="black", outline="", stipple="gray25"
        )

        for i in range(len(self.drops)):
            x = i * 15
            y = self.drops[i]
            char = str(random.randint(0, 9))
            self.canvas.create_text(x, y, text=char, fill=GREEN, font=FONT)

            if y > self.height and random.random() > 0.97:
                self.drops[i] = 0
            else:
                self.drops[i] += 15

        self.canvas.after(50, self.draw)

# ---------------- MAIN APP ----------------
class FsocietyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FSOCIETY")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg=BG)

        self.canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.matrix = MatrixEffect(self.canvas, root.winfo_screenwidth(), root.winfo_screenheight())
        self.matrix.draw()

        self.login_frame = tk.Frame(root, bg=BG, bd=2, relief="solid")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            self.login_frame,
            text="INGRESE LA CONTRASEÑA",
            fg=GREEN,
            bg=BG,
            font=("Consolas", 16)
        ).pack(padx=20, pady=10)

        self.entry = tk.Entry(
            self.login_frame,
            show="*",
            fg=GREEN,
            bg=BG,
            insertbackground=GREEN,
            font=FONT
        )
        self.entry.pack(padx=20, pady=10)
        self.entry.bind("<Return>", self.check_password)

        tk.Button(
            self.login_frame,
            text="ENTRAR",
            command=self.check_password,
            fg=GREEN,
            bg=BG,
            activebackground=BG,
            activeforeground=GREEN
        ).pack(pady=10)

    def check_password(self, event=None):
        if self.entry.get() == PASSWORD:
            self.login_frame.destroy()
            self.show_welcome()
        else:
            self.entry.delete(0, tk.END)

    def show_welcome(self):
        frame = tk.Frame(self.root, bg=BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="BIENVENIDO",
            fg=GREEN,
            bg=BG,
            font=("Consolas", 28, "bold")
        ).pack(pady=10)

        tk.Label(
            frame,
            text="A los mejores black hat",
            fg=GREEN,
            bg=BG,
            font=("Consolas", 18)
        ).pack(pady=5)

        tk.Label(
            frame,
            text="FSOCIETY",
            fg=GREEN,
            bg=BG,
            font=("Consolas", 22, "bold")
        ).pack(pady=10)

# ---------------- RUN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FsocietyApp(root)
    root.mainloop()
