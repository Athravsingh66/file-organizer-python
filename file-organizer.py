import os
import shutil

print(os.getcwd())

file_types = {
"Images": [".jpg", ".png", ".jpeg", ".gif"],
"Videos": [".mp4", ".mkv", ".avi"],
"Audio": [".mp3", ".wav"],
"Documents": [".pdf", ".docx", ".txt"],
"Code": [".py", ".c", ".cpp", ".java"],
"Archives": [".zip", ".rar", ".7z"]
}
def show_supported_extensions():

    print("="*50,"\n")
    
    for folder,extension in file_types.items():
        
        print(folder,":",", ".join(extension),"\n")



def organize_files():
    
    path = input("Enter Folder path:")
    
    if not os.path.isdir(path):
        print("Invalid Folder path")
        return 
    
    for file in os.listdir(path):
        file_path=os.path.join(path,file)
        
        if os.path.isfile(file_path):
            _,extension = os.path.splitext(file)
            
            for folder,extensions in file_types.items():
                if extension.lower() in extensions:
                    
                    folder_path=os.path.join(path,folder)
                    
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                        
                    shutil.move(file_path,os.path.join(folder_path,file))
                    break
                
    print("File Organized Successfully !!!!")




def main_menu():
    
    while True:
        print("========== FILE ORGANIZER ==========")
        print("1. Organize Files")
        print("2. Show Supported Extensions")
        print("3. Exit")
        
        choice = input("Enter your Choice:")
        
        if choice == "1":
            organize_files()
            
        elif choice == "2":
            show_supported_extensions()
            
        elif choice == "3":
            print("Exiting .........!!!!!")
            break
        
        else:
            print("Invalid Choice")
            
main_menu()
