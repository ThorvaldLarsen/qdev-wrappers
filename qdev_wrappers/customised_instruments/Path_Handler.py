from qcodes import Instrument, validators as vals
import os

class Path_Handler(Instrument):
    '''
    Virtual intrument to keep track of experiment paths.
    '''
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

        self.add_parameter('WorkingDir',
                            label='Working Directory',
                            set_cmd=lambda: x,
                            value=None,
                            vals=vals.Strings())


    def Create_Folder(self,string):
        try:
            os.makedirs(string)
        except FileExistsError:
            pass


