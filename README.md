# nbtof
This module is used to convert .ipynb file to .py function.  
**Table of contents**  
- [nbtof](#nbtof)
  - [Intoroduction](#intoroduction)
  - [Installation](#installation)
  - [Documantation](#documantation)
    - [Tags](#tags)
  - [Examples and Recomended Usage](#examples-and-recomended-usage)
    - [Setting Parameters](#setting-parameters)
    - [Batch processing](#batch-processing)



## Intoroduction

Only by writing the `#@~` marks in notebook files, you can easily convert notebook file to py file with the function which perform the same process as notebook.  
For example, in the case that you want to convert `short_sample.ipynb` to function.

  
**short_sample.ipynb**

```python
#@param
a = 1
b = 1
```
```python
c = a + b
```
```python
#@return
c
```
  
You can take functionalized py file `output.py` by executing the next code.

```python
import nbtof

nbtof.nbtof_generate(
    output_py_file='output.py',
    notebook_file='short_sample.ipynb',
    )
```

**output.py**

```python
def short_sample(a, b):
    c = a + b
    return c
```
## Installation
The latest nbtof can be installed from PyPI:  
```
pip install nbtof
```


## Documantation
### Tags
| Tag | Description |
| ---- | ---- |
| `#@param` | Variable names in the cell become function's argument names. The values assigned at the notebook is ignored. |
| `#@default` | Variable names in the cell become function's argument names. The values assigned at the notebook get default values. |
| `#@args` | Variable names in the cell become function's variable length argument ***args** names. The values assigned at the notebook is ignored. |
| `#@kwargs` | Variable names in the cell become function's variable length argument ****kwargs** names. The values assigned at the notebook is ignored. |
| `#@return` | Variable names in the cell become function's return value |
| `#@ignore` | Anything in the cell is ignored. |
| `#@help` | What you write becomes function's docstring. Please write it in quotation marks. |
| `#@advance` | You use this tag for codes which you don't want to include in the function but in the py file (ex. import) |
| `#@r_advance` | You use this tag for codes which you don't want to run at notebook but include in the py file (ex. relative import) |



## Examples and Recomended Usage

### Setting Parameters
### Batch processing


