from command_prompt.app_cmd import run_cmd


if __name__ == "__main__":
    try:
        filename = r"command_prompt\json_folder\command_prompt.json"
        run_cmd(filename)

    except Exception as e:
        print(e)
