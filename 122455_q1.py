#	Adding a New Patient: We’ll create a list to store patient dictionaries. Each dictionary will have keys for “name,” “age,” and “illness.” Here’s an example function to add a new patient:
def add_patient(patients_list, name, age, illness):
	   
        """
	    #  Adds a new patient to the list of patients.
	
	    Args:
	        patients_list (list[dict]): List of patient dictionaries.
	        name (str): Name of the patient.
	        age (int): Age of the patient.
	        illness (str): Description of the patient's illness.
	
	    Returns:
	        None
	    """

new_patient = {"name": name, "age": age, "illness": illness}  # type: ignore
patients_list.append(new_patient) # type: ignore

# Example usage:
patients = []  # Initialize an empty list for patients
add_patient(patients, "sydney sweney", 35, "Headache")
	
    # Displaying All Patients: We’ll iterate through the list of patients and print their details. Here’s an example function:

def display_all_patients(patients_list):
	    """
	    Displays details of all patients.
	
	    Args:
	        patients_list (list[dict]): List of patient dictionaries.

    Returns:
        None
	    """
for patient in patients_list:
	        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

	# Example usage:
display_all_patients(patients)

# Searching for a Patient by Name: We’ll search for a patient by their name and return their details if found. Here’s an example function:

def search_patient_by_name(patients_list, target_name):
    """
	    Searches for a patient by name and displays their details if found.
	
	    Args:
	        patients_list (list[dict]): List of patient dictionaries.
	        target_name (str): Name of the patient to search for.
	
	    Returns:
	        None
	    """
for patient in patients_list:
       if patient['name'] == target_name:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
        return
print(f"Patient '{target_name}' not found.")
	
	# Example usage:
search_patient_by_name(patients, "Sydney Sweney")
	# Removing a Patient by Name: We’ll remove a patient from the list by their name. Here’s an example function:
def remove_patient_by_name(patients_list, target_name):
	    """
    Removes a patient from the list by name.
	
    Args:
        patients_list (list[dict]): List of patient dictionaries.
        target_name (str): Name of the patient to remove.
	
	    Returns:
	        None
	    """
for patient in patients_list:
      if patient['name'] == target_name:
	            patients_list.remove(patient)
print(f"Patient '{target_name}' removed.")
return
print(f"Patient '{target_name}' not found.")
	
	# Example usage:
remove_patient_by_name(patients, "Sydney Sweney")
	# Exiting the Program: You can use a while loop to keep the program running until the user chooses to exit. For example:
while True:
	    print("\nMenu:")
print("1. Add a new patient")
print("2. Display all patients")
print("3. Search for a patient by name")
print("4. Remove a patient by name")  
print("5. Exit")

choice = input("Enter your choice (1-5): ")
if choice == "1":
        # Call add_patient function
        pass
elif choice == "2":
	        # Call display_all_patients function
	        pass
elif choice == "3":
	        # Call search_patient_by_name function
       pass
elif choice == "4":
        # Call remove_patient_by_name function
        pass
elif choice == "5":
	        print("Exiting the program.")
break
else:
print("Invalid choice. Please enter a valid option.")
