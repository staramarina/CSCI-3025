# example taken from www.geeksforgeeks.org/python/extract-nested-data-from-complex-json/

# Complex dictionary with nested structures
data = {
    "location": {
        "country": "India",
        "state": "Uttar Pradesh",
        "city": "Greater Noida"
    },
    "organizations": [
        {
            "name": "GeeksforGeeks",
            "type": "Educational",
            "departments": ["Computer Science", "Mathematics", "Physics"]
        },
        {
            "name": "TechCorp",
            "type": "Technology",
            "departments": ["Software Development", "Hardware Design"]
        }
    ],
    "projects": {
        "ongoing": ["ProjectA", "ProjectB"],
        "completed": ["ProjectX", "ProjectY"]
    }
}


# Extract nested data using dot notation
country_dot = data["location"]["country"]
city_dot = data["location"]["city"]

print(f"Extracted Data using Dot Notation:")
print(f"Country: {country_dot}")
print(f"City: {city_dot}")

Extracted Data using Dot Notation:
Country: India
City: Greater Noida


# Extract nested data using list comprehension
edu_departments = [dept for org in data["organizations"]
                   if org["name"] == "GeeksforGeeks" for dept in org["departments"]]
completed_projects = [project for status, projects in data["projects"].items(
) if status == "completed" for project in projects]

print(f"Extracted Data using List Comprehension:")
print(f"Educational Departments: {edu_departments}")
print(f"Completed Projects: {completed_projects}")

Extracted Data using List Comprehension:
Educational Departments: ['Computer Science', 'Mathematics', 'Physics']
Completed Projects: ['ProjectX', 'ProjectY']


# Extract nested data using recursion
def extract_data_recursive(data, keys):
    return data[keys[0]] if len(keys) == 1 else extract_data_recursive(data[keys[0]], keys[1:])


edu_department_recursive = extract_data_recursive(
    data, ["organizations", 0, "departments", 0])

print(f"Extracted Data using Recursion:")
print(f"Educational Department (Recursive): {edu_department_recursive}")

Extracted Data using Recursion:
Educational Department (Recursive): Computer Science
