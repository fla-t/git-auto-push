import argparse
import os
import sys


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






def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--init",
        help="create a save file to store the tracked repos.",
        action="store_true",
    )

    parser.add_argument(
        "-t",
        "--track",
        default="",
        help="Identify the location of the repo you want to track, leave it empty if its the current directory.",
    )

    parser.add_argument(
        "-l",
        "--list",
        help="list the repos currently being tracked.",
    )

    args = parser.parse_args()
    if (args.init):
        print(saveFile_dir)
    
    if (args.track):
        print(args.track)





if __name__ == "__main__":
    main()