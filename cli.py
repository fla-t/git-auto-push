import argparse
import os
import sys
import utils

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
        action="store_true",
        help="track the current working directory.",
    )

    parser.add_argument(
        "--trackdir",
        default="",
        type=str,
        help="Identify the location of the repo you want to track.",
    )

    parser.add_argument(
        "-ls",
        "--list",
        help="list the repos currently being tracked.",
    )

    args = parser.parse_args()

    if (args.init):
        utils.init()
    
    elif (args.track):
        utils.track(os.getcwd())



if __name__ == "__main__":
    main()