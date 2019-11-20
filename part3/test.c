#include <stdio.h>

int main(int argc, char const *argv[]) {
    int a=10;
    int b=5;
    int sum, sub, mult, div;

    sum = a+b;
    sub = a-b;
    mult = a*b;
    div = a/b;
    
    printf("This is a simple test to check gem5 !!!\n");
    printf("sum = %d\nsub = %d\nmult = %d\ndiv = %d\n", sum, sub, mult, div);

    return 0;
}
