// // // Online C compiler to run C program online
// // #include <stdio.h>
// // #include <stdlib.h>

// // int main() {
// //     // Write C code here
// //     // printf("Try programiz.pro");
// //     int a,n;
// //     scanf("%d",&n);
// //     int b[n];
// //     int *c=(int*)malloc(n*sizeof(int));;
// //     printf("%ld %ld %ld %ld\n",&a,&n);
// //     char s[] = "%s[%ld] = %ld\n";
// //     for (int i = 0; i < n;i++)
// //         printf(s,"arrb" ,i, b + i);
// //     for (int i = 0; i < n;i++)
// //         printf(s,"arrc", i, c+ i);
// //         return 0;

// #include <pthread.h>
// #include <stdio.h>
// #include <stdlib.h>
// #include <unistd.h>

// #define N 5  // Number of philosophers

// pthread_mutex_t forks[N];  // Mutexes for forks
// pthread_t philosophers[N]; // Threads for philosophers

// void think(int id) {
//     printf("Philosopher %d is thinking...\n", id);
//     sleep(rand() % 3); // Random thinking time
// }

// void eat(int id) {
//     printf("Philosopher %d is eating...\n", id);
//     sleep(rand() % 2); // Random eating time
// }

// void* philosopher(void* num) {
//     int id = *(int*)num;

//     while (1) {
//         think(id);
        
//         // Pick up forks (lower numbered fork first to avoid deadlock)
//         pthread_mutex_lock(&forks[id]);
//         pthread_mutex_lock(&forks[(id + 1) % N]);

//         eat(id);

//         // Put down forks
//         pthread_mutex_unlock(&forks[(id + 1) % N]);
//         pthread_mutex_unlock(&forks[id]);
//     }
// }

// int main() {
//     int i, ids[N];

//     // Initialize mutexes
//     for (i = 0; i < N; i++) {
//         pthread_mutex_init(&forks[i], NULL);
//     }

//     // Create philosopher threads
//     for (i = 0; i < N; i++) {
//         ids[i] = i;
//         pthread_create(&philosophers[i], NULL, philosopher, &ids[i]);
//     }

//     // Wait for all philosophers to finish (they won't in this case)
//     for (i = 0; i < N; i++) {
//         pthread_join(philosophers[i], NULL);
//     }

//     // Destroy mutexes
//     for (i = 0; i < N; i++) {
//         pthread_mutex_destroy(&forks[i]);
//     }

//     return 0;
// }
    // printf("%d %d %d",a,b,c);

// Online C compiler to run C program online
#include <stdio.h>
// #include <unistd.h>
// int main() {
//     // Write C code here
//     for (int i=0;i<2;i+=1){
//     printf("Try programiz.pro\n");
//         int val=fork();
//         printf("%d %d\n",val,i);
//     }

//     return 0;
// }

// int main(){
//     char *s = "%d %d %p";
//     printf( s,10,220);
// }
// Online C compiler to run C program online
#include <stdio.h>

// int main() {
//     // Write C code here
//     for (int i = -128; i < 128;i++)
//         printf("%c %d", i,i);
//         int a[5];
//     char *p=&a;
//     for (int i = 0; i < 5; i++){
//         a[i] = 0;
//     }
//     for (int i = 0; i < 10;i+=1){
//         p[i] = 'a';
//         printf("%d %d %d\n",i,p[i],a[i/4]);
//     }
//     for (int i = 0; i < 5; i++){
//         printf("%d\n", a[i]);
//     }
//     printf("%d\n", ('a' << 16)+('a' << 8) + 'a');
//     int fact = 0;
//     for (int i = 0; i < 4;i++){
//         fact <<= 8;
//         fact += 'a';
//         printf("%d\n", fact);
//     }
//         return 0;
// }
// int main(){
//     char s[100] = "welcome";
//     printf("\tWelcome11\n");
//     printf("W\telcome11\n");
//     printf("We\tlcome11\n");
//     printf("Welc\tome11\n");
//     printf("Welco\tme11\n");
//     printf("Welcom\te11\n");
//     printf("Welcome\t11\n");
//     printf("Welcome1\t1\n");
//     // printf("Welcome");
//     // printf("Welcome");
// }
int main(){
    // char c[20];
    // for (int i = 0; i < 20;i++)
    //     c[i] = i%2==0?0xA0:0x0A;
    // int *a = c;
    // for (int i = 0; i < 5;i++)
    //     printf("%u\n", a[i]);
    int a;
    char *c;
    printf("%d", scanf("%d %d %d %s",&a,&a,&a,&c));
}