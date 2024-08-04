filename = input("Input the Filename: ")
file_parts = filename.split(".")
extension = file_parts[-1]
extension_mapping = {
    'py': 'python',
    'txt': 'text',
    'cpp': 'C++',
    'java': 'Java',
    'js': 'JavaScript',
    'html': 'HTML',
    'css': 'CSS',
    'rb': 'Ruby',
    'go': 'Go',
    'php': 'PHP',
}
extension_name = extension_mapping.get(extension, 'unknown')
print(f"The extension of the file is: '{extension_name}'")
