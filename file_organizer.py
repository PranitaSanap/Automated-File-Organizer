
import os
import shutil

folder = input("Enter folder path: ")

categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"]
}

if not os.path.isdir(folder):
    print("Invalid folder path!")
    raise SystemExit

for category in list(categories) + ["Others"]:
    os.makedirs(os.path.join(folder, category), exist_ok=True)

count = 0

for file in os.listdir(folder):
    source = os.path.join(folder, file)

    if not os.path.isfile(source):
        continue

    ext = os.path.splitext(file)[1].lower()
    category = "Others"

    for name, extensions in categories.items():
        if ext in extensions:
            category = name
            break

    destination = os.path.join(folder, category, file)

    if os.path.exists(destination):
        print("Skipped duplicate:", file)
        continue

    shutil.move(source, destination)
    print(file, "->", category)
    count += 1

print("Organization complete!")
print("Files moved:", count)
