# File Handling and Exception Handling Assignment
#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content modified and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' can't be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_filename = input("Enter the filename you want to read: ")

    output_filename = input("Enter the filename to save the modified content: ")
    modify_file(input_filename, output_filename)
main()


