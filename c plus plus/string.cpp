#include <iostream>
#include <string>
using namespace std;

int main() {
    /////////////////////// my code //////////////////////
    string a,b;

    cin >> a;
    cin >> b;

    cout << a.size() << " " << b.size() << "\n";
    cout << a + b << "\n";

    string x = a, y = b;
    x[0] = b[0];
    y[0] = a[0];

    cout << x << " " << y;

    return 0;
    //////////////////// end of my code //////////////////

}