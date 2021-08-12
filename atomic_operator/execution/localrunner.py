from ..base import Base


class LocalRunner(Base):
    """Runs AtomicTest objects locally
    """

    def __init__(self, atomic_test):
        """A single AtomicTest object is provided and ran on the local system

        Args:
            atomic_test (AtomicTest): A single AtomicTest object.
        """
        self.test = atomic_test
        self.__local_system_platform = self.get_local_system_platform()

    def __get_executor_command(self):
        """Checking if executor works with local system platform
        """
        __executor = None
        for executor in self.test.executor:
            self.show_details(f"Checking if executor works on local system platform.")
            if self.__local_system_platform in self.test.supported_platforms:
                __executor = self.command_map.get(executor.name).get(self.__local_system_platform)
        return __executor

    def __run_dependencies(self, executor):
        """Checking dependencies
        """
        if self.test.dependency_executor_name:
            executor = self.test.dependency_executor_name
        for dependency in self.test.dependencies:
            self.show_details(f"Dependency description: {dependency.description}")
            if Base.CONFIG.get_prereqs:
                self.show_details(f"Retrieving prerequistes")
                self.execute_subprocess(executor, dependency.get_prereq_command)
            self.execute_subprocess(executor, dependency.prereq_command)

    def run(self):
        """The main method which runs a single AtomicTest object.
        """
        executor = self.__get_executor_command()
        self.show_details(f"Using {executor} as executor.")
        pass
        if executor:
            if Base.CONFIG.check_dependencies and self.test.dependencies:
                self.__run_dependencies(executor)
            for test in self.test.executor:
                self.show_details("Running command")
                self.execute_subprocess(executor, test.command)
                if Base.CONFIG.cleanup and test.cleanup_command:
                    self.show_details("Running cleanup command")
                    self.execute_subprocess(executor, test.cleanup_command)