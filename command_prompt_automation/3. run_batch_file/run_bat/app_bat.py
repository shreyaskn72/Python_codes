import subprocess


def trigger_batch_file(filename):

    try:
        # subprocess.call([r'path where the batch file is stored\name of the batch file.bat'])
        subprocess.call([filename])


    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     filename = r'bat_folder/req.bat'
#     trigger_batch_file(filename)