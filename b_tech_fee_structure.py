from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import csv

# Initialize the WebDriver 
driver = webdriver.Edge()
def btech_fee_structure(driver,name, links):
    
    name_df = pd.DataFrame({"Name": [name]})
    
    course_fee_data=[] 
    college_fee_struture=[]
    for link in links:
        print(link)
        driver.get(link)
        time.sleep(2) 
        try:
            course_name=driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/section/div[1]/div[1]/div/div/div[1]/div/div[1]/div[1]/h2')[0].text
                            
            table_head=driver.find_element(By.TAG_NAME, 'thead').text.strip().split() 
                            
            table_body=driver.find_element(By.TAG_NAME, 'tbody').text.strip().split()
            print(course_name)
            print(table_body)
            print(table_head) 
            time.sleep(2)
            
            if "Semester" in table_head:
              to = table_head.index("Semester")
            else:
              to = len(table_head)
            
            fr=1
            modified_year=[]
            if table_head[0]=="Years":
              modified_year=table_head[fr:to]
            else:
              years=table_head[fr:to]
              modified_year=[]
              for year in years:
                modified_year.append(year)
                modified_year.append("")
            semester=table_head[to+1:]
            
            maximum_length=8
            
            if len(semester)<maximum_length:
                semester=semester+[""]*(maximum_length-len(semester))
            elif len(semester)>maximum_length:
                semester=semester[:maximum_length]
            else:
                semester=[""]*maximum_length 
            if len(modified_year)<maximum_length :
                modified_year=modified_year+[""]*(maximum_length-len(modified_year))
            elif len(modified_year)>maximum_length:
                modified_year=modified_year[:maximum_length]
            else:
                modified_year=[""]*maximum_length
            
            
            tution_index=""
            AdmissionFees_index = ""
            TutionFees_index =""
            RegistrationFees_index = ""
            ExamFees_index = ""
            OtherFees_index= ""
            TotalFees_index = ""
            time.sleep(1)
            if "Tution" in table_body:
              TutionFees_index=table_body.index("Tution")
            if "Admission" in table_body:
              AdmissionFees_index = table_body.index("Admission")
            if "Registration" in table_body:
              RegistrationFees_index =table_body.index("Registration")
            if "Exam" in table_body:
              ExamFees_index =table_body.index("Exam")
            if "Other" in table_body:
              OtherFees_index= table_body.index("Other")
            if "Total" in table_body:
              TotalFees_index =table_body.index("Total")
            
            AdmissionFees = ""
            TutionFees =""
            RegistrationFees = ""
            ExamFees = ""
            OtherFees= ""
            TotalFees = ""
            for i in table_body:
                if table_body.index(i) == AdmissionFees_index:
                    # print("AdmissionFees_index", AdmissionFees_index)
                    fr=table_body.index(i)+2
                    to=fr
                    for i in range(to,len(table_body)):
                      if table_body[i].startswith('₹') or table_body[i].startswith('-'):
                        to=to+1
                
                      else:
                        break
                
                      AdmissionFees=table_body[fr:to]
                      # print("AdmissionFees:", AdmissionFees)
                
                elif  table_body.index(i) == TutionFees_index :
                    # print("hellio",table_body.index(i))
                    # print("i am iside TutionFees_index", TutionFees_index)
                    fr=table_body.index(i)+2
                    to=fr
                    for i in range(to,len(table_body)):
                      if table_body[i].startswith('₹') or table_body[i].startswith('-'):
                        to=to+1
                
                      else:
                        break
                      TutionFees=table_body[fr:to]
                      # print("TutionFees:", TutionFees)
                
                elif  table_body.index(i) == RegistrationFees_index:
                    fr=table_body.index(i)+2
                    to=fr
                    for i in range(to,len(table_body)):
                
                      if table_body[i].startswith('₹') or table_body[i].startswith('-'):
                        to=to+1
                
                      else:
                        break
                
                      RegistrationFees=table_body[fr:to]
                      # print("RegistrationFees:", RegistrationFees)
                elif  table_body.index(i) == ExamFees_index:
                    fr=table_body.index(i)+2
                    to=fr
                    for i in range(to,len(table_body)):
                      if table_body[i].startswith('₹') or table_body[i].startswith('-'):
                        to=to+1
                
                      else:
                        break
                
                      ExamFees=table_body[fr:to]
                
                elif  table_body.index(i) == OtherFees_index:
                    # print("iam inside OtherFees_index", OtherFees_index)
                    fr=table_body.index(i)+2
                    to=fr
                    for i in range(to,len(table_body)):
                      if table_body[i].startswith('₹') or table_body[i].startswith('-'):
                        to=to+1
                
                      else:
                        break
                
                      OtherFees=table_body[fr:to]
                    # print("OtherFees", OtherFees, len(OtherFees))
                
                elif  table_body.index(i) == TotalFees_index:
                    # print("i am inside TotalFees_index ", TotalFees_index)
                    fr=table_body.index(i)+2
                    
                    if table_body.index(i) + 2:
                      # print("hello")
                      starting_index=table_body.index(i) + 2
                      if table_body[starting_index].startswith('₹'):
                        # print("hi ashifa")
                        fr=table_body.index(i)+2
                      else:
                        fr=table_body.index(i)+4
                    
                    to=fr
                    for i in range(to,len(table_body)):
                      if table_body[i].startswith('₹') or table_body[i].startswith('Lakhs'):
                        to=to+1
                
                      else:
                        break
                
                      TotalFees=table_body[fr:to]
                
                maximum_length=8
                modified_AdmissionFees=[]
                if len(AdmissionFees)==0:
                   modified_AdmissionFees=[""]*maximum_length
                elif len(AdmissionFees)<maximum_length :
                  modified_AdmissionFees=[]
                  for fee in AdmissionFees:
                    modified_AdmissionFees.append(fee)
                    modified_AdmissionFees.append("")
                  if len(modified_AdmissionFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_AdmissionFees)))
                    # print("length",length)
                    modified_AdmissionFees=modified_AdmissionFees+length
                elif len( modified_AdmissionFees)>maximum_length:
                     modified_AdmissionFees= modified_AdmissionFees[:maximum_length]
                else:
                  modified_AdmissionFees=AdmissionFees
                # print("modified_AdmissionFees", modified_AdmissionFees)
                
                modified_TutionFees=[]
                if len(TutionFees)==0:
                   modified_TutionFees=[""]*maximum_length
                elif len(TutionFees)<maximum_length:
                  modified_TutionFees=[]
                  for fee in TutionFees:
                    modified_TutionFees.append(fee)
                    modified_TutionFees.append("")
                  if len(modified_TutionFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_TutionFees)))
                    # print("length",length)
                    modified_TutionFees=modified_TutionFees+length
                elif len(modified_TutionFees)>maximum_length:
                    modified_TutionFees= modified_TutionFees[:maximum_length]
                else:
                  modified_TutionFees=TutionFees
                # print("modified_TutionFees",modified_TutionFees)
                
                modified_RegistrationFees=[]
                if len(RegistrationFees)==0:
                   modified_RegistrationFees=[""]*maximum_length
                elif len(RegistrationFees)<maximum_length :
                  modified_RegistrationFees=[]
                  for fee in RegistrationFees:
                    modified_RegistrationFees.append(fee)
                    modified_RegistrationFees.append("")
                  if len(modified_RegistrationFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_RegistrationFees)))
                    # print("length",length)
                    modified_RegistrationFees=modified_RegistrationFees+length
                elif len(modified_RegistrationFees)>maximum_length:
                     modified_RegistrationFees= modified_RegistrationFees[:maximum_length]
                
                else:
                  modified_RegistrationFees=RegistrationFees
                
                modified_ExamFees=[]
                if len(ExamFees)==0:
                   modified_ExamFees=[""]*maximum_length
                elif len(ExamFees)<maximum_length :
                  modified_ExamFees=[]
                  for fee in ExamFees:
                    modified_ExamFees.append(fee)
                    modified_ExamFees.append("")
                  if len(modified_ExamFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_ExamFees)))
                    # print("length",length)
                    modified_ExamFees=modified_ExamFees+length
                elif len(modified_ExamFees)>maximum_length:
                     modified_ExamFees= modified_ExamFees[:maximum_length]
                else:
                  modified_ExamFees=ExamFees
                
                modified_OtherFees=[]
                if len(OtherFees)==0:
                   modified_OtherFees=[""]*maximum_length
                elif len(OtherFees)<maximum_length :
                
                  # modified_OtherFees=[]
                  for fee in OtherFees:
                    
                    modified_OtherFees.append(fee)
                    modified_OtherFees.append("")
                  if len(modified_OtherFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_OtherFees)))
                    # print("length",length)
                    modified_OtherFees=modified_OtherFees+length
                elif len(modified_OtherFees)>maximum_length:
                     modified_OtherFees= modified_OtherFees[:maximum_length]
                else:
                  modified_OtherFees=OtherFees
                
                modified_TotalFees=[]
                if len(TotalFees)==0:
                   # print(len(TotalFees)==0)
                   modified_TotalFees=[""]*maximum_length
                elif len(TotalFees)<maximum_length:
                  
                  for fee in TotalFees:
                    modified_TotalFees.append(fee)
                    for index, value in enumerate(modified_TotalFees):
                      if value.startswith('Lakhs'):
                        modified_TotalFees[index] = ""
                  if len(modified_TotalFees)<maximum_length:
                    length=([""]*(maximum_length-len(modified_TotalFees)))
                    # print("length",length)
                    modified_TotalFees=modified_TotalFees+length
                elif len(modified_TotalFees)>maximum_length:
                     modified_TotalFees= modified_TotalFees[:maximum_length]
                    
                else:
                  modified_TotalFees=TotalFees
                  # print(len(modified_TotalFees))
                  for index, value in enumerate(modified_TotalFees):
                    if value.startswith('Lakhs'):
                      modified_TotalFees[index] = ""
              
            
            
            print("modified_year",modified_year)
            print("semester",semester)
            print("modified_AdmissionFees",modified_AdmissionFees)
            print("modified_TutionFees",modified_TutionFees)
            print("modified_RegistrationFees",modified_RegistrationFees)
            print("modified_ExamFees", modified_ExamFees)
            print("modified_OtherFees",modified_OtherFees)
            print("modified_TotalFees", modified_TotalFees)

            table_data_dic={"year":modified_year, "semester":semester, "AdmissionFees":modified_AdmissionFees,"TutionFees":modified_TutionFees,"RegistrationFees":modified_RegistrationFees,"ExamFees":modified_ExamFees,"OtherFees":modified_OtherFees,"Total Year Wise Fees":modified_TotalFees}
            # print("table_data_dic", type(table_data_dic))          
                            
            df = pd.DataFrame(table_data_dic)
                            
            # Create a DataFrame from course_name for each iteration
            college_df = pd.DataFrame({'Course_Name': [course_name]})
            # print("college_df", type(college_df))
            concatenated_df=[]
            if college_df.empty:
                continue
                # Concatenate college_df with df, setting ignore_index=True
            concatenated_df = pd.concat([college_df, df], ignore_index=True)
            if not concatenated_df.empty:
                course_fee_data.append(concatenated_df)
                

        except:
            print("oops! something went wrong")
            continue
    if course_fee_data is  None:
        pass
    else:
        college_fee_struture=pd.concat([name_df]+course_fee_data, ignore_index=True)
    
    return college_fee_struture



def find_the_page_to_process(driver,college_link):

  data_frames_list_2years=[]
  data_frames_list_3years=[]
  college = []
  # print("i am inside find page", college_link)
  driver.get(college_link)
  # Wait for the new page to load
  time.sleep(3)
  
  btech_links=driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/section/div[1]/div[1]/div/section/table/tbody')
                                             
  for element in btech_links:
    try: 
      a_tag = element.find_elements(By.TAG_NAME, "a")
      for tag in a_tag:
        print("btech tag", tag.text)
        if tag.text == "B.Tech":
          extracted_btech_link=tag.get_attribute("href")
          driver.get(extracted_btech_link)

          link_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/section/div[1]/div[1]/div/div[2]/div/div/div')
          # time.sleep(3)
          
          for element in link_elements:
            a_tag = element.find_elements(By.TAG_NAME, "a")
            if a_tag:
              tag = a_tag[0]
              college.append(tag.get_attribute("href"))
        
          
    except:
      print("no btech tag found")
      break
        
        
                 
  return college
# def find_the_page_to_process(driver,college_link):
#     # Initialize an empty list to store all the DataFrames
#         filtered_links=[]
#         college = []
#         data_frames_list_2years=[]
#         data_frames_list_3years=[]
#     # for college_name, college_link in college_data_df[13:]:
    
#     # for college_name, college_link in college:
#         print("i am inside find page", college_link)
#         driver.get(college_link)
#         # Wait for the new page to load
#         time.sleep(3)
    
#         Btech_link = driver.find_elements(By.LINK_TEXT, 'B.Tech')
#         if Btech_link:
#             links = []
#             for link in Btech_link:
#                 links.append(link.get_attribute('href'))
#             # for link in links: 
#             #     print(link)
#             extracted_mtech_link=""
#             if len(links) > 1:
#                 extracted_mtech_link = links[1]
#             else:
#                 print("list index out of range")
#             if  extracted_mtech_link:
#                 driver.get(extracted_mtech_link)
        
#                 link_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/section/div[1]/div[1]/div/div[2]/div/div/div')
                                                                
#                 # time.sleep(3)
                
#                 for element in link_elements:
#                     a_tag = element.find_elements(By.TAG_NAME, "a")
#                     if a_tag:
#                         tag = a_tag[0]
#                         college.append(tag.get_attribute("href"))
        
#                 # filtered_links = []
#                 # for link in college:
#                 #     if link.startswith("https://collegedunia.com/university") :
#                 #         filtered_links.append(link)
#         return college

def load_webpage_and_save_data(driver):

    # Load the webpage containing the table
    driver.get("https://collegedunia.com/btech-colleges")
    screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
    i=1
    scroll_pause_time = 25
    college_data = []
    retry_count = 10 # Number of times to retry
    retry_scroll_pause_time=10 
    while retry_count > 0:
        try:
            # Scroll the page until we have collected data for all colleges
            while len(college_data)<4277:
                i += 1
                # find the table where the first column starts with #.
                tables = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/section/div/div[2]/div/div[3]/div/div/div/div/table/tbody/tr[starts-with(td[1], "#")]')
            
                # Iterate over each table to find the name and link
                for table in tables:
                    h_tag = table.find_elements(By.TAG_NAME, "h3")
                    if h_tag:
                        name = h_tag[0].text
            
                    a_tag = table.find_elements(By.TAG_NAME, "a")
                    if a_tag:
                        
                        tag = a_tag[0]
                        link = tag.get_attribute("href")
                        # if link.startswith("https://collegedunia.com/university") :
                        if (name, link) in college_data:
                            pass
                        else:
                            college_data.append((name, link))
                        df=pd.DataFrame(college_data)
                        df=df.to_csv(r"C:\Users\tmaas\OneDrive\Desktop\web_scrapping\btech_data\btech_all_data.csv", index=False)
                        
                        
                if len(college_data)==4276:
                    break
            
                # Scroll the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)
                # Check if reaching the end of the page
                scroll_height = driver.execute_script("return document.body.scrollHeight;")
                if screen_height * i > scroll_height:
                    break
                
            break  # Break the retry loop if data is successfully collected
    
        except:
            print("retrying")
            retry_count-=1
            time.sleep(retry_scroll_pause_time)
            if retry_count==0:
                print("Maximum retry attempts reached. Exiting...")
                break
    return df


def main():    
    file_path=r"C:\Users\tmaas\Downloads\filtered_df_1.csv"
    # Define a list to store tuples of (name, link) for each college
    btech_college_info=[]
    # Open the file in 'r' mode
    with open(file_path, 'r', newline='') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile)
    
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Each row is a list where the first element is the college name and the second element is the college link
            college_name = row[0]
            college_link = row[1]
            btech_college_info.append((college_name, college_link))
    # print(len(btech_college_info))
    # print(btech_college_info[4044])
    # print(btech_college_info[])
    # Initialize an empty list to store all the DataFrames
    no_data_list=[]
    data_frames_list = []
    retry_count = 10 # Number of times to retry
    retry_scroll_pause_time=10 
    
    for college_name,college_link in btech_college_info[1:1000]:
        print(college_name, college_link)
        filtered_link=find_the_page_to_process(driver,college_link)
        if filtered_link!=[]:
            result = btech_fee_structure(driver,college_name, filtered_link)
            data_frames_list.append(result)
        else:
            no_data_list.append((college_name, college_link))
            df=pd.DataFrame(no_data_list)
            df.to_csv(r"C:\Users\tmaas\OneDrive\Desktop\web_scrapping\btech_data\no_data_list_1_1000.csv", index=False)
        # print(len(data_frames_list))   
        if data_frames_list != []:      
            # Concatenate the DataFrames in the list into a single DataFrame
            concatenated_df = pd.concat(data_frames_list, ignore_index=True)
            print(len(concatenated_df))                    
            # save to file
            concatenated_df.to_csv(r"C:\Users\tmaas\OneDrive\Desktop\web_scrapping\btech_data\data_list_1_1000.csv.csv", index=False)
        else:
            no_data_list.append((college_name, college_link))
            
    print("data have been saved to file")
    print(len(no_data_list))
    print(no_data_list)
    driver.quit()
if __name__ == "__main__":
    main()