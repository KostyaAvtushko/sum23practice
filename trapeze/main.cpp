#include <iostream>
#include <cmath>
double f(double x){
    return pow(x, x)*(1 + log(x));
}

double Trapeze(double a, double b, int n){
    double h = (b - a)/n;
    double sum = f(a) + f(b);
    for(int i = 1; i <= n - 1; i++)
        sum += 2*f(a + i*h);
    sum *= h/2;

    return sum;
}

int main() {
    double a = 1;
    double b = 3;


    double eps;
    std::cin >> eps;
    int k = 10;
    int i = 0;
    double diff;
    do{
        i++;
        diff = fabs(Trapeze(a, b, k*i) - Trapeze(a, b, k*(i + 1)));
    }while(diff > eps);

    std::cout << eps << " " << Trapeze(a, b, k*(i + 1));

    return 0;
}
