import os

def rename_files(folder_path):
    try:
        files = os.listdir(folder_path)
        count = 1

        for filename in files:
            old_path = os.path.join(folder_path, filename)

            if os.path.isfile(old_path):
                extension = os.path.splitext(filename)[1]
                new_name = f"file_{count}{extension}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                count += 1

        print("Files renamed successfully.")

    except Exception as error:
        print("Error while renaming files.")
        print("Reason:", error)


path = input("Enter the folder path: ")
rename_files(path)
