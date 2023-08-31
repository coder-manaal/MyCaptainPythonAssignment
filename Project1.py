#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#School administration tool
import csv

def write_into_csv(info_list):
    with open (stu_info.csv, 'a', newline='') as csv_file:
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact No", "Email ID" ])
        
        writer.writerow(info_list)
        
condition = True

while(condition):
    stu_info = input("Enter student information in the format, (Name Age Contact_No Email_ID):")
    print("Entered information of the student"+stu_info)
    
    #split
    stu_list = stu_info.split(' ')
    print ("Split up information is:"+ str(stu_list))
    
    
    write_into_csv(stu_info)
           
    condition_check = input("Enter (yes/no) if you want to enter information about more students:")
    if condition_check == "yes":
        condition = True
    elif condition_check == "no":
        condition = False


# In[ ]:




