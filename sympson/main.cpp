#include <iostream>
#include <cmath>

double f(double x){
    return log(x)/(x*sqrt(1 + log(x)));
}

double Sympson(double a, double b, int n){
    double h = (b - a) / n;
    double sum = f(a) + f(b);
    int k;
    for(int i = 1; i <= n - 1; i++) {
        k = 2 + 2 * (i % 2);
        sum += k * f(a + i * h);
    }
    sum *= h / 3;
    return sum;
}

int main() {
    setlocale(LC_ALL, "Rus");
    double a = 1;
    double b = 3.5;
    double eps;
    std::cout << "¬ведите точность ";
    std::cin >> eps;
    int k = 10;
    int i = 0;
    double diff;

    do {
        i++;
        diff = fabs(Sympson(a, b, k * i) - Sympson(a, b, k * (i + 1)));
    }while(diff > eps);

    std::cout << Sympson(a, b, k * (i + 1));

    return 0;
}
