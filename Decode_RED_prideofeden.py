import os, tkinter, tkinter.filedialog, tkinter.messagebox
from pathlib import Path

# Display the folder selection dialog
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('puraede_decode','Select the target folder.')

# Change the target by changing this line
dir = tkinter.filedialog.askdirectory(initialdir = iDir)

# Decoding process
for i in Path(dir).glob("**/*.iab"):
    i2 = str(i)
    with open(i, 'rb') as f:
        header = f.read()
        UnityFS = header.find(b'\x55\x6E\x69\x74\x79\x46\x53')
    os.remove(os.path.join(dir, i))
    with open(str(i2[:-4])+'.unity3d', 'wb') as f:
        f.write(header[UnityFS:]) #Exporting binaries from UnityFS onwards
