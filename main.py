import sys


if len(sys.argv) > 2:
    print('Try: "python main.py <file_path>"')
    sys.exit(1)
if len(sys.argv) == 2:
    fp = sys.argv[1]
else:
    try:
        fp = input('File path: ').strip()   
    except: 
        print("File not found")
        sys.exit(2) 
    
    






if fp.endswith(".csv"):
    import csv_reader
else:
    print("HTML reader to be added here")
    pass