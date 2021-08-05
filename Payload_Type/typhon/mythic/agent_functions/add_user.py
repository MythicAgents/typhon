from mythic_payloadtype_container.MythicCommandBase import *  # import the basics
import json  # import any other code you might need
# import the code for interacting with Files on the Mythic server
from mythic_payloadtype_container.MythicRPC import *

# create a class that extends TaskArguments class that will supply all the arguments needed for this command
class AddUserArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "fullname": CommandParameter(
                name="fullname", 
                type=ParameterType.String,
                required=True, 
                description="Full name for the new user"
            ),
            "username": CommandParameter(
                name="username", 
                type=ParameterType.String,
                required=True, 
                description="Username for the new user"
            ),
            "password": CommandParameter(
                name="password", 
                type=ParameterType.String,
                required=True, 
                description="Password for the new user"
            ),
            "home_directory": CommandParameter(
                name="home_directory", 
                type=ParameterType.String,
                required=True, 
                description="Username for the new user"
            ),
            "administrator" : CommandParameter(
                name="administrator", 
                type=ParameterType.Boolean,
                required=True,
                default_value=False,
                description="Do you want to provide administrative access to this user?"
            )
        }

    # you must implement this function so that you can parse out user typed input into your parameters or load your parameters based on some JSON input
    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                self.add_arg("fullname", self.command_line)
                self.add_arg("username", self.command_line)
                self.add_arg("password", self.command_line)
                self.add_arg("home_directory", self.command_line)
                self.add_arg("administrator", self.command_line)

                
        else:
            raise ValueError("Missing arguments")


# this is information about the command itself
class AddUserCommand(CommandBase):
    cmd = "add_user"
    needs_admin = True
    help_cmd = "add_user"
    description = "Adds a user through the Jamf agent."
    version = 1
    author = "@calhall"
    argument_class = AddUserArguments
    attackmapping = []
    browser_script = None

    # this function is called after all of your arguments have been parsed and validated that each "required" parameter has a non-None value
    async def create_tasking(self, task: MythicTask) -> MythicTask:

        task.display_params = task.args.get_arg("fullname")
        task.display_params = task.args.get_arg("username")
        task.display_params = task.args.get_arg("password")
        task.display_params = task.args.get_arg("home_directory")
        task.display_params = task.args.get_arg("administrator")
        return task

    async def process_response(self, response: AgentResponse):
        pass
