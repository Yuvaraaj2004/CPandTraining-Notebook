#include <stdio.h>
#include <string.h>

typedef struct
{
    int *a;
    char *b;
    
} c;

int main(int argc, char const *argv[])
{
    // char s[] = "abcdefghijklmnopqrstuvwxyz";
    // int i=0,j=strlen(s)-1;
    // while(i<j){
    //     int temp = s[i];
    //     s[i] = s[j];
    //     s[j] = temp;
    //     i++, j--;
    // }
    // printf("%s\n", s);

    // for(int i = 0; i <strlen(s); i++){
    //     c* var = (c *)s+i;
    //     printf("%x %c ", var->a,var->b);
    //     for (int j = 0; j < 4;j++){
    //         printf("%c", *(((char*)var->b)+j));
    //     }
    //     printf("\n");
    // }

    // int a[] = {1, 2, 3, 4, 5};
    // int *p = a;
    // printf("%d\n", p);
    // printf("%d %d\n",p-50,  p[1]);
    // for (int i = 0; i < 199; i++)
    // {
    //     /* code */
    // printf("%d %d \n",a[-i],a-i);
    // }

    // return 0;

    int a;
    printf("%d %d\n",&a,a);
    char s[] = "hello";
    char *p;
    printf("%d %s\n",&s,s);
    scanf("%d", &p);
    strcpy(p, "hi");
    printf("%s %s",p, s);
}
