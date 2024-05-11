import sys

def get_fp():
    try:
        fp = input('File path: ').strip()
        fp = fp.strip("'")
        print(fp)
        return fp
    except:
        print("Invalid file path:", fp)
        pass

def check_file_type():
    fp = get_fp()
    if fp.endswith(".csv"):
        from csv_reader import open_up
        open_up(fp)
    elif fp.endswith(".html"):
        from html_reader import open_up
        open_up(fp)
    else:
        print(fp)
        print("Only HTML and CSV file types are supported at this time.")
        pass

if __name__ == "__main__":
    check_file_type()