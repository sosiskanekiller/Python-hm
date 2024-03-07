import os #импортируем os что бы было круто

def pisat_bukvi(title):  # это типо как в луа local text = че то там
    print(f"{title}")

def pisat_bukvi_cvetom(title):  # это типо как в луа local text = че то там
    print(f"\033[95m{title}\033[0m")

def govno_color(text):#это типо как в луа local green = че то там
    print("\033[92m" + text + "\033[0m")

def main_menu():
    pisat_bukvi("""
  ___    ___         _____                        
 |   \  / __|  ___  |_   _|  ___   __ _   _ __    
 | |) | \__ \ |___|   | |   / -_) / _` | | '  \   
 |___/  |___/         |_|   \___| \__,_| |_|_|_|  
    """)

    input("Нажмите Enter, чтобы продолжить...")
    os.system('cls' if os.name == 'nt' else 'clear')

    pisat_bukvi_cvetom("\nЗадание №1")

    print("Печать")
    print("через")
    print("строку")

    pisat_bukvi_cvetom("\nЗадание №2")

    print("1. 2 + 2 =", 2 + 2)
    print("2. 2 + 2 = {}".format(2 + 2))
    print(f"3. 2 + 2 = {2 + 2}")
    print("4. 2 + 2 = " + str(2 + 2))
    print("5. {} = {}".format("2 + 2", 2 + 2))

    pisat_bukvi_cvetom("\nЗадание №3")
    govno_color("""  
      _  __  _         _   _   _ 
     | |/ / (_)  _ _  (_) | | | |
     | ' <  | | | '_| | | | | | |
     |_|\_\ |_| |_|   |_| |_| |_|
            """)

    input("\033[95m\nНажмите Enter, чтобы завершить программу...\033[0m")


if __name__ == "__main__":
    main_menu()
