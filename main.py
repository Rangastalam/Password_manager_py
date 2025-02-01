
from tkinter import *
import random

from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sym=['!','@','#','$','%','^','&','*']
    pass_=[]
    pass_+=random.choices(alpha,k=8)
    pass_+=random.choices(sym,k=2)
    pass_.append(str(random.randint(0,9)))
    random.shuffle(pass_)
    pass_string="".join(pass_)

    password_entry.insert(0,pass_string)
    pyperclip.copy(pass_string)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website=website_entry.get()
    user_name=email_entry.get()
    password=password_entry.get()
    new_data= {
        website:{
            "email":user_name,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops",message="Make sure you have not left any field empty")
    else:

        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered\nEmail: {user_name}\npassword: {password}")
        if is_ok:
            try:
                with open("passwords.json","r") as file:
                    data=json.load(file)
                    data.update(new_data)
                with open("passwords.json","w") as file:
                    json.dump(data,file,indent=4)
            except FileNotFoundError:
                with open("passwords.json","w") as file:
                    json.dump(new_data,file,indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0, END)

def search_password():
    website = website_entry.get()


    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message="There are No Passwords Saved yet")
    else:

        searched=data.get(website)


        try:
            messagebox.showinfo(title=f"Details of {website}", message=f"Email:{searched["email"]},\nPassword:{searched["password"]}")
        except TypeError:
            messagebox.showinfo(title="Ooops", message="Password not saved for the mentioned website")


    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.config(bg="white")
logo_img=PhotoImage(file= "logo.png")
lock=canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:",background="white")
website_label.grid(row=1,column=0)



email_label=Label(text="Email/Username:",background="white")
email_label.config(padx=0)
email_label.grid(row=2,column=0)



password_label=Label(text="Password:",background="white")
password_label.grid(row=3,column=0)


website_entry=Entry(width=28)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=46)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"karthikrishi91@gmail.com")

password_entry=Entry(width=28)
password_entry.grid(row=3,column=1)

generatepass_button=Button(text="Generate Password",background="white",command=pass_generator)
generatepass_button.grid(row=3,column=2)

Searchpass_button=Button(text="Search",background="white",command=search_password)
Searchpass_button.grid(row=1,column=2)
Searchpass_button.config(width=12)

add_button=Button(text="Add",background="white",borderwidth=0.5,command=add_pass)
add_button.config(width=39)
add_button.grid(row=4,column=1,columnspan=2)













window.mainloop()