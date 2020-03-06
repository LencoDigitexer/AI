#�������� ��������

import numpy as np
x = np.array([ [1,2,3], [4,5,6] ])
print("x: \n {}".format(x))

from scipy import sparse
#�������� ��������� �������
eye = np.eye(10)
print(eye)

#��������������� ������� ����� � ����������� �������� � ������� CSR
# ��������� ������ ��������� ��������

sparse_matrix = sparse.csr_matrix(eye)
print("����������� ������� scipy � ������� CSR: \n {}".format(sparse_matrix))


#������ COO
data = np.ones(4)
print(data) #����� ��������� ��������� - ��������� �������
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix(( data, (row_indices, col_indices)))
print("������ COO: \n{}".format(eye_coo))



%matplotlib inline
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x,y,marker="x")


import pandas as pd
data = {'name':["ilya", "misha"],
       'loc':["stav", "london"],
       'resh':[1,2]}
data_pandas=pd.DataFrame(data)
display(data_pandas)