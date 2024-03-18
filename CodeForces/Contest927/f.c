#include <stdio.h>

int main()
{
    int a = 1, b = 1, c = 1;
    
    printf ("%d %d %d %d", a, ++a ,a ,++a+a++, a++ + ++b, ++c + c++ + a++);

    return 0;
}