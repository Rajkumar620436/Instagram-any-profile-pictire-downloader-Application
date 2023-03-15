from tkinter import *
import instaloader

from tkinter import messagebox

insta=instaloader.Instaloader()
def download():

    username=entryField.get()
    insta.download_profile(username,profile_pic_only=True)
    messagebox.showinfo('Success','profile Image is Successfully download')

root=Tk()
root.title('Instagram Profile Pic Downloader')
logoImage=PhotoImage(file='instagram (1).png')

logoLabel=Label(root,image=logoImage)


titleLabel=Label(root,text='Instagram Profile Image Downloader',font=('Times new Roman',30,'bold'))
titleLabel.grid(row=1,column=0,pady=10,padx=30)

enterLabel=Label(root,text='Enter UserName:',font=('arial',20,'bold'))
enterLabel.grid(row=2,column=0,pady=10)
entryField=Entry(root,width=40,font=('arial',15,'bold'),bd=5)
entryField.grid(row=3,column=0,pady=10)

downloadButton=Button(root,text='DOWNLOAD',font=('arial',15,'bold'),command=download)
downloadButton.grid(row=4,column=0,pady=10)
root.mainloop()



