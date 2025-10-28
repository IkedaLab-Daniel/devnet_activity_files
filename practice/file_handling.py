print("=" * 50)
print("        PYTHON FILE HANDLING PRACTICE")
print("=" * 50)

import os
import json
import csv
from datetime import datetime

# =============================================================================
# BASIC FILE OPERATIONS
# =============================================================================
print("\n1. BASIC FILE OPERATIONS")
print("-" * 27)

# Creating and writing to a file
print("Creating and writing to a file:")
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is easy!\n")
print("✓ File 'sample.txt' created and written to")

# Reading from a file
print("\nReading from the file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("Reading line by line:")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# =============================================================================
# FILE MODES
# =============================================================================
print("\n2. FILE MODES")
print("-" * 14)

print("Available file modes:")
print("'r' - Read (default)")
print("'w' - Write (overwrites existing)")
print("'a' - Append")
print("'r+' - Read and write")
print("'x' - Exclusive creation (fails if file exists)")

# Append mode example
print("\nAppending to file:")
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write(f"Timestamp: {datetime.now()}\n")

print("File after appending:")
with open("sample.txt", "r") as file:
    print(file.read())

# =============================================================================
# USING 'WITH' KEYWORD (CONTEXT MANAGERS)
# =============================================================================
print("\n3. USING 'WITH' KEYWORD")
print("-" * 25)

print("Benefits of using 'with':")
print("- Automatically closes file even if error occurs")
print("- Cleaner, more readable code")
print("- Proper resource management")

# Bad practice (without 'with')
print("\nWithout 'with' (not recommended):")
file = open("temp.txt", "w")
file.write("This is temporary content")
file.close()  # Must remember to close!

# Good practice (with 'with')
print("With 'with' statement (recommended):")
with open("temp.txt", "w") as file:
    file.write("This is better content")
# File automatically closed here

# Multiple files with 'with'
print("\nUsing 'with' for multiple files:")
with open("input.txt", "w") as input_file, open("output.txt", "w") as output_file:
    input_file.write("Input data")
    output_file.write("Output data")
print("✓ Both files created and automatically closed")

# =============================================================================
# FILE READING METHODS
# =============================================================================
print("\n4. FILE READING METHODS")
print("-" * 26)

# Create a sample file with multiple lines
sample_content = """Line 1: First line
Line 2: Second line
Line 3: Third line
Line 4: Fourth line
Line 5: Fifth line"""

with open("multiline.txt", "w") as file:
    file.write(sample_content)

print("Methods to read files:")

# Method 1: read() - entire file
print("\n1. read() - entire file:")
with open("multiline.txt", "r") as file:
    content = file.read()
    print(repr(content))

# Method 2: readline() - one line at a time
print("\n2. readline() - one line at a time:")
with open("multiline.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"First: {repr(first_line)}")
    print(f"Second: {repr(second_line)}")

# Method 3: readlines() - all lines as list
print("\n3. readlines() - all lines as list:")
with open("multiline.txt", "r") as file:
    lines = file.readlines()
    print(f"All lines: {lines}")

# Method 4: Iterating over file object
print("\n4. Iterating over file object:")
with open("multiline.txt", "r") as file:
    for line in file:
        print(f"Processing: {line.strip()}")

# =============================================================================
# FILE WRITING METHODS
# =============================================================================
print("\n5. FILE WRITING METHODS")
print("-" * 26)

# write() method
with open("write_example.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

# writelines() method
lines_to_write = ["Third line\n", "Fourth line\n", "Fifth line\n"]
with open("write_example.txt", "a") as file:
    file.writelines(lines_to_write)

print("File after writing:")
with open("write_example.txt", "r") as file:
    print(file.read())

# =============================================================================
# FILE MODIFICATION
# =============================================================================
print("\n6. FILE MODIFICATION")
print("-" * 21)

print("Original file content:")
with open("write_example.txt", "r") as file:
    original_lines = file.readlines()
    for i, line in enumerate(original_lines, 1):
        print(f"{i}: {line.strip()}")

# Modify specific lines
print("\nModifying file (replacing 'line' with 'LINE'):")
modified_lines = []
for line in original_lines:
    modified_line = line.replace("line", "LINE")
    modified_lines.append(modified_line)

# Write back the modified content
with open("write_example.txt", "w") as file:
    file.writelines(modified_lines)

print("Modified file content:")
with open("write_example.txt", "r") as file:
    print(file.read())

# =============================================================================
# FILE DELETION
# =============================================================================
print("\n7. FILE DELETION")
print("-" * 17)

# Create a temporary file for deletion demo
with open("temp_delete.txt", "w") as file:
    file.write("This file will be deleted")

print("Files before deletion:")
files_before = [f for f in os.listdir(".") if f.endswith(".txt")]
print(files_before)

# Delete the file
if os.path.exists("temp_delete.txt"):
    os.remove("temp_delete.txt")
    print("✓ File 'temp_delete.txt' deleted")

print("Files after deletion:")
files_after = [f for f in os.listdir(".") if f.endswith(".txt")]
print(files_after)

# Safe deletion with error handling
def safe_delete(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"✓ Successfully deleted {filename}")
        else:
            print(f"⚠ File {filename} does not exist")
    except PermissionError:
        print(f"✗ Permission denied: Cannot delete {filename}")
    except Exception as e:
        print(f"✗ Error deleting {filename}: {e}")

safe_delete("nonexistent.txt")

# =============================================================================
# WORKING WITH JSON FILES
# =============================================================================
print("\n8. WORKING WITH JSON FILES")
print("-" * 28)

# Create sample data
student_data = {
    "students": [
        {"name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Physics"]},
        {"name": "Bob", "age": 19, "grade": "B", "subjects": ["Chemistry", "Biology"]},
        {"name": "Charlie", "age": 21, "grade": "A", "subjects": ["Math", "Computer Science"]}
    ],
    "created": datetime.now().isoformat()
}

# Writing JSON to file
print("Writing JSON data to file:")
with open("students.json", "w") as file:
    json.dump(student_data, file, indent=2)
print("✓ JSON data written to 'students.json'")

# Reading JSON from file
print("\nReading JSON data from file:")
with open("students.json", "r") as file:
    loaded_data = json.load(file)

print(f"Loaded {len(loaded_data['students'])} students:")
for student in loaded_data['students']:
    print(f"- {student['name']}: Grade {student['grade']}, Age {student['age']}")

# Modifying JSON data
print("\nModifying JSON data:")
loaded_data['students'].append({
    "name": "Diana", 
    "age": 20, 
    "grade": "A+", 
    "subjects": ["Art", "Literature"]
})

# Write back modified data
with open("students.json", "w") as file:
    json.dump(loaded_data, file, indent=2)
print("✓ JSON data modified and saved")

# =============================================================================
# WORKING WITH CSV FILES
# =============================================================================
print("\n9. WORKING WITH CSV FILES")
print("-" * 27)

# Writing CSV data
print("Writing CSV data:")
csv_data = [
    ["Name", "Age", "City", "Salary"],
    ["Alice", 25, "New York", 50000],
    ["Bob", 30, "London", 55000],
    ["Charlie", 28, "Tokyo", 48000],
    ["Diana", 26, "Paris", 52000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print("✓ CSV data written to 'employees.csv'")

# Reading CSV data
print("\nReading CSV data:")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read headers
    print(f"Headers: {headers}")
    
    for row_num, row in enumerate(reader, 1):
        print(f"Row {row_num}: {row}")

# Working with CSV using DictReader
print("\nUsing CSV DictReader:")
with open("employees.csv", "r") as file:
    dict_reader = csv.DictReader(file)
    for employee in dict_reader:
        print(f"{employee['Name']} ({employee['Age']}) works in {employee['City']}")

# =============================================================================
# FILE AND DIRECTORY OPERATIONS
# =============================================================================
print("\n10. FILE AND DIRECTORY OPERATIONS")
print("-" * 35)

print("Current working directory:")
print(os.getcwd())

print("\nFiles in current directory:")
files = [f for f in os.listdir(".") if os.path.isfile(f)]
print(files[:10])  # Show first 10 files

print("\nFile information:")
if os.path.exists("sample.txt"):
    stat = os.stat("sample.txt")
    print(f"Size: {stat.st_size} bytes")
    print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")

# Create directory
directory_name = "practice_files"
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"✓ Directory '{directory_name}' created")

# Move files to directory (simulation)
sample_files = ["sample.txt", "multiline.txt", "write_example.txt"]
for filename in sample_files:
    if os.path.exists(filename):
        new_path = os.path.join(directory_name, filename)
        # In real scenario, you'd use shutil.move()
        print(f"Would move {filename} to {new_path}")

# =============================================================================
# ERROR HANDLING IN FILE OPERATIONS
# =============================================================================
print("\n11. ERROR HANDLING")
print("-" * 20)

def safe_read_file(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'"
    except Exception as e:
        return f"Unexpected error: {e}"

# Test error handling
print("Testing error handling:")
print(safe_read_file("sample.txt"))  # Should work
print(safe_read_file("nonexistent.txt"))  # Should show error

def safe_write_file(filename, content):
    """Safely write to a file with error handling"""
    try:
        with open(filename, "w") as file:
            file.write(content)
            return f"✓ Successfully wrote to '{filename}'"
    except PermissionError:
        return f"✗ Permission denied: Cannot write to '{filename}'"
    except Exception as e:
        return f"✗ Error writing to '{filename}': {e}"

print(safe_write_file("test_safe.txt", "Safe writing test"))

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n12. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Log file processor
def create_sample_log():
    """Create a sample log file"""
    log_entries = [
        "2024-01-01 10:30:15 INFO User logged in: alice",
        "2024-01-01 10:31:22 ERROR Database connection failed",
        "2024-01-01 10:32:10 INFO User logged in: bob",
        "2024-01-01 10:33:45 WARNING Low disk space",
        "2024-01-01 10:34:20 ERROR File not found: config.txt",
        "2024-01-01 10:35:15 INFO User logged out: alice"
    ]
    
    with open("app.log", "w") as file:
        for entry in log_entries:
            file.write(entry + "\n")
    
    return len(log_entries)

def analyze_log_file(filename):
    """Analyze log file and count different log levels"""
    log_counts = {"INFO": 0, "ERROR": 0, "WARNING": 0}
    
    try:
        with open(filename, "r") as file:
            for line in file:
                for level in log_counts:
                    if level in line:
                        log_counts[level] += 1
                        break
        
        return log_counts
    except FileNotFoundError:
        return "Log file not found"

print("Creating and analyzing log file:")
entries_created = create_sample_log()
print(f"Created {entries_created} log entries")

log_analysis = analyze_log_file("app.log")
print("Log analysis:")
for level, count in log_analysis.items():
    print(f"{level}: {count}")

# Example 2: Configuration file manager
def create_config_file():
    """Create a configuration file"""
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "username": "admin"
        },
        "app": {
            "debug": True,
            "max_users": 100,
            "timeout": 30
        }
    }
    
    with open("config.json", "w") as file:
        json.dump(config, file, indent=2)
    
    return config

def load_config():
    """Load configuration from file"""
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return create_config_file()  # Create default config

print("\nConfiguration file example:")
config = load_config()
print(f"Database host: {config['database']['host']}")
print(f"Max users: {config['app']['max_users']}")

# =============================================================================
# CLEANUP
# =============================================================================
print("\n13. CLEANUP")
print("-" * 12)

# List of files created during this practice
created_files = [
    "sample.txt", "temp.txt", "input.txt", "output.txt", 
    "multiline.txt", "write_example.txt", "students.json", 
    "employees.csv", "test_safe.txt", "app.log", "config.json"
]

print("Files created during this practice session:")
for filename in created_files:
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"- {filename} ({file_size} bytes)")

print("\nTo clean up these files, you can run:")
print("import os")
print("files_to_delete = [", end="")
print(", ".join([f"'{f}'" for f in created_files]), end="")
print("]")
print("for file in files_to_delete:")
print("    if os.path.exists(file):")
print("        os.remove(file)")

print("\n" + "=" * 50)
print("       END OF FILE HANDLING PRACTICE")
print("=" * 50)

print("\n📚 SUMMARY:")
print("✓ File creation, reading, writing, and deletion")
print("✓ Different file modes and their uses")
print("✓ Context managers with 'with' keyword")
print("✓ JSON and CSV file handling")
print("✓ Error handling and safe file operations")
print("✓ Practical examples and best practices")