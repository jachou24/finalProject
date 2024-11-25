import tkinter as tk
import ayoThatsCap
import superSonicSnailMail

class filterButtons():
    def __init__(self, filterName, imgName):
        self.fname = filterName
        self.img = imgName
        newButton = tk.Button(root, text=self.fname, command=lambda: filterButtons.applyFilter(imgName))
        newButton.pack()
    
    def applyFilter(imgName):
        pass
        #img.show()


root = tk.Tk()

fname = tk.Button(root, text="TAKE PHOTO", command=lambda: superSonicSnailMail.sendEmail(ayoThatsCap.takePhoto()))
fname.pack()

filters = {
    'sunglasses' : 'sunglasses.jpg',
    'mustache' : 'mustache.jpg',
    'hearts blush' : 'heartsBlush.jpg'
}
for fil in filters:
    newButton = filterButtons(fil, filters[fil])


def requestEmail(emailAdd):
    addressInstructions = tk.label(text="Enter your email:")
    adressBox = tk.Entry(root, textvariable=emailAdd)
    adressBox.pack()
    return emailAdd

def showCap(img):
    imgtk = tk.ImageTk.PhotoImage(img)
    imgShow = tk.Label(root, image=imgtk)
    imgShow.pack()

root.mainloop()