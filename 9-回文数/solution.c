#include <stdbool.h>
bool isPalindrome(int x) {
    if(x<0 || (x>0 && x%10==0)) return false;
    int back=0;
    while(back<x) {
        back=back*10+x%10;
        x/=10;
    }
    return (back==x || x==back/10);
}