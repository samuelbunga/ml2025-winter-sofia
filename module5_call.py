from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_numbers()

    while True:
        try:
            X = int(input("Enter X (integer to search): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(processor.search_number(X))

if __name__ == "__main__":
    main()