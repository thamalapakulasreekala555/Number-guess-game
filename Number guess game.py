import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess the number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Check", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try a higher number.")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try a lower number.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.secret_number} in {self.attempts} attempts!")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()