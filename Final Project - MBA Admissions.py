File = open("Student List.txt","r")                #import file 
print("MARYVILLE UNIVERSITY IS WELL-KNOWN AS ONE OF THE BEST MBA PROGRAM WITH VERY COMPETITIVE ADMISSION RATE ")
Input = int(input("PLEASE ENTER AN INTEGER AS THE ADMISSION RATE(%) FOR THIS YEAR.  : "))
imported_list = []                             # define list variable, custom list, and admission list 
student_list = []
custom_list = []
admission_list = []


class Student:                                      # define class Student
    def __init__(self,student_list,accepted_list):  # 2 parameters 
        self.student_list = student_list
        self.accepted_list = accepted_list          #define instance variables 
        self.male = 0 
        self.female = 0 
        self.age1 = 0 
        self.age2 = 0
        self.age3 = 0 
        self.north_america = 0
        self.asia = 0
        self.europe = 0
        self.africa = 0
        self.latin_america = 0
    
    def getCountry(self,admission_list):                      #function to get countries of applicants
        for i in admission_list:
            if i[2] in ["America","Canada"]:
                self.north_america += 1
            elif i[2] in ["India","Taiwan","Vietnam","Korean","Russia"]:
                self.asia += 1
            elif i[2] in ["Nigeria","Egypt"]:
                self.africa += 1
            elif i[2] in ["Brazil","Mexico"]:
                self.latin_america += 1
            else: self.europe += 1
            
    def getCountryPerc1(self,admission_list):                  #Accessor to return country value 
        return (self.north_america/len(admission_list))*100
    
    def getCountryPerc2(self,admission_list):                  #Accessor to return country value 
        return (self.asia/len(admission_list))*100
    
    def getCountryPerc3(self,admission_list):                 #Accessor to return country value 
        return (self.africa/len(admission_list))*100
    
    def getCountryPerc4(self,admission_list):                 #Accessor to return country value 
        return (self.latin_america/len(admission_list))*100
    
    def getCountryPerc5(self,admission_list):                 #Accessor to return country value 
        return (self.europe/len(admission_list))*100
        
    def getAge(self,admission_list):                          # Function to get student Age Range 
        for i in admission_list:
            if 18 <= int(i[3]) <= 25:
               self.age1 +=1
            elif 26 <= int(i[3]) <= 30:
                self.age2 +=1
            else:
                self.age3 +=1
                 
    def getAgePerc1(self,admission_list):                     #Accessor to return Age Range value  
        return (self.age1/len(admission_list))*100
    
    def getAgePerc2(self,admission_list):                      #Accessor to return Age Range value  
        return (self.age2/len(admission_list))*100
    
    def getAgePerc3(self,admission_list):                       #Accessor to return Age Range value  
        return (self.age3/len(admission_list))*100
    
    
    def getGender(self,admission_list):                        # Function to get Gender informatio from Applicants 
        for i in admission_list:
            if i[1] == "Female":
                self.female +=1
            else:
                self.male +=1
                
    def getGenderPerc1(self,admission_list):                   #Accessor to return Gender value  
        return (self.male/len(admission_list))*100
    
    def getGenderPerc2(self,admission_list):                   #Accessor to return Gender value
        return (self.female/len(admission_list))*100
    
    def getScore(self):
        return self.accepted_list
    
    def get_admission_list(self,student):
        for j in self.student_list:
            if j[0] in student[0]:
                return(j)
    
class Stack:                       # Using Stack as a Data Structure to store student information 
    def __init__(self):
        self.stack = []            # Define empty stack 
        
    def Insert(self,student):      # Append Student into a stack from the end 
        self.stack.append(student)

        
    def Pop(self):                  # Pop student off the stack from the end 
        self.stack.pop()
    
    def sortByScore(self):            # Sort Algorithm used to sort the student lists by Gmat Score and then Name Alphabet
        self.stack = sorted(sorted(self.stack, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
    
    def getSortedList(self):          # Accessor to return value of stack 
        return self.stack
    
def getList():                       # Function to handle lists from the imported file
    for line in File:                          # Appending every single line in the file
        imported_list.append(line) 
    for item in imported_list:
        student_info = item.strip("\n")           # Strip \n at the end
        student_info = student_info.split("\t")         # Split any Tab between text and turn into list                        
        custom_list.append((student_info[0],int(student_info[4])))
        student_list.append(student_info)           # Return student list
    
    for student in custom_list:                  # Insert each student into list
        stack.Insert(student)
        
    for student in range(len(custom_list) - int((Input/100)*len(custom_list))):      # Pop any imqualified student. 
        stack.Pop()
        
    return custom_list, student_list  ,stack.getSortedList()    #Return list value 

def getAdmissionList():                                         # Get Admission list base on Input %
    for i in stack.getSortedList():
        student.get_admission_list(i)
        admission_list.append(student.get_admission_list(i))
        
        
        
stack = Stack()                     # Assign object 
getList()                            # Get student list 
stack.sortByScore()                  # Sort by score
student = Student(student_list,stack.getSortedList()) # Pass argument into a object
getAdmissionList()

def main():
    
    print("THE ADMISSION RATE IS {0}%, WE ARE ACCEPTING {1} APPLICANTS THIS YEAR".format(Input,int((Input/100)*len(custom_list)))) # Print statement 
    print("******************************************************")
    print("  NAME","        ","   GENDER","        "," COUNTRY","       ","AGE","      ","GMAT_SCORE") 
    for i in admission_list:                                                            # For each student in admission list, print following information 
        print(i[0],"        ",i[1],"        ",i[2],"        ",i[3],"        ",i[4])
    print("******************************************************")    
    student.getGender(admission_list)                                                   # Call function to perform task
    print("The Acceptance Rate For Male Applicant is   : {0:0.2f}%\nThe Acceptance Rate For Female Applicant is : {1:0.2f}%".format(student.getGenderPerc1(admission_list),student.getGenderPerc2(admission_list)))
    print("******************************************************")
    student.getAge(admission_list)                                                      # Call function to perform task
    print("The Average Age Range are\n 18-25 yrs: {0:0.2f}%\n 26-30 yrs: {1:0.2f}%\n 31+ yrs  : {2:0.2f}%"\
          .format(student.getAgePerc1(admission_list),student.getAgePerc2(admission_list),student.getAgePerc3(admission_list)))      #print following information 
    student.getCountry(admission_list)
    print("******************************************************")
    print("Acceptance Rate From Country Are:\nNorth_America : {0:0.2f}%\nAsia          : {1:0.2f}%\nAfrica        : {2:0.2f}%\nLatin_America : {3:0.2f}%\nEurope        : {4:0.2f}% "\
          .format(student.getCountryPerc1(admission_list),student.getCountryPerc2(admission_list),student.getCountryPerc3(admission_list),student.getCountryPerc4(admission_list),student.getCountryPerc5(admission_list)))
    
main()





        



