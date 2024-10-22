from notes import *

def main():
    notes_manager = Notes()
    while True:
        print("\nSelect an option:")
        print("1:Add")
        print("2:Filter")
        print("3:show all notes")
        print("4:count notes")
        print("5:Unique notes")
        print("exit to quit")
        user_input = input("Select an option: ").strip()
        if user_input == "1":
            note = input("enter a note: ").strip()
            notes_manager.add_note(note)

        elif user_input == "2":
            keyword = input("Enter a keyword: ").strip()
            notes_manager.filter_notes(keyword)

        elif user_input == "3":
            notes_manager.show_data()
            
        elif user_input == "4":
            notes_manager.count_notes()

        elif user_input == "5":
            notes_manager.unique_value()

        elif user_input == "exit":
            break
        else:
            print("not found!")

if __name__ == "__main__":
    main()