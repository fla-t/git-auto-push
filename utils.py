import os
import sys

def getSaveLoc():
    if os.sep == "\\":  # Windows OS
        saveFile_loc = os.path.expanduser(
            os.path.join("~")
        )
    else:  # Other than Windows
        saveFile_loc = os.getenv(
            "XDG_DATA_HOME",
            os.path.expanduser(os.path.join("~")),
        )
    saveFile_dir = os.path.join(saveFile_loc, "git-auto-push")

    if not os.path.exists(saveFile_dir):
        os.mkdir(saveFile_dir)

    return saveFile_dir

filepath = os.path.join(getSaveLoc(), "auto-pusher.txt")


def init():
    if os.path.isfile(filepath):
        print("File already exists!")
    else:
        filehandler = open(os.path.join(getSaveLoc(), "auto-pusher.txt"), "xt")
        filehandler.close()
        print("A save file has been created!")


def track(dir):
    if os.path.isfile(filepath):
        filehandler = open(filepath, "a")
        filehandler.write(dir)
        filehandler.write("\n")
        filehandler.close()

        print("The directory {} is being tracked now".format(dir))
            
    else:
        print("File does not exists!\n\nUse --init or -i to create a save file.")
