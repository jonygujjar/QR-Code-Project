import qrcode
from tkinter import *
from tkinter import messagebox
from segno import helpers

#Creating the window
wn = Tk()
wn.title('QR Code Generator')
wn.geometry('700x700')
wn.config(bg='#516D75')
#Label for the window
headingFrame = Frame(wn,bg="#00cccc",bd=5)
headingFrame.place(relx=0.13,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code
Frame1 = Frame(wn,bg="#516D75")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text/URL: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name
Frame3 = Frame(wn,bg="#516D75")
Frame3.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Name Your QR Code: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting the input of the size of the QR Code
Frame4 = Frame(wn,bg="#516D75")
Frame4.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.2)

label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.1)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)
#Function to generate the QR code and save it
def generateCode():
  #Creating a QRCode object of the size specified by the user
  qr = qrcode.QRCode(version = size.get(),
            box_size = 10,
            border = 4)
  qr.add_data(text.get()) #Adding the data to be encoded to the QRCode object
  qr.make(fit = True) #Making the entire QR Code space utilized
  img = qr.make_image() #Generating the QR Code
  img.save(f'{name.get()}.png') #Saving the QR Code
  #Showing the pop up message on saving the file
  messagebox.showinfo("QR Code Generator","QR Code is saved successfully!")

#Button to generate and save the QR Code
button = Button(wn, text='Generate QR Code',bg="#00cccc",font=('Courier',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.7, relwidth=0.30, relheight=0.05)


# Function to make new window
def openNewWindow():
  newwn = Toplevel(wn)
  newwn.title('V_Card Generator')
  newwn.geometry('700x700')
  newwn.config(bg='#516D75')
#Label for the window
  headingFrame = Frame(newwn,bg="#00cccc",bd=5)
  headingFrame.place(relx=0.13,rely=0.05,relwidth=0.7,relheight=0.1)
  headingLabel = Label(headingFrame, text="Generate V_Card QR Code", bg='azure', font=('Times',20,'bold'))
  headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

  #Taking the input of the text or URL to get QR code
  Frame1 = Frame(newwn,bg="#516D75")
  Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

  label1 = Label(Frame1,text="First Name: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label1.place(relx=0.05,rely=0.2, relheight=0.08)

  name_f = Entry(Frame1,font=('Century 12'))
  name_f.place(relx=0.05,rely=0.3, relwidth=0.4, relheight=0.15)
  
  label5 = Label(Frame1,text="Last Name: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label5.place(relx=0.5,rely=0.2, relheight=0.08)

  name_l = Entry(Frame1,font=('Century 12'))
  name_l.place(relx=0.5,rely=0.3, relwidth=0.4, relheight=0.15)

  #Getting input of the location to save QR Code
  Frame2 = Frame(newwn,bg="#516D75")
  Frame2.place(relx=0.1,rely=0.3,relwidth=0.7,relheight=0.3)

  label2 = Label(Frame2,text="Enter the Contact No: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label2.place(relx=0.05,rely=0.1, relheight=0.08)

  contact = Entry(Frame2,font=('Century 12'))
  contact.place(relx=0.05,rely=0.2, relwidth=1, relheight=0.15)

  #Getting input of the QR Code image name
  Frame3 = Frame(newwn,bg="#516D75")
  Frame3.place(relx=0.1,rely=0.45,relwidth=0.7,relheight=0.3)

  label3 = Label(Frame3,text="Enter the E-Mail: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label3.place(relx=0.05,rely=0.1, relheight=0.08)

  mail = Entry(Frame3,font=('Century 12'))
  mail.place(relx=0.05,rely=0.2, relwidth=1, relheight=0.15)

  #Getting the input of the size of the QR Code
  Frame4 = Frame(newwn,bg="#516D75")
  Frame4.place(relx=0.1,rely=0.6,relwidth=0.7,relheight=0.2)

  label4 = Label(Frame4,text="Enter the Url: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label4.place(relx=0.05,rely=0.1, relheight=0.08)

  url = Entry(Frame4,font=('Century 12'))
  url.place(relx=0.05,rely=0.2, relwidth=1, relheight=0.2)

  Frame5 = Frame(newwn,bg="#516D75")
  Frame5.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)

  label5 = Label(Frame5,text="Name Your QR Code: ",bg="#516D75",fg='azure',font=('Courier',13,'bold'))
  label5.place(relx=0.05,rely=0.1, relheight=0.08)

  q_name = Entry(Frame5,font=('Century 12'))
  q_name.place(relx=0.05,rely=0.2, relwidth=1, relheight=0.2)
  def generateVcard():
    qrcode = helpers.make_vcard(name=(name_f.get()+';'+name_l.get()), displayname=(name_f.get()+' '+name_l.get()),
                          email=mail.get(), phone=contact.get(),url=url.get())
    qrcode.save(f'{q_name.get()}.png', scale=8)
    qrcode.designator
    '5-L'
    messagebox.showinfo("V_Card Generator","QR Code is saved successfully!")

  button2 = Button(newwn, text='Generate V_Card QR Code',bg="#00cccc",font=('Courier',15,'normal'),command=generateVcard)
  button2.place(relx=0.135,rely=0.9, relwidth=0.5, relheight=0.05)
  newwn.mainloop()


headingFrame2 = Frame(wn,bg="#00cccc",bd=5)
headingFrame2.place(relx=0.13,rely=0.77,relwidth=0.7,relheight=0.1)
headingLabel2 = Label(headingFrame2, text="Generate V_Card QR Code", bg='azure', font=('Times',15,'bold'))
headingLabel2.place(relx=0,rely=0, relwidth=1, relheight=1)
#
button1 = Button(wn, text='Generate V_Card',bg="#00cccc",font=('Courier',15,'normal'),command=openNewWindow)
button1.place(relx=0.35,rely=0.9, relwidth=0.30, relheight=0.05)





#Runs the window till it is closed manually
wn.mainloop()