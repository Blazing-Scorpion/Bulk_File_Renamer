import os
from termcolor import colored
import platform


class rename:

    def __init__(self):
        self.folder_path = None
        self.initial = None

    def rename_files(self):
        i = 0
        for filename in os.listdir(self.folder_path):
            source = os.path.join(self.folder_path, filename)
            extension = os.path.splitext(filename)
            if i == 0:
                destination_filename = f"{self.initial}{extension[1]}"
            else:
                destination_filename = f"{self.initial}_{str(i)}{extension[1]}"
            final_destination = os.path.join(self.folder_path, destination_filename)
            if os.path.exists(final_destination):
                i += 1
                continue
            print(colored(f"Renaming {source} to {final_destination}", "yellow"))
            os.rename(source, final_destination)
            i += 1

    def banner(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        print(colored("""          
              ____        _ _        _____ _ _      
             | __ ) _   _| | | __   |  ___(_) | ____ 
             |  _ \| | | | | |/ /   | |_  | | |/ _  /
             | |_) | |_| | |   <    |  _| | | |  __/
             |____/ \__,_|_|_|\_\   |_|   |_|_|\___|  
                                             ____                                      
                                            |  _ \ ___ _ __   __ _ _ __ ___   ___ _ __ 
                                            | |_) / _ \ '_ \ / _` | '_ ` _ \ / _ \ '__|
                                            |  _ <  __/ | | | (_| | | | | | |  __/ |   
                                            |_| \_\___|_| |_|\__,_|_| |_| |_|\___|_| \n""", 'green'))
        self.display_information()

    def display_information(self):
        print(colored("\nThis Tool is Programmed to Rename all the Files in a Directory.\n", 'yellow'))
        print(colored("Usage: The User needs to Provide an Initial that they want. Every File's name "
                      "will be Changed with the \n       Initial as the Suffix Followed by Consecutive "
                      "Numbers.\n", 'cyan'))
        self.user_input()

    def user_input(self):
        self.folder_path = input(colored("\nEnter The Path of the Folder: ", "green"))
        if not os.path.exists(self.folder_path):
            print(colored("\nThe Entered Path Does Not Exist! Exiting!!\n", 'red'))
            exit(0)
        self.initial = input(colored("\nEnter the initial of each file: ", 'green'))
        print(colored("\nStarting the Renaming Process.... \n", "green"))
        self.rename_files()


if __name__ == "__main__":
    renamer = rename()
    renamer.banner()
    print(colored("\nAll the Files have been Renamed Successfully.\n", 'green'))
