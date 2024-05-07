# nbtof <!-- omit in toc -->

---

| [English]() | 日本語 |

---

This module is used to convert Jupyter Notebook to the python function with the same process.  


- [はじめに](#はじめに)
- [インストール方法](#インストール方法)
- [利用方法](#利用方法)
  - [マーク一覧](#マーク一覧)
  - [マークの詳細](#マークの詳細)
    - [#@param](#param)
    - [#@default](#default)
    - [#@args](#args)
    - [#@kwargs](#kwargs)
    - [#@return](#return)
    - [#@ignore](#ignore)
    - [#@help](#help)
    - [#@advance](#advance)
    - [#@r\_advance](#r_advance)



## はじめに

Jupyter Notebook で作成した一連の処理を簡単に関数化できるライブラリnbtofを作成しました. `#@~` マークを Notebook に記述するだけで対応した関数が取得できます. 例えば, 以下の **sample.ipynb** を関数化したいときは

  
**sample.ipynb**

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

下記を実行することで関数化された **sample.py** を取得することができます.

```python
import nbtof

nbtof.nbtof_generate(
    notebook_name='sample.ipynb',
    func_py_name='sample.py',
    )
```

**sample.py**

```python
def sample(a, b):
    c = a + b
    return c
```


## インストール方法

PyPI から下記でインストールできます.

```
$ pip install nbtof
```


## 利用方法

### マーク一覧

| マーク | 説明 |
| ---- | ---- |
| `#@param` | セル内の変数名は関数の引数になります. Jupyter Notebook内で割り当てられた値は無視されます.|
| `#@default` | セル内の変数名は関数の引数になります. Jupyter Notebook内で割り当てられた値はデフォルト値になります. |
| `#@args` | セル内の変数名が関数の可変長引数 *args の名前になります. Jupyter Notebook内で割り当てられた値は無視されます.|
| `#@kwargs` | セル内の変数名が関数の可変長引数 **kwargs の名前になります. Jupyter Notebook内で割り当てられた値は無視されます. |
| `#@return` | このマークの次の行が関数の戻り値になります. |
| `#@ignore` | このマークがついたセル内の記述は無視されます. |
| `#@help` | セル内の内容は Docstring になります. |
| `#@advance` | セル内の記述は関数の宣言前に直接記述されます. (例: インポート等に利用してください) |
| `#@r_advance` | セル内の `#` が記述された行は関数の宣言前に `#` が外されて記述されます. (例: 相対インポート等に利用してください) | 

### マークの詳細

#### #@param

Jupyter Notebook

**sample_param.ipynb**

```python
#@param
a = 0
```
```python
print("Hello World !")
```

は以下に変換されます.


```python

def sample_param(a):
    print('Hello world !')

```

#### #@default

Jupyter Notebook

**sample_default.ipynb**
```python
#@default
a = 0
```
```python
print("Hello World !")
```

は以下に変換されます.


```python

def sample_default(a=0):
    print('Hello world !')

```

#### #@args

Jupyter Notebook

**sample_args.ipynb**
```python
#@args
a = 0
```
```python
print("Hello World !")
```

は以下に変換されます.

```python

def sample_args(*a):
    print('Hello world !')

```


#### #@kwargs

Jupyter Notebook

**sample_kwargs.ipynb**
```python
#@kwargs
a = 0
```
```python
print("Hello World !")
```

は以下に変換されます.


```python
def sample_kwargs(**a):
    print('Hello world !')
```


#### #@return

Jupyter Notebook

**sample_return.ipynb**
```python
#@return
a = 0
```
```python
if a == 0:
#@return
    True
else:
#@return
    False
```

は以下に変換されます.

```python

def sample_return(a):
    if a == 0:
        return True
    else:
        return False
```

#### #@ignore

Jupyter Notebook

**sample_ignore.ipynb**
```python
#@ignore
1 + 1
```
```python
print('Hello world !')
```

は以下に変換されます.


```python
def sample_ignore():
    print('Hello world !')
```

#### #@help

Jupyter Notebook

**sample_help.ipynb**
```python
#@help
"""
This function outputs "Hello world !" sentence.

Parameters
----------

Returns
-------

"""
```
```python
print('Hello world !')
```

は以下に変換されます.

```python
def sample_help():
    """
    This function outputs "Hello world !" sentence.
    
    Parameters
    ----------
    
    Returns
    -------
    
    """
    print('Hello world !')
```

#### #@advance

Jupyter Notebook

**sample_advance.ipynb**
```python
#@advance
import os
import sys
```
```python
#@advance
def func():
    print(os.getcwd())
    print(sys.prefix)
    print("Hello world !")
```
```python
func()
```

は以下に変換されます.

```python
import os
import sys

def func():
    print(os.getcwd())
    print(sys.prefix)
    print('Hello world !')

def sample_advance():
    func()
```

#### #@r_advance

Jupyter Notebook

**sample_r_advance.ipynb**
```python
#@r_advance
#from . import foo
#from . import bar
```
```python
print("Hello world !")
```

は以下に変換されます.

```python
from . import foo
from . import bar

def sample_r_advance():
    print('Hello world !')
```
