import tkinter as tk
from PIL import ImageTk, Image
import threading
import ayoThatsCap
import superSonicSnailMail

root = tk.Tk()

class filterButtons():
    def __init__(self, filterName, imgName):
        self.fname = filterName
        self.img = imgName
        newButton = tk.Button(root, text=self.fname, command=lambda: filterButtons.applyFilter(imgName))
        newButton.pack()
    
    def applyFilter(imgName):
        pass
        #img.show()

def requestEmail():
    emailAdd = tk.StringVar()
    addressInstructions = tk.Label(root, text="Enter your email:")
    addressInstructions.pack()
    adressBox = tk.Entry(root, textvariable=emailAdd)
    adressBox.pack()
    return emailAdd

def showCap(img):
    imgtk = ImageTk.PhotoImage(Image.fromarray(img))
    imgShow = tk.Label(root, image=imgtk)
    imgShow.pack()

def dispCap():
    while ayoThatsCap.getCap()[1]==False:
        frame = ayoThatsCap.getCap()[0]
        showCap(frame)

filters = {
    'sunglasses' : 'sunglasses.jpg',
    'mustache' : 'mustache.jpg',
    'hearts blush' : 'heartsBlush.jpg'
}

def main():
    root.title('Photobooth')
    receiver = requestEmail()
    fname = tk.Button(root, text="TAKE PHOTO", command=lambda: superSonicSnailMail.sendEmail(ayoThatsCap.getCap(), receiver))
    fname.pack()

    for fil in filters:
        newButton = filterButtons(fil, filters[fil])

    root.mainloop()

threadMain = threading.Thread(target=main)
threadCap = threading.Thread(target=dispCap)

threadMain.start()
threadCap.start()