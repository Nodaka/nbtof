from .nbtof_base import*
from .nbtof_concat import *

def nbtof_generate(
    output_py_file,
    notebook_file,
    ):
    
    with open(output_py_file, 'w') as f:
        pass
    
    if type(notebook_file) == str:
        notebook_file = [notebook_file]
    
    for notebook_file_name in notebook_file:
        func_file_path, _ = nbtof_base(nb_path=notebook_file_name)
        nbtof_update_base(
            output_py_file,
            func_file_path)

    return output_py_file
