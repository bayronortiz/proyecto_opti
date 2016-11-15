# -*- coding: utf-8 -*-
import numpy as np

'''
    Clase Simplex, implementa la resolución de una matriz por método simplex
'''


class Simplex():

    def __init__(self):
        self.selec_cero = True      #Variable que controla la toma del cero, primera vez

    '''
        set_selec_cero: Método modificador de selección del cero.
        params(val:bool(True|False))
    '''
    def set_selec_cero(self, val):
        self.selec_cero = val

    '''
        menor_col: Retorna una tupla (int:numero menor, int:posicion columna)
        params: (mat:Matriz numpy)
        descripcion: Busca en la primera fila de la matriz, el número menor
            obteniendo la columna
    '''
    def pivote_col(self, mat):
        _, c = mat.shape  # Obtenemos dimension de columnas
        menor = mat[0][0]
        pos_c = -1       # Posición columna

        for i in range(1):
            for j in range(c):
                if mat[i][j] < menor:
                    menor = mat[i][j]
                    pos_c = j

        if menor != 0:
            return pos_c
        else:
            return -1

    '''
        menor_fil: Retorna la posición de la fila (int:fila)
        params: (mat: Matriz numpy, col:Columna número menor)
        descripcion: Busca en la primera fila de la matriz, el número menor
    '''
    def pivote_fil(self, mat, col_m):
        f, c = mat.shape    # Obtenemos el número de filas y columnas

        menor_b = 0     # Guarda el menor divisón columna b
        div_b = 0       # Guarda valor de la división columna b temporalment
        pos_f = -1

        for i in range(f):
            if i > 0:
                if mat[i][col_m] != 0:
                    div_b = mat[i][c-1] / mat[i][col_m]

                    if div_b >= 0:
                        if i == 1:
                            menor_b = div_b
                            pos_f = i

                        elif div_b < menor_b:
                            if div_b == 0:
                                if self.selec_cero:
                                    menor_b = div_b
                                    pos_f = i
                                    self.selec_cero = False
                            else:
                                menor_b = div_b
                                pos_f = i
        return pos_f

    '''
        conv_pivote_unit: Convierte al pivote unitario, sí este es diferente de
            uno.
        params: (mat:matriz numpy, fil_piv:int, col_piv:int)
        return: retorna una nueva matriz
    '''
    def conv_pivote_unit(self, mat, fil_piv, col_piv):
        dim_x, dim_y = mat.shape    # Obtenemos dimensiones
        new_mat = np.zeros((dim_x, dim_y))  # Creamos nueva matriz

        pivote = mat[fil_piv][col_piv]

        for i in range(dim_x):
            for j in range(dim_y):
                if i == fil_piv:
                    new_mat[i][j] = mat[i][j] / pivote  # Convertimos el pivote unitario
                else:
                    new_mat[i][j] = mat[i][j]

        return new_mat

    '''
        multi_fila_pivote: Multiplica la fila por el pivote, para convertir a
            ceros los numeros de la columna que acompañan al pivote.
    '''
    def multi_fila_pivote(self, mat, fil_piv, col_piv):
        dim_x, dim_y = mat.shape    # Obtenemos dimensiones de la matriz
        new_mat = np.zeros((dim_x, dim_y))
        val_anular = 0      # Valor necesario para anular la columna

        for i in range(dim_x):
            for j in range(dim_y):
                if i == fil_piv:
                    new_mat[i][j] = mat[i][j]   # Pasamos la fila pivote a la matriz

        for i in range(dim_x):
            val_anular = (-1) * mat[i][col_piv]
            for j in range(dim_y):
                if i != fil_piv:
                    new_mat[i][j] = (val_anular * mat[fil_piv][j]) + mat[i][j]

        return new_mat

    '''
        sol_simplex: Implementa el algoritmo simplex para la resolución de la
            matriz
        return: mat_sol matriz solución, de lo contrario retorna -1
    '''
    def sol_simplex(self, m):
        dim_x, dim_y = m.shape
        col_piv = self.pivote_col(m)
        fil_piv = self.pivote_fil(m, col_piv)
        mat_tmp = np.zeros((dim_x, dim_y))
        lista_mat = []
        lista_mat.append(np.copy(m))

        while(True):
            if fil_piv == -1 or col_piv == -1:
                break

            if m[fil_piv][col_piv] != 1:    # Convertimos el pivote a uno
                mat_tmp = self.conv_pivote_unit(m, fil_piv, col_piv)
                m = np.copy(mat_tmp)
                lista_mat.append(np.copy(m))

            mat_tmp = self.multi_fila_pivote(m, fil_piv, col_piv)
            m = np.copy(mat_tmp)
            lista_mat.append(np.copy(m))

            col_piv = self.pivote_col(m)
            fil_piv = self.pivote_fil(m, col_piv)

        return lista_mat