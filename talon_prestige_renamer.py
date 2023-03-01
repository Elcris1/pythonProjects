import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directory = input("Introduce the directory: ")
    entries = os.listdir(directory) # Getting the list of files
    print("Replacing directory:", directory)
    # Code for every file in directory
    for entry in entries:
        # if not a file -> Directory
        if "." not in entry:
            # Getting new directory name
            newDirectory = directory + "\\" + entry
            print("Directory found:", newDirectory)
            # Getting the list of files in new directory
            newFiles = os.listdir(newDirectory)
            for file in newFiles:
                # Replacing name for the file
                newFileName = file.replace(".pie_c_12_9", "")
                print("\t Renaming", file, "for", newFileName)

                # Creating old and new directories for the os module
                oldFileDirectory = newDirectory + "\\" + file
                newFileDirectory = newDirectory + "\\" + newFileName

                # Renaming the file
                os.rename(oldFileDirectory, newFileDirectory)

            print(newDirectory, "already replaced")
        else:
            # Replacing the name for the file
            newEntryName = entry.replace(".pie_c_12_9", "")
            print("\t Renaming", entry, "for", newEntryName)

            # Creating the new and the old directories for the os module
            oldFileDirectory = directory + "\\" + entry
            newFileDirectory = directory + "\\" + newEntryName

            # Renaming the file
            os.rename(oldFileDirectory, newFileDirectory)

    print(directory, "Replaced")

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
