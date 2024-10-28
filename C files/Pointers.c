
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int v =10;


int main() {
    /*
    int *f(int x) {
        v += x;
        return &v;
    }
    int* (*p)(int)=f;
    printf("%d %d %d", p(10),p(2),p(3));
    */

    /*
    int  b=3, c=5,a[]={1,2,3};
    int (*p)[3];
    printf("%d ", sizeof(c=b));
    printf("%d %d", c,sizeof(a));
    */
   /*
    void f(int p[]){
        printf("%d", sizeof(p));
    }
    int a[]={1,2,3};
    f(a);
    */

   /*
   int f(int (*p)[1],int size){
    for (int i = 0; i < size; i++,p++)
    {
        printf("%d %d ", *p, **p);
        
    }
    // return 0;
    }
   int a[]={1,2,3};
   f(a, 3);
   */

  /*
    int f(n){
    if (n<0)
        return 0;
    static int v;
    v = n - 1;
    printf("%d", v);
    f(n - 1);
    return 0;
}

    f(5);*/

    int *p = malloc(sizeof(int)*5);
    for (int i = 0; i < 5; i++)
    {
        p[i] = i;
    }
    printf("%d %d\n", *p,p);
    p++;
    free(p);
     for (int i = -1; i < 5; i++)
    {
        printf("%d ", p[i]);
    }
    printf("%d ",(p));
    return 0;
}

