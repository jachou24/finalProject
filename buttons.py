import tkinter as tk

class buttons():
    def __init__(self, filterName, imgName):
        self.fname = filterName
        self.img = imgName
        newButton = tk.Button(root, text=self.fname, command=lambda: buttons.applyFilter(imgName))
        newButton.pack()
    
    def applyFilter(imgName):
        pass
        #img.show()


root = tk.Tk()

fname = tk.Button(root, text="TAKE PHOTO")
fname.pack()

filters = {
    'sunglasses' : 'sunglasses.jpg',
    'mustache' : 'mustache.jpg',
    'hearts blush' : 'heartsBlush.jpg'
}

for fil in filters:
    buttons(fil, filters[fil])



root.mainloop()