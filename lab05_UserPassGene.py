name = input("Enter your full name: ")
roll = input("Enter your roll number: ")

#extra spaces
name = name.strip()

#multiple spaces
name = " ".join(name.split())

#Convert to lowercase
name = name.lower()

#unwanted punctuation
name = name.replace(",", "").replace(".", "").replace("-", "")

# Generate u_name
username = name.replace(" ", ".") + "." + roll.lower()

#Generate email
email = f"{username}@college.edu"

print("Username:", username)
print("Email:", email)
