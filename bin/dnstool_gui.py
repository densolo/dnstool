
import tkinter as tk
from tkinter import filedialog, Menu, Text, END, Label, Entry, Button, NW, N, W
import sys

from dnstool import query_name


class IORedirector(object):
    def __init__(self,text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):
    
    def write(self,str):
        self.text_area.insert(END, str)

    def flush(self):
        pass

    @staticmethod
    def attach_to_text_area(root, textName, inputStr=""):
        import sys
        text = root.nametowidget(textName)
        sys.stdout = StdoutRedirector(text)
        sys.stderr = StdoutRedirector(text)
        text.insert(END, inputStr)


class DnsWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DNS Tool")

        self.configure_form()
        StdoutRedirector.attach_to_text_area(self.root, "output_text_area")


    def configure_textarea(self):
        S = tk.Scrollbar(self.root)
        T = tk.Text(self.root, height=40, width=120)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        return T


    def configure_form(self):
        Label(text="Name:").grid(row=0, column=0)
        Entry(name="name_input", width=30).grid(row=0, column=1, columnspan=2, sticky=W)
        Button(command=self.handle_resolve_button, text="Resolve").grid(row=0, column=3)

        Label(text="Output:").grid(row=1, column=0, sticky=NW)
        S = tk.Scrollbar()
        T = tk.Text(name="output_text_area", height=40, width=120)
        T.grid(row=1, column=1, columnspan=3)
        T.config(yscrollcommand=S.set)

    def handle_resolve_button(self):
        input_widget = self.root.nametowidget("name_input")
        output_widget = self.root.nametowidget("output_text_area")

        name = input_widget.get()
        output_widget.delete('1.0', END)
        if name.strip():
            response = query_name(name.strip())
            print(response.to_text())


def main():    
    window = DnsWindow()
    window.root.mainloop()


if __name__ == '__main__':
    main()
