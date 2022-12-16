
with open("sample.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write("hello hi")