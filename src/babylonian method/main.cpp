#include<bits/stdc++.h>
using namespace std;
int main(){
    int i;
    cin>>i;
    double x = i/2;
    while (true){
        double b = (x+ i/x)/2;
        if (abs(x-b) < 1e-10){
            x = b;
            break;
        }
        x = b;
    }
    cout<<x;
    return 0;
}