from mythic_payloadtype_container.MythicCommandBase import *  # import the basics
import json  # import any other code you might need
# import the code for interacting with Files on the Mythic server
from mythic_payloadtype_container.MythicRPC import *

# create a class that extends TaskArguments class that will supply all the arguments needed for this command
class ExecuteArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = {
            "script": CommandParameter(
                name="script", type=ParameterType.String, description="Script to run"
            ),
        }

    # you must implement this function so that you can parse out user typed input into your parameters or load your parameters based on some JSON input
    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                self.add_arg("script", self.command_line)
        else:
            raise ValueError("Missing arguments")


# this is information about the command itself
class ExecuteCommand(CommandBase):
    cmd = "execute_command"
    needs_admin = False
    help_cmd = "execute_command"
    description = "Executes a bash command using a Jamf Policy."
    version = 1
    author = "@calhall"
    argument_class = ExecuteArguments
    attackmapping = []
    browser_script = None

    # this function is called after all of your arguments have been parsed and validated that each "required" parameter has a non-None value
    async def create_tasking(self, task: MythicTask) -> MythicTask:

        task.display_params = task.args.get_arg("script")
        return task

    async def process_response(self, response: AgentResponse):
        pass
