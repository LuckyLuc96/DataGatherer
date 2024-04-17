import sys


fp = str()

def get_fp():
    global fp
    if len(sys.argv) > 2:
        print('Try: "python main.py <file_path>"')
        sys.exit(1)
    if len(sys.argv) == 2:
        fp = sys.argv[1]
        return fp
    else:
        try:
            fp = input('File path: ').strip()
            return fp
        except:
            print("Invalid file path:", fp)
            pass

def check_file_type():
    config = open("config.py", "w")
    config.write('fp ="')
    config.write(fp)
    config.write('"')
    config.close()
    
    if fp.endswith(".csv"):
        import csv_reader
    if fp.endswith(".html"):
        import html_reader
    else:
        print(fp)
        print("Only HTML and CSV file types are supported at this time.")
        pass


if __name__ == "__main__":
    get_fp()
    check_file_type()
