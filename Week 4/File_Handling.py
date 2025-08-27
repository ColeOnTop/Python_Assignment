def modify_content(content):
    # Modify content here (example: convert to uppercase)
    return content.upper()

def main():
    filename = input("Enter the name of the to read from: ")

    try:
        with open(filename, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read.")
        return

    # Modify content
    modified_content = modify_content(original_content)

    # Create a new filename for output
    output_filename = f"modified_{filename}"

    try:
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"✅ Modified content written to '{output_filename}'")
    except IOError:
        print(f"❌ Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
