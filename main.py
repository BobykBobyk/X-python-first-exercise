from customtkinter import *
from PIL import Image
import customtkinter
from tkinter import messagebox

app = customtkinter.CTk()
app.geometry('1200x600')
app.title('Washmachine')
set_appearance_mode('dark')

img_washmachine = Image.open('static/fotos/washmachine.png')

list0=[]
list_1_modus = ['Cotton', 'Synthetics', 'Delicate', 'Quick wash']
list_2_poroshki = ['Ariel', 'Persil', 'Lenor', 'Frosh', 'No.']
list_2_losioni = ['Ariel F', 'Persil F', 'Lenor F', 'Frosh F', 'No.']
list_3_clothingupper = ['Sweater', 'Pants', 'Jacket', 'Hat', 'No']
list_4_clothinglower = ['Underwear', 'T-Shirt', 'Socks', 'Gloves', 'No']
list_5_clothing = ['Yes', 'No']

dict_1_list = {'Cotton': '1h', 'Synthetics': '2,5 h', 'Delicate': '1,25 h', 'Quick wash': '0,5 h',
 'Ariel': 'Powerful', 'Persil': 'Reliable', 'Lenor': 'Fragrant', 'Frosh': 'Vibrant', 'No.':' ',
 'Ariel F': 'Refreshing', 'Persil F': 'Nourishing', 'Lenor F': 'Soothing', 'Frosh F': 'Invigorating',
 'Sweater': '3', 'Pants': '2.5', 'Jacket': '4', 'Hat': '0.5', 'No': '0',
 'Underwear': '0.3', 'T-Shirt': '0.5', 'Socks': '0.2', 'Gloves': '0.2',
 'Yes': '5', 'No': '0'}

list_describing = []
text_for_label = ""

def get_all_data(choice):
    if len(list0) > 5:
        messagebox.showerror("Too many things choosed", "You can choose all things \n only 1 time, 6 times in sum")
        list0.clear()
    else:
        list0.append(choice)
    print(list0)

def load_all_data():
    global list_describing
    list_describing = []
    list0_new = list0

    for i in list0_new:
        list_describing.append(dict_1_list[i])

    print(list_describing)

def show_all_data():
    global list_describing, text_for_label
    list0.clear()
    print(list0)

    if len(list_describing) < 6:
        messagebox.showerror("Incomplete data", "Please choose all items before showing data.")
        return

    time = list_describing[0]
    a1 = list_describing[1]
    a2 = list_describing[2]
    weight = float(list_describing[3]) + float(list_describing[4]) + float(list_describing[5])

    text_for_label = f"Time: {time} \n Clothing is {a1}, {a2} \n The weight of the washed clothing: {weight}"
    print(text_for_label)

    label_results.configure(text=text_for_label)

#-----------------------------------------------------------------------------------------------------------------------

frame1_modus = customtkinter.CTkFrame(master=app, fg_color='#8D6F3A', border_color='#FFCC70', border_width=2, width=300)
frame1_modus.pack(expand=True)
frame1_modus.place(x=10, y=10)

label1_modus = customtkinter.CTkLabel(master=frame1_modus, text='Choose your wash modus')
label1_modus.place(x=20, y=10)

combobox0_modus = CTkComboBox(master = frame1_modus, values = list_1_modus, command=get_all_data)
combobox0_modus.place(x=20, y= 40)

label11_modus = customtkinter.CTkLabel(master=frame1_modus, text='Every wash modus has own Washtime!')
label11_modus.place(x=20, y=170)

#-----------------------------------------------------------------------
frame2_poroshki = CTkFrame(master = app, fg_color='#6396BD', border_color = '#8AD4DC', border_width=2, width=300, height= 120)
frame2_poroshki.pack(expand=True)
frame2_poroshki.place(x=10, y=225)

label2_poroshki = CTkLabel(master = frame2_poroshki, text = 'Choose your Detergent and Liquid Detergent')
label2_poroshki.place(x=20, y=10)

combobox1_poroshki = CTkComboBox(master = frame2_poroshki, values = list_2_poroshki, command=get_all_data)
combobox1_poroshki.place(x=20, y= 40)

combobox2_losioni = CTkComboBox(master = frame2_poroshki, values = list_2_losioni , command=get_all_data)
combobox2_losioni.place(x=20, y=70)

#-----------------------------------------------------------------------------------------------------------------------

frame3_clothing = CTkFrame(master = app, fg_color='#7BBD63', border_color = '#72FF3F', border_width=2, width=300, height= 160)
frame3_clothing.pack(expand=True)
frame3_clothing.place(x=10, y=360)

label3_clothing = CTkLabel(master = frame3_clothing, text = 'Choose your upper-, lowwerclothing and others')
label3_clothing.place(x=20, y=20)

combobox1_clothing_upper = CTkComboBox(master = frame3_clothing, values= list_3_clothingupper, command=get_all_data)

combobox1_clothing_upper.place(x=20, y=50)

combobox2_clothing_lowwer = CTkComboBox(master = frame3_clothing, values= list_4_clothinglower, command=get_all_data)

combobox2_clothing_lowwer.place(x=20, y=80)

combobox3_clothing_other = CTkComboBox(master = frame3_clothing, values= list_5_clothing, command=get_all_data)

combobox3_clothing_other.place(x=20, y=110)

#-----------------------------------------------------------------------------------------------------------------------

btn_continue = CTkButton(master=app, text='Continue', corner_radius = 32, command=load_all_data)
btn_continue.place(x=20, y=540)

#-----------------------------------------------------------------------------------------------------------------------
label_for_foto = CTkLabel(master=app, text=' ', corner_radius = 32,
                image = CTkImage(dark_image=img_washmachine, light_image=img_washmachine, size=(400,400)))
label_for_foto.place(x=350, y=150)

#-----------------------------------------------------------------------------------------------------------------------
frame4_description = CTkFrame(master = app, fg_color='#F36F6F', border_color = '#FF3636', border_width=2, width=300, height= 390)
frame4_description .pack(expand=True)
frame4_description .place(x=890, y=10)

label_description = CTkLabel(master=frame4_description, text=f'Description\n This washing machine simulator is dedicated\n to the X-Python competition. In this game\n you can fill the machine with \nvarious clothes, powders,\n lotions and get different results, \nfor this you have the interface \nyou see now\n Опис\n Цей симулятор пральної машини \nприсвячений змаганню X-Python. У цій грі\n ви можете наповнити машину \nрізним одягом, порошками,\n лосьйонами та отримати різні результати, \nдля цього у вас є інтерфейс, \nякий ви бачите зараз',
                             corner_radius = 32)
label_description.place(x=-10, y=0)

btn_start = CTkButton(master=frame4_description, text='Start working', corner_radius = 32, command = show_all_data)
btn_start.place(x=80, y=350)
#-----------------------------------------------------------------------------------------------------------------------

frame5_managment = CTkFrame(master = app, fg_color='#CF76F6', border_color = '#BD22FF', border_width=2, width=300, height= 180)
frame5_managment .pack(expand=True)
frame5_managment .place(x=890, y=410)

label_results = CTkLabel(master=frame5_managment, corner_radius = 32)
label_results.place(x=0, y=10)

#-----------------------------------------------------------------------------------------------------------------------

app.mainloop()
