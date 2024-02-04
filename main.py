from tkinter import *
from datetime import date, datetime
import time 


from lib import * 

root = Tk()
root.title("Digital Clocks")


letter = ("Boulder", 150, "bold")

image_file = PhotoImage(file="images_clock/clock.png")
image = Label(root, image=image_file, bg="#fffffe")
image.place(x=0, y=0)

display = Label(root, font=letter, bg="#a1d18d", fg="#fffffe")
display.place(x=90, y=120)

display_seconds = Label(root, font=("Boulder", 20, "bold"), bg="#a1d18d", fg="#fffffe")
display_seconds.place(x=555, y=320)

display_date = Label(root, font=("Boulder", 12, "bold"), bg="#a1d18d", fg="#fffffe")
display_date.place( x=150, y=320)

div_file = PhotoImage(file="images_clock/div.png")
div = Label(root, image=div_file, bd=0)
div.place(x=341, y=103 )

close_button = Button(root, bg="#223845", activebackground="#223845", cursor="hand2", width=2, bd=0 )
close_button.place(x= 214, y=15)
close_button["command"] = root.destroy


move_button = Button(root, bg="#223845", cursor="hand2", width=1, height=6 )
move_button.place(x= 690, y = 200)

move_window(root, move_button)

def clocks_digital():
    tempo = time.strftime("%H %M")
    display.config(text=tempo)

    current_date = "{} / {} / {}".format(date.today().day, date.today().month, date.today().year)
    display_date.config(text= current_date)
    display_seconds.config(text=current_date)
    
    seconds= time.strftime("%S")
    display_seconds.config(text= seconds)

    root.after(1000, clocks_digital)  

clocks_digital()


width_window = int(root.winfo_screenwidth())
height_window = int(root.winfo_screenheight())

root.geometry("722x435+" + str(int(width_window / 2) - int(722 / 2)) + "+" + str(int(height_window / 2) - int(435 / 2)))

root.overrideredirect(True)
root.wm_attributes("-transparentcolor","#fffffe" ) 

root.mainloop()

