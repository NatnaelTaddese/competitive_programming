#include <bits/stdc++.h>
int main(int argc, char const *argv[])
{
    int w;
    std::cin >> w;
    std::cout << ((w % 2 != 0) || (w == 2) ? "NO" : "YES");
    return 0;
}
