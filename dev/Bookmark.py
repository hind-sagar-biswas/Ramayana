import os
import subprocess

class Bookmark():
    def __init__(self, app = None):
        self.app = app
        self.last_read = "BALA:1:1"
        self.bookmarks = []
        self.last_read_file = "read"
        self.bookmarks_file = "bookmarks"

        self.retrieve()
        self.update()

    def fetch_content(self, file_name):
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path, f'cache\\{file_name}.txt')

            with open(file_path, 'r', encoding='utf-8') as infile:
                data = infile.read()
        except:
            data = False
        return data
    
    def write_content(self, file_name, content, mode = 'w'):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, f'cache\\{file_name}.txt')

        try:
            with open(file_path, mode, encoding='utf-8') as outfile:
                outfile.write(content)
        except:
            subprocess.run(["mkdir", "cache"], shell=True)
            self.write_content(file_name, content)


    def update_last_read(self, kanda, sarga, verse):
        self.last_read = f'{kanda}:{sarga}:{verse}'
        self.update()
    
    def get_last_read(self):
        read = list(self.last_read.split(':'))
        return [read[0], int(read[1]), int(read[2])]

    def retrieve(self):
        # retrieve last read
        last_read = self.fetch_content(self.last_read_file)
        if not last_read: self.write_content(self.last_read_file, self.last_read)
        else: self.last_read = last_read

        #retrieve bookmarks
        bookmarks = self.fetch_content(self.bookmarks_file)
        if not bookmarks: self.write_content(self.bookmarks_file, "\n".join(self.bookmarks))
        else: self.bookmarks = bookmarks.split("\n")
        return
    
    def add(self):
        self.bookmarks.append(self.last_read)
        self.update()
        return
    
    def remove(self):
        return
    
    def update(self):
        self.write_content(self.last_read_file, self.last_read)
        self.write_content(self.bookmarks_file, "\n".join(self.bookmarks))
        return
    
book = Bookmark()
book.add()