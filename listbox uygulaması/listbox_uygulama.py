import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo,showwarning

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #set window config
        self.geometry("600x350")
        self.title("ListBox")
        self.resizable(0,0)

        #set lists
        self.create_list()

        #set layout
        self.create_layout()


        #set widget
        self.create_widgets()

        

    def create_list(self):
        self.liste1 = ["Eleman1","Eleman2","Eleman3"]
        self.liste2 = ["Eleman4","Eleman5","Eleman6"]

        self.liste1_var = tk.StringVar(value=self.liste1)
        self.liste2_var = tk.StringVar(value=self.liste2)

    def add_item_1(self):
        if len(self.entry_add_1.get()) == 0:
            showwarning(message="Bilgi Giriniz.")
            self.entry_add_1.focus_set()
            return
        else: 
            self.liste1.append(self.entry_add_1.get())
            self.liste1_var.set(self.liste1)
            self.entry_add_1.delete(0,tk.END)

    def add_item_2(self):
        if len(self.entry_add_2.get()) == 0:
            showwarning(message="Bilgi Giriniz.")
            self.entry_add_2.focus_set()
            return
        else:
            self.liste2.append(self.entry_add_2.get())
            self.liste2_var.set(self.liste2)
            self.entry_add_2.delete(0,tk.END)

    def delete_item_1(self):
        selected_ids = self.listbox_1.curselection()
        selected_values = [self.liste1[i] for i in selected_ids]

        if len(selected_ids) > 0:
            for item in selected_values:
                self.liste1.remove(item)
        
            self.liste1_var.set(self.liste1)
        else:
            showwarning(message="Silmek için bir eleman seçin.")


    def delete_item_2(self):
        selected_ids = self.listbox_2.curselection()
        selected_values = [self.liste2[i] for i in selected_ids]

        if len(selected_ids) > 0:
            for item in selected_values:
                self.liste2.remove(item)
            
            self.liste2_var.set(self.liste2)
        else:
            showwarning(message="Silmek için bir eleman seçiniz.")

    def delete_all_1(self):
        self.liste1.clear()
        self.liste1_var.set(self.liste1)

    def delete_all_2(self):
        self.liste2.clear()
        self.liste2_var.set(self.liste2)

    def item_right(self):
        selected_ids = self.listbox_1.curselection()
        selected_values = [self.liste1[i] for i in selected_ids]

        if(len(selected_ids) > 0):
            for item in selected_values:
                self.liste1.remove(item)
                self.liste2.append(item)
            
            self.liste1_var.set(self.liste1)
            self.liste2_var.set(self.liste2)
        else:
            showwarning(message="Lütfen bir eleman seçiniz.")

    def item_left(self):
        selected_ids = self.listbox_2.curselection()
        selected_values = [self.liste2[i] for i in selected_ids]

        if(len(selected_ids) > 0):
            for item in selected_values:
                self.liste2.remove(item)
                self.liste1.append(item)
            
            self.liste1_var.set(self.liste1)
            self.liste2_var.set(self.liste2)
        else:
            showwarning(message="Lütfen bir eleman seçiniz.")


    def item_right_all(self):
        self.liste2.extend(self.liste1)
        self.liste1.clear()

        self.liste1_var.set(self.liste1)
        self.liste2_var.set(self.liste2)

    def item_left_all(self):
        self.liste1.extend(self.liste2)
        self.liste2.clear()

        self.liste1_var.set(self.liste1)
        self.liste2_var.set(self.liste2)



    







    def create_layout(self):
        main_frame = ttk.Frame(self, padding=50,)
        main_frame.pack()

        self.frame1 = ttk.Frame(main_frame)
        self.frame1.grid(row=0,column=0)

        self.frame2 = ttk.Frame(main_frame)
        self.frame2.grid(row=0,column=1)

        self.frame3 = ttk.Frame(main_frame)
        self.frame3.grid(row=0,column=2)

        main_frame.columnconfigure(0,weight=3)
        main_frame.columnconfigure(1,weight=1)
        main_frame.columnconfigure(2,weight=3)




    def create_widgets(self):
        #FRAME 1
        self.frame1_add_box = ttk.Frame(self.frame1)
        self.frame1_add_box.pack(pady=10)

        self.entry_add_1 = ttk.Entry(self.frame1_add_box,width=15)
        self.entry_add_1.pack(side=tk.LEFT)

        self.btn_add_1 = ttk.Button(self.frame1_add_box,text="+",width=2,command=self.add_item_1)
        self.btn_add_1.pack(side=tk.LEFT)

        self.listbox_1 = tk.Listbox(self.frame1,listvariable=self.liste1_var,selectmode=tk.MULTIPLE)
        self.listbox_1.pack()

        self.frame1_delete_box = ttk.Frame(self.frame1)
        self.frame1_delete_box.pack(pady=10)

        self.btn_delete_1 = ttk.Button(self.frame1_delete_box,text="Sil",command=self.delete_item_1)
        self.btn_delete_1.pack(side=tk.LEFT)

        self.btn_delete_all_1 = ttk.Button(self.frame1_delete_box,text="Hepsini Sil",command=self.delete_all_1)
        self.btn_delete_all_1.pack(side=tk.LEFT)

        

        #FRAME 2
        self.btn_right = ttk.Button(self.frame2,text=">",command=self.item_right)
        self.btn_right.pack()

        self.btn_left = ttk.Button(self.frame2,text="<",command=self.item_left)
        self.btn_left.pack()

        self.btn_right_all = ttk.Button(self.frame2,text=">>",command=self.item_right_all)
        self.btn_right_all.pack()

        self.btn_left_all = ttk.Button(self.frame2,text="<<",command=self.item_left_all)
        self.btn_left_all.pack()

        #FRAME 3
        self.frame3_add_box = ttk.Frame(self.frame3)
        self.frame3_add_box.pack(pady=10)

        self.entry_add_2 = ttk.Entry(self.frame3_add_box,width=15)
        self.entry_add_2.pack(side=tk.LEFT)

        self.btn_add_2 = ttk.Button(self.frame3_add_box,text="+",width=2,command=self.add_item_2)
        self.btn_add_2.pack(side=tk.LEFT)

        self.listbox_2 = tk.Listbox(self.frame3,listvariable=self.liste2_var,selectmode=tk.MULTIPLE)
        self.listbox_2.pack()

        self.frame3_delete_box = ttk.Frame(self.frame3)
        self.frame3_delete_box.pack(pady=10)

        self.btn_delete_2 = ttk.Button(self.frame3_delete_box,text="Sil",command=self.delete_item_2)
        self.btn_delete_2.pack(side=tk.LEFT)

        self.btn_delete_all_2 = ttk.Button(self.frame3_delete_box,text="Hepsini Sil",command=self.delete_all_2)
        self.btn_delete_all_2.pack(side=tk.LEFT)



app = App()
app.mainloop()
