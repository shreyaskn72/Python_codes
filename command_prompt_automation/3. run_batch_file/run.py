from run_bat.app_bat import trigger_batch_file

if __name__ == "__main__":
    try:
        filename = r'run_bat\bat_folder\req.bat'
        trigger_batch_file(filename)

    except Exception as e:
        print(e)
