#include <iostream>
#include <fstream>
#include <string>     // для std::getline
#include <sstream>
#include <boost/algorithm/string.hpp>

using namespace std;


int main()
{
    std::stringstream mystring;
    std::vector<std::string> strs;
    // окрываем файл для чтения
    std::ifstream myfile("/home/al/Projects_My/bio_cell/doc/РИБОСОМА КАК АЛЛОСТЕРИЧЕСКИ ЛИтература.txt");
    if (myfile.is_open())
    {
            while ( myfile >> mystring.rdbuf()) {
            }

    };
    myfile.close();     // закрываем файл
    std::cout << mystring.str() << std::endl << std::endl;
    boost::split(strs, mystring.str(), boost::is_any_of(">>"));
    std::cout << strs.size() << std::endl << std::endl;
}