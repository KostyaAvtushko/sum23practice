#include <cmath>
#include <iostream>

using namespace std;

const double eps = 0.00000001;

int main(int argc, const char * argv[])
{
    double x0 = 1.2,  // Начальное приближение
           x1 = 2;
    for(;;)
    {
        x1 = 2 - sin(1/x0);
        if (fabs(x1 - x0) < eps) break;
        x0 = x1;
    }
    cout << x1 << endl;
}
