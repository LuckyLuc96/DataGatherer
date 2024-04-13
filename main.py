import sys

if len(sys.argv) > 2:
    print('Try: "python main.py <file_path>"')
    sys.exit(1)
if len(sys.argv) == 2:
    fp = sys.argv[1]
    fpvalue = str("fpvalue =", fp)
else:
    try:
        fp = input('File path: ').strip()
        fpvalue = str("fpvalue =", fp)
    except:
        pass

   
with open('config.py', 'a', encoding='utf-8') as file:
    file.write(fpvalue, "\n")

if fp.endswith(".csv"):
    import csv_reader
if fp.endswith("html"):
    import html_reader
else:
    print("Only HTML and CSV file types are supported at this time.")
    pass

with open('config.py', 'a') as file:
    file.write("fpvalue = None")