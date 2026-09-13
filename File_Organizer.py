from pathlib import Path

class FileOrganizer:

    def __init__(self):
        self.category={
            'Images':[".jpg", ".jpeg", ".png", ".gif", ".bmp",".webp", ".svg", ".tiff", ".ico", ".heic",".raw", ".jfif", ".avif"],
            'Videos':[".mp4", ".mkv", ".avi", ".mov", ".wmv",".flv", ".webm", ".mpeg", ".mpg", ".3gp",".m4v", ".ts"],
            'Texts':[".txt", ".log", ".md", ".rtf",".ini", ".cfg", ".conf"],
            'Documents':[".pdf", ".doc", ".docx", ".ppt", ".pptx",".xls", ".xlsx", ".csv", ".odt", ".ods",".odp"],
            'Music':[ ".mp3", ".wav", ".aac", ".flac",".ogg", ".m4a", ".wma", ".aiff"]
            }
        
        self.count={'Total':0,
               'Images':0,
               'Videos':0,
               'Texts':0,
               'Documents':0,
               'Music':0,
               'Others':0}
        
        self.path=self.get_path()


        
    def get_path(self):
        print("Enter directory path or press Enter to use current directory")
        path=input("Path: ").strip().strip('"')

        if path=="":
            p=Path.cwd()
        else:
            p=Path(path)
        
        if p.exists() and p.is_dir():
            print("Folder Found")
            return p
        else:
            print("Invalid Path, Folder Not Found")
            return None
        

    def scan(self):
        if not self.path:
            return "Invalid Path"

        for file in self.path.iterdir():
            if file.is_dir() or file.name.startswith("."):
                continue
            
            suffix=file.suffix.lower()
            category=self.get_category(suffix)
            self.move(file,category)
        
        self.summary()



    def get_category(self,extension):
        for category, extensions in self.category.items():
            if extension in extensions:
                return category
        return "Others"
            


    def move(self,file,category):
        destination=self.path / category
        destination.mkdir(exist_ok=True)
        new_path=destination / file.name
        counter=1

        while new_path.exists():
            new_name=f"{file.stem}({counter}){file.suffix}"
            new_path=destination / new_name
            counter+=1
        try:
            file.rename(new_path)
            self.count[category] += 1
            self.count["Total"] += 1

        except Exception as err:
            print(f"Error moving {file.name}: {err}")


    def summary(self):
        if self.count["Total"] == 0:
            print("No files found")
        
        else:
            print("\nSummary:\n")
            for category, total in self.count.items():
                print(f"{category}: {total}")
                           



                    
organizer = FileOrganizer()
organizer.scan()