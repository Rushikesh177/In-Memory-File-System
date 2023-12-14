import os
import json

class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = '/'
        self.file_system = {}

    def mkdir(self, directory_name):
        new_directory = os.path.join(self.current_directory, directory_name)
        self.file_system[new_directory] = {}
        return f"Directory '{new_directory}' created."

    def cd(self, path):
        if path == '/':
            self.current_directory = '/'
        elif path.startswith('/'):
            self.current_directory = path
        else:
            self.current_directory = os.path.join(self.current_directory, path)
        return f"Current directory: {self.current_directory}"

    def ls(self, path='.'):
        target_path = os.path.normpath(os.path.join(self.current_directory, path)).replace('\\', '/')

        if target_path == '/':
            return f"Contents of {target_path}: {list(self.file_system.keys())}"
        elif target_path in self.file_system and isinstance(self.file_system[target_path], dict):
            return f"Contents of {target_path}: {list(self.file_system[target_path].keys())}"
        else:
            return f"Contents of {target_path}: {self.file_system.get(target_path, 'Not a directory or file')}"

    def touch(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        self.file_system[file_path] = ''
        return f"File '{file_path}' created."

    def cat(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        if file_path in self.file_system and isinstance(self.file_system[file_path], str):
            return self.file_system[file_path]
        else:
            return f"{file_path} is not a file."

    def echo(self, *args):
        text = ' '.join(args[:-1]).strip()
        filename = args[-1]
        file_path = os.path.join(self.current_directory, filename)
        self.file_system[file_path] = text
        return f"Text written to '{file_path}'."

    def mv(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system.pop(source_path)
            return f"{source_path} moved to {destination_path}."
        else:
            return f"{source_path} not found."

    def cp(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system[source_path]
            return f"{source_path} copied to {destination_path}."
        else:
            return f"{source_path} not found."

    def rm(self, path):
        target_path = os.path.join(self.current_directory, path)
        if target_path in self.file_system:
            self.file_system.pop(target_path)
            return f"{target_path} removed."
        else:
            return f"{target_path} not found."

    def save_state(self, filename):
        with open(filename, 'w') as f:
            json.dump({'current_directory': self.current_directory, 'file_system': self.file_system}, f)
        return "File system state saved."

    def load_state(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.current_directory = data['current_directory']
            self.file_system = data['file_system']
        return "File system state loaded."


if __name__ == "__main__":
    file_system = InMemoryFileSystem()

    while True:
        command = input("Enter command (type 'exit' to end): ").split(' ')
        operation = command[0]

        if operation == 'exit':
            break

        args = command[1:]
        result = getattr(file_system, operation)(*args)
        print(result)
