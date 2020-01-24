#include <iostream>

int factorial(int x)
{
    if(x == 0)
        return 1;
    else
    {
        return x * factorial(x - 1);
    }
}

bool facDiv(int n, int m)
{
    int factN = factorial(n);

    float k = factN/m;

    if(k == (int)k)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int n = 0;
    int m = 0;

    std::cout << "Input 2 numbers being the first a factorial and the second a divider." << std::endl;

    std::cin >> n >> m;

    if(facDiv(n, m) == 1)
        std::cout << "YES! " << n << "! is divisable by " << m << ".  :)" << std::endl;
    else
        std::cout << "NO! " << n << "! is not divisable by " << m << ".  :(" << std::endl;
    

    return 0;
}