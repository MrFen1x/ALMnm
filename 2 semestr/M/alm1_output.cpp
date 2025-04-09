#include <iostream>

int main()
{
int i = 10;
{init}
for (int x = 0; x < 10; x++;) {
    i = i + 1;
    int z = 0;
    do {
        z++;
        i += z;
    } while (z < 3);
}
{upd}
}