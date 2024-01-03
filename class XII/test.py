import struct

def write_sample_binary_file(file_path):
    # Sample student records
    students = [
        ('S001', 'Alice', 80.5),
        ('S002', 'Bob', 65.2),
        ('S003', 'Charlie', 90.0),
        ('S004', 'David', 72.8),
        ('S005', 'Eva', 85.3),
    ]

    try:
        with open(file_path, 'wb') as file:
            for student in students:
                s_admno, s_name, percentage = student
                # Assuming the encoding of strings is utf-8
                s_admno_bytes = s_admno.encode('utf-8')
                s_name_bytes = s_name.encode('utf-8')
                record = struct.pack('12s 12s f', s_admno_bytes, s_name_bytes, percentage)
                file.write(record)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

# Example usage to create a sample binary file
write_sample_binary_file('STUDENT.DAT')
