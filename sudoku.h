#ifndef SUDOKU_H
#define SUDOKU_H

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int ft_solve_grid(int **grid);
void ft_delete_numbers(int **grid, int n);
int ft_fillgridnumber(int **grid);
int sizetest(int **matrix);
void ft_print(int **matrix);
void ft_save(int **matrix, int **solution);
int ft_solution_compare(int **matrix1, int **matrix2);
int zufallszahl_1_bis_9();
int ft_numbercheck(int **grid, int x, int y, int z, int Blocknumbervalue);
void ft_fillemptygrid(int **grid);
int ft_solve(int **grid);

#endif // SUDOKU_H