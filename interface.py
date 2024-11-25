import tkinter as tk
import ayoThatsCap
import superSonicSnailMail

root = tk.Tk()
fname = tk.Button(root, text="TAKE PHOTO", command=lambda: superSonicSnailMail.sendEmail(ayoThatsCap.getCap()))
fname.pack()

class filterButtons():
    def __init__(self, filterName, imgName):
        self.fname = filterName
        self.img = imgName
        newButton = tk.Button(root, text=self.fname, command=lambda: filterButtons.applyFilter(imgName))
        newButton.pack()
    
    def applyFilter(imgName):
        pass
        #img.show()
filters = {
    'sunglasses' : 'sunglasses.jpg',
    'mustache' : 'mustache.jpg',
    'hearts blush' : 'heartsBlush.jpg'
}
for fil in filters:
    newButton = filterButtons(fil, filters[fil])

def requestEmail(emailAdd):
    addressInstructions = tk.label(root, text="Enter your email:")
    addressInstructions.pack()
    adressBox = tk.Entry(root, textvariable=emailAdd)
    adressBox.pack()
    return emailAdd

def showCap(img):
    imgtk = tk.ImageTk.PhotoImage(img)
    imgShow = tk.Label(root, image=imgtk)
    imgShow.pack()

def dispCap():
    while ayoThatsCap.getCap()[1]==False:
        frame = ayoThatsCap.getCap()[0]
        showCap(frame)

root.mainloop()