class Bookmark():
    def __init__(self, app):
        self.app = app
        self.last_read = "BALA:1:1"
        self.bookmarks = []

    def update_last_read(self, kanda, sarga, verse):
        self.last_read = f'{kanda}:{sarga}:{verse}'
        self.update()
    
    def get_last_read(self):
        read = list(self.last_read.split(':'))
        return [read[0], int(read[1]), int(read[2])]

    def retrieve(self):
        return
    
    def add(self):
        return
    
    def remove(self):
        return
    
    def update(self):
        return