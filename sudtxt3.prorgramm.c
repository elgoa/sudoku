#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int zufallszahl_1_bis_9() {
    // Zufallszahlengenerator initialisieren
    

    // Zufallszahl zwischen 1 und 4 erzeugen und zurückgeben
    return (rand() % 9) + 1;
}

int ft_solution_compare(int **matrix1, int **matrix2)
{
    int i = 0;
    int j = 0;
    
    while(i < 9)
    {
        while(j < 9)
        {
            if(matrix1[i][j] != matrix2[i][j])
            return 1;
            j ++;
        }
        j = 0;
        i ++;
        }
    return 0;
}

void    ft_save(int **matrix,int **solution)
{
    int i = 0;
    int j = 0;

    while(i < 9)
    {
        while(j < 9)
        {
            solution[i][j] = matrix[i][j] ;
            j ++; 
        }
        j = 0;
        i ++;
    }
}

int sizetest(int **matrix)
{
    int i = 0;
    int j = 0;
    
    while(i < 9)
	{
		while(j < 9)
		{
			if(matrix[i][j] > 9 || matrix[i][j] == 0)
            return 1;
			j ++;
		}
		j = 0;
		i ++;
	}
    return 0;
}

void ft_print(int **matrix)
{
	int i = 0;
	int j = 0;

	while(i < 9)
	{
		while(j < 9)
		{
			printf("%d ", matrix[i][j]);
			j ++;
		}
		printf("\n");
		j = 0;
		i ++;
	}
}

void ft_fillemptygrid(int **grid)
{
    int i;
    int j;

    i = 0;
    j = 0;

    while(i < 9)
	{
		while(j < 9)
		{
			grid[i][j] = 0;
			j ++;
		}
		j = 0;
		i ++;
	}
	i = 0;
	j = 0;
}

int ft_numbercheck(int **grid, int x, int y, int z, int Blocknumbervalue)
{
    int x0 = 0;
    int y0 = 0;
    int blocknumber;

    if (z < 1)
    return 1;

    if (z > 9)
    return 1;

    while(x0 < x)
    {
        if(grid[x0][y] == z && x0 != x)
        return 1;
        x0 ++;
    }
        while(y0 < y)
    {
        if(grid[x][y0] == z && y0 != y)
        return 1;
        y0 ++;
    }
    x0 = 0;
    y0 = 0;
    while(x0 < 9)
    {
        while(y0 < 9)
        {
           blocknumber = x0 / 3 + y0 / 3 * 5;
            if(grid[x0][y0] == z && blocknumber == Blocknumbervalue)
            return 1;
            y0 ++;
        }
        y0 = 0;
        x0 ++;
    }
    return 0;
}

int ft_fillgridnumber(int **grid)
{
    int i = 0;
    int j = 0;
    int z[2][1];

    z[0][0] = zufallszahl_1_bis_9();
    

    
    while(i < 9)
    {
        while (j < 9)
        {
            z[1][0] = i / 3  + j / 3 * 5;
            while(ft_numbercheck(grid, i, j, z[0][0], z[1][0]) != 0 &&ft_numbercheck(grid, i, j, (z[0][0] - 9), z[1][0]) != 0 )
            {
                if(z[0][0] == 18)
                return 1;
                if(ft_numbercheck(grid,i,j,(z[0][0] - 9), z[1][0]) == 0 && z[0][0] > 9)
                return 1;
                z[0][0] ++;
            }
             
            if(z[0][0] < 10)
            grid[i][j] = z[0][0];
             else
             grid[i][j] = z[0][0] - 9;
            z[0][0] = zufallszahl_1_bis_9();
            j ++;
        }
        j = 0;
        i ++;
    }
    return 0;
}

int ft_solve_grid(int **grid)
{
    int i = 0;
    int j = 0;
    int z[2][1];

    z[0][0] = zufallszahl_1_bis_9();
    
    while(i < 9)
    {
        while (j < 9)
        {
            z[1][0] = i / 3  + j / 3 * 5;
            while(ft_numbercheck(grid, i, j, z[0][0], z[1][0]) != 0 &&ft_numbercheck(grid, i, j, (z[0][0] - 9), z[1][0]) != 0 && grid[i][j] == 0)
            {
                if(z[0][0] == 18)
                return 1;
                if(ft_numbercheck(grid,i,j,(z[0][0] - 9), z[1][0]) == 0 && z[0][0] > 9 && grid[i][j] == 0)
                return 1;
                z[0][0] ++;
            }
             
            if(z[0][0] < 10 && grid[i][j] == 0)
            grid[i][j] = z[0][0];
            else if(grid[i][j] == 0)
            grid[i][j] = z[0][0] - 9;
            z[0][0] = zufallszahl_1_bis_9();
            j ++;
        }
        j = 0;
        i ++;
    }
    return 0;
}

void    ft_delete_numbers(int **grid,int n)
{
    int i;
    int j;
    int blocknumber;
    int blockdeletecount[9];
    int blockdelete[9];
    int linenumbercount[9];
    int columnnumbercount[9];
    int linedelecount[9];
    int columndeletecount[9];

    i = 0;
    j = 0;

    while(i < 9)
    {
        blockdelete[i] = 0;
        linenumbercount[i] = 0;
        columnnumbercount[i] = 0;
        linedelecount[i] = n;
        columndeletecount[i] = n;
        blockdeletecount[i] = n;
        i ++;
    }
    i = 0;

    while(i < 9)
    {
        while(j < 9)
        {
            blocknumber = i / 3 * 3 + j / 3 ;
 
            if(2 * zufallszahl_1_bis_9() - blockdeletecount[blocknumber] - linenumbercount[i] -  columnnumbercount[j] <= 2 * n - linedelecount[i] - columndeletecount[j]
            && blockdeletecount[blocknumber] > 0)
            {
            grid[i][j] = 0;
            blockdeletecount[blocknumber] = blockdeletecount[blocknumber] - 1;
            }
            else
            {
                linenumbercount[i] = linenumbercount[i] + 1;
                columnnumbercount[j] = columnnumbercount[j] + 1;
            }
            j ++;
        }
        j = 0;
        i ++;
    }
}



int main(void) {
    int **array;
    int **solution;
    int **savesudoku;
    int solved = 0;
    int *solved2;
    int i = 0;
    int j = 0;
    int sudokunumber = 1;
    int number_solutions = 1;
    FILE *file;
    FILE *file2;
    solved2 = &solved;
    array = (int **)malloc(9 * sizeof(int *));
    while (i < 9) {
        array[i] = (int *)malloc(9 * sizeof(int));
        i++;
    }
    i = 0;
    solution = (int **)malloc(9 * sizeof(int *));
    while (i < 9) {
        solution[i] = (int *)malloc(9 * sizeof(int));
        i++;
    }
    i = 0;
    savesudoku = (int **)malloc(9 * sizeof(int *));
    while (i < 9) {
        savesudoku[i] = (int *)malloc(9 * sizeof(int));
        i++;
    }
    srand(time(NULL));
    while(sudokunumber < 26)
    {
    solved = 0;
    
    char dateiname[50];
    snprintf(dateiname, sizeof(dateiname), "sudoku%d.txt", sudokunumber);
    char dateinamelösung[50];
    snprintf(dateinamelösung, sizeof(dateinamelösung), "sudokusolution%d.txt", sudokunumber);
    printf("%s", "Fill grid with 0");
    
    printf("\n");
    ft_fillemptygrid(array);
    // while (j == 0 | j == 15)
    //  {
        ft_print(array);

        // printf("%d", sizetest(array));
        printf("\n");
    while(sizetest(array) != 0 || number_solutions != 0)
    {
        ft_fillemptygrid(array);
    while (sizetest(array) != 0) {
        printf("%s", "gen new Solution");
        printf("\n");
        ft_fillemptygrid(array);
        ft_fillgridnumber(array);
        number_solutions = 1;
    }

    ft_save(array,solution);
    printf("%d", number_solutions);
    printf("\n");
    while(number_solutions != 0)
    {
        if(j == 15)
        {
            j = 0; 
            break;
        }
        j ++;
        ft_delete_numbers(array, 10);
        ft_save(array,savesudoku);
        printf("%s", "numbers deleted");
        printf("\n");
        printf("\n");
        
   
        number_solutions = 0;
        


    i = 0;

    while(i < 10 && number_solutions == 0)
    {
    printf("%s", "begin solution");
    printf("\n");
    solved = 0;
    while(sizetest(array) != 0)
    {
    if (solved > 20000000)
    break;
    ft_save(savesudoku,array);
    solved = solved + ft_solve_grid(array);
    
    }
    printf("%s", "compare solutions");
     printf("\n");
    // ft_print(array);
     
    number_solutions = number_solutions + ft_solution_compare(array, solution);
    printf("%s", "number solutions:");
    printf("%d", number_solutions);
    printf("\n");
    
    i++;
    }
    
    ft_save(solution,array);
    }
    }
            ft_print(savesudoku);
            
       for(i = 1; i <= 25; ++i)
     {
         char filename[20];
     }

    FILE *file = fopen(dateinamelösung, "w");   
         for (i = 0; i < 9; i++) {
         for (int j = 0; j < 9; j++) {
             fprintf(file, "%d ", array[i][j]); 
        }
        

     fprintf(file, "\n");
    }
   FILE *file2 = fopen(dateiname, "w");

        if (file2 == NULL) 
        {
            printf("Fehler.\n");
            return 1;
        }
            for (i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {

            fprintf(file2, "%d ", savesudoku[i][j]); 
        }
        fprintf(file2, "\n");
    }

     
    

    // }


    fclose(file);
    fclose(file2);
   // system("python3 sudokuConv.py");
    printf("\n");
    ft_print(array);
    printf("\n");
    sudokunumber ++;
    }
    for (i = 0; i < 9; i++) {
        free(array[i]);
    }
    free(savesudoku);
        for (i = 0; i < 9; i++) {
        free(savesudoku[i]);
    }
    free(solution);
        for (i = 0; i < 9; i++) {
        free(solution[i]);
    }
    free(array);

    return 0;
}
