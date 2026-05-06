from data_handler import input_data, load_csv, load_json
from pdf_generator import generate_pdf

data = []

def menu():
    global data

    while True:
        print("\n===== PDF REPORT GENERATOR =====")
        print("1. Add Data")
        print("2. Load Data from CSV")
        print("3. Load Data from JSON")
        print("4. Generate Student Report")
        print("5. Generate Company Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input_data()

        elif choice == "2":
            path = input("Enter CSV file path: ")
            data = load_csv(path)

        elif choice == "3":
            path = input("Enter JSON file path: ")
            data = load_json(path)

        elif choice == "4":
            generate_pdf(data, "Student")

        elif choice == "5":
            generate_pdf(data, "Company")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()