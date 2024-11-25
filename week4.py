def read_and_write_file():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read from: ")

    try:
        # Try to open the file for reading
        with open(filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()
            
            # Modify the content in some way, e.g., convert to uppercase
            modified_content = content.upper()  # Example modification
            
            # Define the output file name
            output_filename = "modified_" + filename
            
            # Write the modified content to a new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
            
            print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()