import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform To-Do Manager")

        # Entry field
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task list
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons for delete and mark complete
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Completed", command=self.complete_task)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def complete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            self.task_listbox.insert(tk.END, f"{task} ✔")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
