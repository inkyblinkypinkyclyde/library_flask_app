class Book:

    def __init__(self, title, author, blurb, read=False, id=None):
        self.title = title
        self.author = author
        self.blurb = blurb
        self.read = read
        self.id = id

    def mark_read(self):
        self.read = True