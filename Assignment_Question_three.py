# Importing required modules 
from datetime import datetime
import os,sys, shutil

# User defined function to create backup of files
def backup(source_dir,destination_dir):

    # To check if the user provided source directory exists
    if not os.path.exists(source_dir):
        return (f"{source_dir} does not exists")

    # To check if the user provided destination directory exists , if not then creating it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # To loop through all the files in source directory
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir,file)
        destination_file = os.path.join(destination_dir,file)

        # To check if the file is already persent in destination directory , then appending the timestamp to provide uniqueness
        if os.path.exists(destination_file):
            base , ext = os.path.splitext(file)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            destination_file = os.path.join(destination_dir,f"{base}_{timestamp}{ext}")

        # To copy all the files from source directory to destination directory
        try :
            shutil.copy2(source_file,destination_file)
            print(f"Copying of {file} to {destination_file} is successful")
        # error handling 
        except Exception as e:
            print(f"Copying of {file} failed")

if __name__ == '__main__':

    # To check if user has provided proper argunments  
    if len(sys.argv)!=3:
        print("Please excute the script as Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        backup(source_dir,destination_dir)