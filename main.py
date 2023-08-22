# Fake name generator. | ohusq | 21-8-23 : 22:39 AMSTERDAM

# Importeer de bibioltheken
import random as rnd

# Constructueer de getRandom class
class getRandom():
    def __init__(self) -> None:
        pass
    
    def catch_error(_, file_name) -> None:
        print(f"""
            File has not been found in the current directory.
            \n
            Please check your files.
            \n
            File not found: {file_name}(.txt)
        """)
    # files Class gebruik voor beter indexen. ookal is dit niet het slimste
    class files():
        def __init__(self) -> None:
            self.first_names = open("first-names.txt", "r")
            self.last_names  = open("last-names.txt", "r")
            self.middle_names= open("middle-names.txt", "r")
            

    def first_name() -> str:
        try:
            with getRandom.files().first_names as f:
              lines = f.readlines() # Pakt alle lijnen (kan laggen)
              return str(rnd.choice(lines))
        except FileNotFoundError:
            getRandom().catch_error("first_names")

    def middle_name() -> str:
        try:
            with getRandom.files().middle_names as f:
              lines = f.readlines() # Pakt alle lijnen (kan laggen)
              return str(rnd.choice(lines))
        except FileNotFoundError:
            getRandom().catch_error("middle_names")

    def last_name() -> str:
        try:
            with getRandom.files().last_names as f:
              lines = f.readlines() # Pakt alle lijnen (kan laggen) 
              return str(rnd.choice(lines))
        except FileNotFoundError:
            getRandom().catch_error("last_names")
            
        
if __name__ == "__main__":
    print("PHASE 1 | Success loading base file |")
    print("PHASE 2 | Loading                   | You can ignore the part under this line")
    print(f"PHASE 2 | Random name (first)       | {getRandom.first_name()}")
    print("--"*20)
    print("Welcome to ohusq's fake name generator!")
    print("Would you like to use a middle name?")
    use_middle_name = input("Input (yes / no) :")

    if use_middle_name.lower() == "yes" or use_middle_name.lower() == "y":
        print("You have pressed: yes")
        fake_first_name  = getRandom.first_name().strip("\n")
        fake_middle_name = getRandom.middle_name().strip("\n")
        fake_last_name   = getRandom.last_name().strip("\n")
        fake_full_name   = fake_first_name + " " + fake_middle_name + " " + fake_last_name # Dit is dom.
        print("Your fake name has loaded")
        print(f"Your new name is: {fake_full_name}")
    elif use_middle_name.lower() == "no" or use_middle_name.lower() == "n":
        print("You have pressed: yes")
        fake_first_name  = getRandom.first_name().strip("\n")
        fake_last_name   = getRandom.last_name().strip("\n")
        fake_full_name   = fake_first_name + " " + fake_last_name # Dit is dom.
        print("Your fake name has loaded")
        print(f"Your new name is: {fake_full_name}")
