# slipt the word from the right, and only make two splits.
answer = input("File name: ").lower().strip().rsplit(".", maxsplit = 1)

if len(answer) == 2:
    match answer[1]:
        case "jpg" | "jpeg":
            print(f"image/jpeg")
        case "gif" | "png":
            print(f"image/{answer[1]}")
        case "pdf" | "zip":
            print(f"application/{answer[1]}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")

