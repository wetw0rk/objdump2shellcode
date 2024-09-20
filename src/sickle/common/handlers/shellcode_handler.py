import os
import sys

from sickle.common.lib.generic.mparser import get_module_list
from sickle.common.lib.generic.mparser import check_module_support

class ShellcodeHandler():
    """This class is responsible for calling the appropriate shellcode module.

    :param payload: The shellcode module to use for shellcode stub generation
    :type payload: str

    :param arg_object: Arguments used by the shellcode module
    :type arg_object: dict
    """

    def __init__(self, payload, arg_object):
        
        self.payload = payload
        self.arg_object = arg_object

    def get_shellcode(self):
        """Calls the respective shellcode module and returns the generated bytecode
        to the caller.

        :return: Raw bytecode from assembly
        :rtype: bytes
        """

        payload_module = check_module_support("payloads", self.payload) 
        if (payload_module == None):
            return None

        sc_obj = payload_module.Shellcode(self.arg_object)
        bytecode = sc_obj.get_shellcode()
        
        return bytecode

    def print_stubs():
        """Prints all currently supported shellcode stubs along with a short description
        for each.
        """

        payloads = get_module_list("payloads")
        print(f"\n  {'Shellcode':<80} {'Description'}")
        print(f"  {'---------':<80} {'-----------'}")
        for i in range(len(payloads)):
            sc_module = check_module_support("payloads", payloads[i]) #, True)
            print(f"  {payloads[i]:<80} {sc_module.Shellcode.description}")