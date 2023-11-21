import os



def load_filepaths_from_directory(path):
    # List to store the names of the puf data files in
    txt_files = []

    # Add all filenames to list so we can pass them as an argument to our Calculators
    for filename in os.listdir(path):
        # Check if the file ends with .txt
        if filename.endswith(".txt"):
            # Add the file path to the list
            txt_files.append(os.path.join(path, filename))

    return txt_files