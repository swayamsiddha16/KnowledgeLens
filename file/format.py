with open("swayam.log") as f:
    emp_content=f.readlines()
    num_lines = len(emp_content)
    print("The file contains ",num_lines,"lines")
    line_num=1
    while True:
        for i in range(line_num,line_num+21):
            if i< num_lines:
                print(emp_content[i])
        user_input = input("Do you want to see another 20 lines ? (y/n): ")
        if user_input.lower()=="y":
            line_num += 20
        else:
            print("Thank you for visiting.")
            break


   
   