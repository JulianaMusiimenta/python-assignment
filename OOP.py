#OOP's(Object Oriented Programming)
#An object is also an instance,it is found in a class
#Here we create objects that do not exist and we give them classes,objects
#Modeling-Trying to identify classes and attributes in each class
#The things that we want the class to do are the methods

#Examples
#1.Creating classes 
#Classes names always start with a capital letter and it's always singular.
#Syntax class Name:
# Cohort class:
    # name
    # description
    # start_date
    # end_date
    # total_number_of_students
    # All the objects are strings.
    
#Within the cohort class:
#Add a constructor for the cohort class.hint read about constructors

class Cohort:
    def __init__(self, name, description, start_date, end_date, total_number_of_students):
        # Initializing the attributes of the cohort
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_number_of_students = total_number_of_students

    def __str__(self):
        # Provide a string representation of the cohort
        print(f"Cohort Name: {self.name}\nDescription: {self.description}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nTotal Students: {self.total_number_of_students}")

# Example usage:
cohort4 = Cohort(
    name=" Cohort4 class 2024",
    description="A commited class",
    start_date="2024-11-10",
    end_date="2024-06-12",
    total_number_of_students="58"
)
print(cohort4)


#Add a method(function to the class that prints the cohort name and the total number of student

class Cohort:
    def __init__(self, name, description, start_date, end_date, total_number_of_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_number_of_students = total_number_of_students

    # Method to print the cohort name and total number of students
    def print_cohort_info(self):
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {self.total_number_of_students}")

 # Example usage:
cohort4 = Cohort("Python course unit", "A logical course unit ", "2024-01-01", "2024-06-30", "60")
cohort4.print_cohort_info()

#3 Create a new instance(object) of the cohort class.hint newCohort = Cohort()


# Create a new cohort with name and start date
cohort5 = Cohort(
    name=" Cohort5 class 2024",
    description="Assured class",
    start_date="2025-11-10",
    end_date="2025-06-12",
    total_number_of_students="90"
)
print(cohort5)


