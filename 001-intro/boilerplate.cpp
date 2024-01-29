#include <bits/stdc++.h>
// this header files includes all the library used for competitve programming
// that includes iostream, vectors and algorithms

using namespace std;

int main(int argc, char const *argv[])
{
    // input and output can be a bottle neck in competetive programming
    // the following code will optimize input and output
    ios::sync_with_stdio(0);
    cin.tie(0);

    // reading a whole line from an input that is not interrupted by \n
    string s;
    getline(cin, s);

    // In some contest systems, files are used for input and output. An easy solution
    // for this is to write the code as usual using standard streams, but add the following
    // lines to the beginning of the code:
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // After this, the program reads the input from the file ”input.txt” and writes the
    // output to the file ”output.txt”.

    // INTEGER DATA TYPES
    int int32_bit = 32;
    long long int64_bit = 23423542LL;
    // notice that there is LL at the end of the number, that is to indicate the number is a long long
    // there might be errors if there are other int types working with long types
    // to fix that we have to convert the int into a long before we can procced to arthmetrics
    int64_bit = (long long)int32_bit * int32_bit;

    cout << int64_bit;
    // out cout object has been changed in line 22, so we are going to see the output in the output.txt file

    // FLOATING POINTS
    double mid_precision;
    long double high_prescision = 3.14159265;

    // to output the number in the desired decimal place
    printf("%.9f", high_prescision);
    // number is now precise to 9 decimal places
    // using scientific notation
    double s_notation = 1e-8; // this is the same as 1 * 10 ^ -8
    s_notation = 1e10;        // 1 * 10 ^ 10

    return 0;
}
