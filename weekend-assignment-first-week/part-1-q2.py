from datetime import datetime
import json

repeat = True
while repeat:
    name = input("Enter Name: ")
    dob = input("Enter Your Date Of Birth(mm/dd/yy): ")
    
    try:
        date = datetime.strptime(dob, '%m/%d/%y')
    except ValueError:
        print("Invalid date format entered!")
    else:
        age_input = input("Enter Age: ")
        try:
            age = int(age_input)
        except ValueError:
            print("That's not an integer!")
        else:
            hobbies = input('Enter hobbies of a list separated by comma: ')
            hobbies_list = hobbies.split(',')

            final_dict = {
                "name": name,
                "dob": str(date),
                "age": age,
                "hobbies": hobbies
            }

            # Serializing json 
            json_object = json.dumps(final_dict, indent = 4)
            
            # Writing to sample.json
            with open("sample.json", "w") as outfile:
                outfile.write(json_object)


            repeat_check = input('Do you wish to Quit? (y/n)')
            if(repeat_check == 'y'):
                repeat = False
            else:
               repeat = True
print("The Program Ended Successfully!")