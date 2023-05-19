from mythic_container.MythicCommandBase import *
import json
from mythic_container.MythicRPC import *
import sys
import base64

# create a class that extends TaskArguments class that will supply all the arguments needed for this command
class AddUserArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(
                name="fullname", 
                type=ParameterType.String,
                description="Full name for the new user",
                parameter_group_info=[
                    ParameterGroupInfo(
                        required=True,
                        group_name="Defaults"
                    )
                ]
            ),
            CommandParameter(
                name="username", 
                type=ParameterType.String,
                description="Username for the new user",
                parameter_group_info=[
                    ParameterGroupInfo(
                        required=True,
                        group_name="Defaults"
                    )
                ]
            ),
            CommandParameter(
                name="password", 
                type=ParameterType.String,
                description="Password for the new user",
                parameter_group_info=[
                    ParameterGroupInfo(
                        required=True,
                        group_name="Defaults"
                    )
                ]
            ),
            CommandParameter(
                name="home_directory", 
                type=ParameterType.String,
                description="Username for the new user",
                parameter_group_info=[
                    ParameterGroupInfo(
                        required=True,
                        group_name="Defaults"
                    )
                ]
            ),
            CommandParameter(
                name="administrator", 
                type=ParameterType.Boolean,
                default_value=False,
                description="Do you want to provide administrative access to this user?",
                parameter_group_info=[
                    ParameterGroupInfo(
                        required=False,
                        group_name="Defaults"
                    )
                ]
            )
        ]

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
    attackmapping = ["T1136", "T1136.001", "T1548.004"]
    browser_script = None
    attributes = CommandAttributes(
        builtin=True
    )

    # this function is called after all of your arguments have been parsed and validated that each "required" parameter has a non-None value
    async def create_tasking(self, task: MythicTask) -> MythicTask:

        task.display_params = "Fullname: " + task.args.get_arg("fullname")
        task.display_params += ", Useraname: " + task.args.get_arg("username")
        task.display_params += ", Password: " + task.args.get_arg("password")
        task.display_params += ", HomeDirectory: " + task.args.get_arg("home_directory")
        task.display_params += ", Administrator: " + task.args.get_arg("administrator")
        
        return task

    async def process_response(self, response: AgentResponse):
        pass
