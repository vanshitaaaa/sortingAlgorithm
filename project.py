from tkinter import*
from tkinter import ttk
import random
from sorting import*
import tkinter.font as font

root = Tk()
root.title("Algorithm Visualizer")
root.geometry("800x1000")
root.config( bg = 'LavenderBlush3')

select_Algo = StringVar()
arr = []

def Creating_Array():
    global arr
    low = int(Lower_Limit.get())
    high = int(Upper_Limit.get())
    size = int(Array_Size.get())
    arr =[]
    for i in range(size):
        arr.append(random.randrange(low , high+1))
        
    drawrectangle(arr, ['purple' for x in range(len(arr))]) 

        
def drawrectangle(arr , Arraycolor):
    Canvas1.delete("all")
    Canvas_width = 600
    Canvas_height = 500
    rectangle_width = (Canvas_width / (len(arr)+1))
    border_1 = 200
    spacing = 15
    for i, height in enumerate(arr):
       x0 = (i*rectangle_width) + border_1 + spacing
       y0 = Canvas_height - (height*10)
       x1 = ((i+1)*rectangle_width) + border_1
       y1 = Canvas_height
       Canvas1.create_rectangle(x0,y0,x1,y1, fill = Arraycolor[i])
       Canvas1.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))

    root.update_idletasks()

    

def sorting(value):
    global arr
    if value == "Bubble Sort":
        Bubble_Sort(arr, drawrectangle, Sorting_speed.get())
    elif value == "Selection Sort":
        Selection_Sort(arr, drawrectangle, Sorting_speed.get())
        

Frame1 = Frame(root, width = 1000, height= 350, bg = 'pink' , padx =20, pady = 20,borderwidth=3, relief="raised")
Frame1.grid(row = 0 , column = 0, padx = 400 , pady = 20)
Canvas1 = Canvas(root , width= 1000 , height = 750 , bg = 'pink',borderwidth=3, relief="sunken")
Canvas1.grid(row =1 , column = 0 , padx= 200 , pady = 10)

Choose_Algo = ttk.Combobox(Frame1, width = 15 , textvariable = select_Algo, values = ['Bubble Sort'  , 'Selection Sort'])
Choose_Algo.grid( row = 0 , column = 0,padx = 5, pady =5)
Choose_Algo.current(0)

Sorting_speed = Scale (Frame1 , orient = HORIZONTAL , from_ = 0.1 , to = 2.0,relief="raised" , label = "Sorting Speed",troughcolor ='white', resolution = 0.2 , length=100)
Sorting_speed.grid(row = 0 , column = 1, padx =5 , pady =5)

Lower_Limit = Scale (Frame1 , orient = HORIZONTAL , from_ = 1 , to = 20,relief="raised" , label = "Lower Limit",troughcolor ='white', resolution = 1 , length=100)
Lower_Limit.grid(row = 1 , column = 0, padx =5 , pady =5)

Upper_Limit = Scale (Frame1 , orient = HORIZONTAL , from_ = 20 , to = 100,relief="raised" , label = "Upper Limit",troughcolor ='white', resolution = 1 , length=100)
Upper_Limit.grid(row = 1 , column = 1, padx =5 , pady =5)

Array_Size = Scale (Frame1 , orient = HORIZONTAL , from_ = 5 , to = 30,relief="raised" , label = "Array Size",troughcolor ='white', resolution = 1 , length=100)
Array_Size.grid(row = 1 , column = 2, padx =5 , pady =5)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

Create_Array = Button( Frame1 , text = "CREATE ARRAY", bg ='white'  , font=buttonFont ,height = 7,width= 17,relief="raised" ,activebackground = 'LavenderBlush3', activeforeground ='white',command = Creating_Array )
Create_Array.grid(row = 0 , column = 3, padx = 5 , pady =2)

Sort_start = Button( Frame1 , text = "SORT !" , bg ='white' ,height = 7,width= 17 ,font=buttonFont, relief="raised",activebackground = 'LavenderBlush3', activeforeground ='white', command = lambda: sorting(select_Algo.get()))
Sort_start.grid(row = 1 , column = 3, padx= 5, pady = 2)








root.mainloop()


 
