int reverse(int x) {
    int re=0,flag=1;
    if(x==0) return 0;
    if(x<0) {flag=0;x=-x;}
    int tail=x%10;
    while(tail==0) {
        x/=10;
        tail=x%10;
    }
    while(x>0) {
        if(re!=0 && re*10 / re != 10) return 0;
        if((re*10 > 0 && x%10 > 0 && re*10+x%10 < 0) || (re*10 < 0 && x%10 < 0 && re*10+x%10 > 0)) return 0;
        re=re*10+x%10;
        x/=10;
    }
    if(flag==0) re=-re;
    return re;
}