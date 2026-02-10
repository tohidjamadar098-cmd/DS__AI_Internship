filename = input("Enter a filename (e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print("\nFile contents:")
        print(contents)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
