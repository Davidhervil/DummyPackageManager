from enum import Enum

class Command(Enum):
    # Using an Enum prevents from having typos when referencing commands
    DEPEND = 0
    INSTALL = 1
    REMOVE = 2
    LIST = 3
    END = 4

class PackageManager():

    def __init__(self) -> None:
        # Dicts to represent a adirectional graph of dependencies
        self.downwards_dependencies = {}
        self.upwards_dependencies = {}
        # Set of installed packages. We use a set becasue we'll be checking if an item
        # is in it generally more than iterating over it. This also saves us the work when
        # "installing" shared dependencies 
        # but in a real life scenario we DO NEED TO CHECK IF THEY'RE ALREADY INSTALLED
        self.installed = set()
        # Set to mark manually installed packages
        self.manually_installed = set()

    def add_dependency(self, package, dependency_package):
        # We store the dependency of the package and also mark upwards dependencies
        # We do this so we know when a package can be safely deleted
        if package not in self.downwards_dependencies:
            self.downwards_dependencies[package] = {dependency_package}
        else:
            self.downwards_dependencies[package].add(dependency_package)
        
        # Upwards dependencies
        if dependency_package not in self.upwards_dependencies:
            self.upwards_dependencies[dependency_package] = {package}
        else:
            self.upwards_dependencies[dependency_package].add(package)

    def manage_depenencies(self, package, dependencies):
        for dependency in dependencies:
            self.add_dependency(package, dependency)

        if len(dependencies) == 0:
            print(f"Wrong usage of DEPEND command on package {package}. Aborting")
            exit()

    def install(self, package, manually):
        # We mark each dependency accordingly if they were manually installed
        # by putting their name in the manually_instaled set
        # for later when we need to removed them automatically (or not)
        if package in self.installed:
            if manually:
                print(f"\t{package} is already installed")
            return
        
        # Install dependencies
        if package in self.downwards_dependencies:
            for dependency in self.downwards_dependencies[package]:
                self.install(dependency, False)
        
        self.installed.add(package)
        if manually:
            self.manually_installed.add(package)

        print(f"\t{package} successfully installed")

    def remove(self, package, automatic):
        # Check if is instaleld
        if package not in self.installed:
            print(f"\t{package} is not installed")
            return
        # Check if there is no other package dependant on it
        if package in self.upwards_dependencies:
            for dependant in self.upwards_dependencies[package]:
                if dependant in self.installed:
                    if not automatic:
                        print(f"\t{package} is still needed")
                    return

        if automatic:
            print(f"\t{package} is no longer needed")

        # "Uninstall" it
        self.installed.remove(package)
        if package in self.manually_installed:
            self.manually_installed.remove(package)
        print(f"\t{package} successfully removed")
        
        # Check for automatic removal of non manually installed dependencies
        if package in self.downwards_dependencies:
            for dependency in self.downwards_dependencies[package]:
                if dependency in self.installed and (dependency not in self.manually_installed):
                    self.remove(dependency, True)
        
    def showInstalled(self):
        for package in self.installed:
            print(f"\t{package}")

    def run(self):
        # We check for user input on each iteration and kill it
        # if we find END
        user_input = None
        while(user_input != Command.END.name):
            user_input = input()
            print(user_input)
            
            input_content = user_input.split()
            if len(input_content) == 0:
                print("No input was introduced. Aborting.")
                exit()

            else:
                command = input_content[0]
                if command not in Command._member_names_:
                    print("Unknown command. Aborting")
                    exit()
                command = Command[command]
                if command == Command.DEPEND:
                    if not (len(input_content) > 2):
                        print(f"Wrong usage of DEPEND command. Aborting")
                        exit()
                    self.manage_depenencies(input_content[1], input_content[2:])

                if command == Command.INSTALL:
                    if len(input_content) != 2 :
                        print(f"Wrong usage of INSTALL command. Aborting")
                        exit()
                    self.install(input_content[1], True)

                if command == Command.REMOVE:
                    if len(input_content) != 2 :
                        print(f"Wrong usage of REMOVE command. Aborting")
                        exit()
                    self.remove(input_content[1], False)

                if command == Command.LIST:
                    self.showInstalled()
        
        print(Command.END.name)
