import tkinter as tk
from datetime import datetime

class TemplateApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Template App")

        # Create the text entry widget and pack it to the left side of the window
        self.text_entry = tk.Text(self.root)
        self.text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the options frame and pack it to the right side of the window
        self.options_frame = tk.Frame(self.root, width=200, bg="gray")
        self.options_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Create the Add button and pack it to the top of the options frame
        self.add_button = tk.Button(self.options_frame, text="Add", command=self.add_text)
        self.add_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create the Load button and pack it below the Add button
        self.load_button = tk.Button(self.options_frame, text="Load", command=self.load_text)
        self.load_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create the List button and pack it below the Load button
        self.list_button = tk.Button(self.options_frame, text="List", command=self.list_text)
        self.list_button.pack(side=tk.TOP, padx=10, pady=10)

    def add_text(self):
        # Get the current date and time in the format YYYY-MM-DD HH:MM
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

        # Get the text from the text entry widget
        text = self.text_entry.get('1.0', tk.END).strip()

        # Append the text and date to the file
        with open('text_file.txt', 'a') as f:
            f.write(f'{current_time} | {text}\n')

    def load_text(self):
        # TODO: Add functionality to load text into the text entry widget
        pass

    def list_text(self):
        # Read the contents of the text file
        with open('text_file.txt', 'r') as f:
            contents = f.readlines()

        # Create a new window to display the contents
        list_window = tk.Toplevel()
        list_window.title("List of Text Entries")

        # Create a listbox widget and pack it to the left side of the window
        listbox = tk.Listbox(list_window)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar widget and pack it to the right side of the window
        scrollbar = tk.Scrollbar(list_window, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link the scrollbar and listbox together
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Add the contents of the file to the listbox
        for line in contents:
            listbox.insert(tk.END, line)

    def run(self):
        self.root.mainloop()

# Create an instance of the TemplateApp class and run the app
app = TemplateApp()
app.run()
