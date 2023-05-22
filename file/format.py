# try:
#     with open("swayam.log") as f:
#         emp_content = f.readlines()
#         num_lines = len(emp_content)
#         if num_lines == 0:
#             raise ValueError("Log file is empty.")

#         print(f"The file contains {num_lines} lines")
#         lines_per_iteration = int(input("Enter the number of lines to print at a time: "))
#         end_line = int(input("Enter the line number up to which you want to see (0 for all lines): "))

#         if end_line == 0 or end_line > num_lines:
#             end_line = num_lines

#         for line_num in range(0, end_line, lines_per_iteration):
#             for line in emp_content[line_num:line_num + lines_per_iteration]:
#                 print(line.strip())

#             if line_num + lines_per_iteration >= end_line:
#                 print("The line ends here.")
#                 break

#             user_input = input("Do you want to see the next set of lines? (y/n): ")
#             if user_input.lower() != "y":
#                 print("Thank you for visiting.")
#                 break

# except FileNotFoundError:
#     print("Log file not found.")
# except IOError:
#     print("Error accessing the log file.")
# except ValueError as e:
#     print(e)
#yml file format
#u have to read 2 file 1 for which file to read and howmuch line and 2nd the particular file the file which contain the info will be the config file
#b.txt-10000



try:
    
    with open("swayam.log") as f:
        emp_content = f.readlines()
        num_lines = len(emp_content)
        if num_lines == 0:
            raise ValueError("Log file is empty.")

        print(f"The file contains {num_lines} lines")
        lines_per_iteration = int(input("Enter the number of lines to print at a time: "))
        end_line = int(input("Enter the line number up to which you want to see (0 for all lines): "))

        if end_line == 0 or end_line > num_lines:
            end_line = num_lines

        for line_num in range(0, end_line, lines_per_iteration):
            for line in emp_content[line_num:line_num + lines_per_iteration]:
                print(line.strip())

            if line_num + lines_per_iteration >= end_line:
                print("The line ends here.")
                break

            user_input = input("Do you want to see the next set of lines? (y/n): ")
            if user_input.lower() != "y":
                print("Thank you for visiting.")
                break

        if line_num + lines_per_iteration < end_line:
            print("The requested number of lines exceeds the available lines.")

except FileNotFoundError:
    print("Log file not found.")
except IOError:
    print("Error accessing the log file.")
except ValueError as e:
    print(e)



