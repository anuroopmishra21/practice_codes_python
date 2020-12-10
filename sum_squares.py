#include <stdio.h>
int coin(int a){
    int s =0;
    while (a!=0){
        s= s+ (a*a);
        a= a-1;
    }
    return(s);
}
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d",coin(n));
    return 0;
}
