#include "stdio.h"

typedef struct 
{
    int roll;
    char name[19];
} s;


int main(int argc, char const *argv[])
{
    s v1 = {0x41424344, "fsdfasdg"};
    // v2 = v1;
    printf("%d, %s %s   end",v1.roll, &v1.name, &v1.roll);
    return 0;
}
