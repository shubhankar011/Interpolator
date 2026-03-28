#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main(){
    double i;
    cin>>i;
    int a = static_cast<int>(sqrt(i));
    double b = pow(a+1,2)-pow(a,2);
    double result = a+(i-pow(a,2))/b;
    cout<<"Approximated Square: "<<result<<endl;
    return 0;
}