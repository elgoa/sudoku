#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "sudoku.h"

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
    while(sudokunumber < 101)
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
        ft_delete_numbers(array, 12);
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
    // while(sizetest(array) != 0)
    // {
    // if (solved > 20000000)
    // break;
    // ft_save(savesudoku,array);
    // solved = solved + ft_solve_grid(array);
    
    // }

    ft_solve(array);
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
