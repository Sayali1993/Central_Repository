import os
txt, pdf, xlsx, xls, mp4 = ([] for i in range(5))

list_files = ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]
print("List of files : ", list_files)

for file_ in list_files:
    name, ext = os.path.splitext(file_)
    if ext == '.txt':
        txt.append(file_)
    elif ext == '.pdf':
        pdf.append(file_)
    elif ext == '.xls':
        xls.append(file_)
    elif ext == '.mp4':
        mp4.append(file_)
    elif ext == '.xlsx':
        xlsx.append(file_)

Dict = {}
Dict[".txt"] = txt
Dict[".pdf"] = pdf
Dict[".xls"] = xls
Dict[".xlsx"] = xlsx
Dict[".mpv4"] = mp4

print("Output : ", Dict)
