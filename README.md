# robot_analysis

This python package aims to provide some utilitary function for robot analysis.

Summary:
  - [Display](#display-module)
    - [Matrix](#matrix)
    - [Headers](#header)
    - [Choices](#choices)
    - [Input](#input)
  - [Math](#math-module)
    - [Reduced Row Echelon Form](#reduced-row-echelon-form)

## Display module

This module provide displaying function for different cases.

To import this module, please use one of both

```Python
import robot_analysis.display
from robot_analysis.display import *
```
------
### **Matrix**: 
```Python
print_matrix(matrix: np.ndarray, xaxis: list = None, yaxis: list = None, name: str = "", width: int = 11)
```


Print a formatted view of the given matrix

**Params**:
  - matrix : _the matrix to show_
  - xaxis : _the name of each column_
  - yaxis : _the name of each row_
  - name : _the name of the matrix_
  - width : _the width of a single cell_
  
  **Result**:
| Name          | xaxis[0]      | xaxis[1]     | ... |
| ------------- |:-------------:| :----------: | --- |
| yaxis[0]      | matrix[0, 0]  | matrix[0, 1] | ... |
| yaxis[1]      | matrix[1, 0]  | matrix[1, 1] | ... |
| ...           | ...           |    ...       | ... |

------
### **Header**: 
```Python
print_header(txt: str or list, width: int = 120)
```

Print a header with the given text.
This function support multiline, as long you define each line in a list


**Params**:
  - txt : _the text to show_
  - width : _the width of the header_
  
 **Result**:
 ```
╔════════════════════════════════════════════════════════════════════╗
║                        Identification                              ║
╚════════════════════════════════════════════════════════════════════╝
```

------
### **Choices**: 
```Python
print_choices(choices: dict) -> int
```

Print a choice and return wich item was picked.


**Params**:
  - choices : a dict with the shape {return_value: text, ...}
  
 **Example**:
 
 If we write this small program

 ```Python
 from robot_analysis.display import print_choices

choices = {24: "First choice",
           96: "Second choice",
           # ...
           }
user_choice = print_choices(choices)
```

Result in :
```Shell
Select your mode :
        1 → First choice
        2 → Second choice
Mode > 2

> user_choice = 96

```

------
### **Input**: 
```Python
print_input(txt: str) -> int
```

 Print a formatted input to the screen.

**Params**:
  - txt : _the input text to show_
  
 **Result**:
 ```Shell
Mode > 
```

## Math module

This module provide computation function.

To import this module, please use one of both

```Python
import robot_analysis.math
from robot_analysis.math import *
```

------
### **Reduced row echelon form**: 
```Python 
ech_red(matrix: np.ndarray, show_step=False) -> numpy.ndarray
```

Compute the reduced row echelon form of the given matrix.


**Params**:
  - matrix : _the matrix from which the reduced row echelon form should be made_
  - width : _whether we should display the intermediate step, use mainly for debug_
