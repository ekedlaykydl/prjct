#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <Windows.h>

using namespace std;
char check_mass[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };

int main()
{
    setlocale(LC_ALL, "Russian");
    while (true) {
        cout << "Добро пожаловать в Калькулятор \n Тут есть команды такие как:\n + Сложение\n - Вычитание\n / Деление\n * Умножение\n | побитовое или\n ^ XOR \n  Вот тебе пример ввода  111+222 111*222 и.т.п.\nТвоя очередь!\n Введено: " << endl;
        vector <char> vector_first;
        ofstream out;
        out.open("file.txt");
        string a;
        cin >> a;
        for (int i = 0; i < a.length(); i++) {
            if (check_mass, a[i]) {
                vector_first.push_back(a[i]);
            }
            else {
                return a[i];
            }
        }
        if (out.is_open())
        {
            for (int i = 0; i < vector_first.size(); i++) {
                out << vector_first[i];
            }
        }
        out.close();
        cout << "Мы все высчитали, у нас получилось:";
        system("000.exe");
        vector_first.clear();
    }
}