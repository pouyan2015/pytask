import tkinter as tk

root = tk.Tk()
root.title("pytasks")
root.geometry("500x400")
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)
def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop() 