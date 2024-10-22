from list_file import * 

class Notes:
    def __init__(self):
        self.notes = MyList()

    def add_note(self, note):
        try:
            self.notes.append(note)
        except ValueError as e:
            print(e)
        else:
            print(f"Note Added: {note}") 

    def filter_notes(self, keyword):
        data = self.notes.filter_data(keyword)
        if data:
            print(f"Notes: {keyword} ---> {data}")
        else:
            print("Not Found!")

    def show_data(self, separator="\n"):
        result = self.notes.join_data(separator)
        print(result) 

    def count_notes(self):
        counts = self.notes.count_value()
        for note, count in counts.items():
            print(note, count)

    def unique_value(self):
        unique_notes = self.notes.unique()
        number_unique_notes = self.notes.nuique()
        print(f"Unique Notes: {unique_notes}")
        print(f"Number of Unique Notes: {number_unique_notes}")

if __name__ == "__main__":
    all_note = Notes()
    all_note.add_note("Python") # ["Python"]
    print(all_note.notes)
    all_note.add_note(7)
    print(all_note.notes)
    all_note.add_note("Python3")
    print(all_note.notes)
    all_note.filter_notes("Python3")
    """separator = input("seprator: ") # separator=""
    if separator == "":
        separator = "\n"
    all_note.show_data(separator)"""
    all_note.count_notes()
    all_note.unique_value()
