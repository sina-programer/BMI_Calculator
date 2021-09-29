from tkinter import *
from tkinter import messagebox
import webbrowser
import os

class Indicator:
    def __init__(self, master, text, from_, to, x, y):        
        self.__mean = (from_ + to)/2
        self.__variable = IntVar()
        self.__variable.set(self.__mean)
        
        Label(master, text=text).place(x=x, y=y)
        scale = Scale(master, from_=from_, to=to, variable=self.__variable, orient=HORIZONTAL)
        scale.place(x=x+70, y=y-19)
        scale.bind('<MouseWheel>', lambda event: self.__rolling(event))
                
    def __rolling(self, event):
        current = self.get()
        delta = event.delta
        
        if delta > 0:
            current += 1
            
        else:
            current -= 1
            
        self.__set(current)
        
    def __set(self, value):
        self.__variable.set(value)
        
    def reset(self):
        self.__variable.set(self.__mean)
        
    def get(self):
        return self.__variable.get()


class App:
    def __init__(self, master):
        master.config(menu=self.init_menu(master))
        master.bind('<Escape>', lambda _: self.reset())
        master.bind('<Return>', lambda _: self.calculate())
        
        self.height = Indicator(master, 'Height(cm): ', 130, 210, 15, 20)
        self.weight = Indicator(master, 'Weight(kg): ', 40, 120, 15, 60)
       
        Button(master, text='Calculate', width=24, command=self.calculate).place(x=15, y=100)
        Label(master, text='Your BMI: ').place(x=20, y=140)
        self.bmi_lbl = Label(master)
        self.bmi_lbl.place(x=80, y=140)
        
    def calculate(self):
        height = self.height.get()
        weight = self.weight.get()
        bmi = weight/((height/100)**2)
        self.show_bmi(bmi)
        
    def show_bmi(self, score):
        bins = [(9, '#D1D100', 'Underweight'), (18.5, '#00AA00', 'normal'), 
                (24.9, '#FF6400', 'Overweight'), (29.9, '#EE0000', 'Obesity')]
        
        for bin, color, label in bins:
            if score >= bin:
                self.bmi_lbl.config(text=f'{score:.3f}  {label}', fg=color)
        
    def reset(self):
        self.height.reset()
        self.weight.reset()
        self.bmi_lbl.config(text='')
    
    def show_about(self):
        dialog = Tk()
        dialog.title('About us')
        dialog.geometry('300x100+550+350')
        dialog.resizable(False, False)
        if os.path.exists(icon):
            dialog.iconbitmap(icon)
        dialog.focus_force()
        
        Label(dialog, text='This program made by Sina.f').pack(pady=12)
        Button(dialog, text='GitHub', width=8, command=lambda: webbrowser.open('https://github.com/sina-programer')).place(x=30, y=50)
        Button(dialog, text='Instagram', width=8, command=lambda: webbrowser.open('https://www.instagram.com/sina.programer')).place(x=120, y=50)
        Button(dialog, text='Telegram', width=8, command=lambda: webbrowser.open('https://t.me/sina_programer')).place(x=210, y=50)
        
        dialog.mainloop()
        
    def init_menu(self, master):
        menu = Menu(master)
        menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', help_msg))
        menu.add_command(label='About us', command=self.show_about)

        return menu        
        

help_msg = '''You can calculate your BMI score by this program\n
1_ Set your height by centimeter
2_ Set your weight by Kilogram
3_ Press the calculate button to see your score\n
And you can use of shortcuts
<Enter>  Calculate your BMI score
<Esc>      Reset to default state'''
        
icon = r'files\icon.ico'

if __name__ == "__main__":
    root = Tk()
    root.title('BMI Calculator')
    root.geometry('210x180+550+250')
    root.resizable(False, False)

    if os.path.exists(icon):  
        root.geometry('210x200+550+250')
        root.iconbitmap(icon)
        
    app = App(root)
        
    root.mainloop()
