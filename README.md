# simple Excel Operator

## install
```bash
pip install excelop
```

### requirement
openpyxl>=3.0.7
 
### usage
```python
from excelop import ExcelOp

ex=ExcelOp("test.xlsx")  # read from test.xlsx or open a new xlsx file
row=ex.get_row_value(1)
col=ex.get_col_value(1)
ex.save() # or ex.save("test_1.xlsx")

###
