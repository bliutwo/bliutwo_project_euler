#include <iostream>
#include <fstream>
#include <time.h>
#include <string>
#include <queue>

// need to use queue to keep track of nodes already visited

void get_num_paths(int & num_paths, int rights_taken, int downs_taken, int max_rights, int max_downs)
{
    if (rights_taken == max_rights && downs_taken == max_downs)
    {
        num_paths++;
        return;
    }
    // try turning right, if you can
    if (rights_taken < max_rights)
        get_num_paths(num_paths, rights_taken + 1, downs_taken, max_rights, max_downs);
    // try turning down, if you can
    if (downs_taken < max_downs)
        get_num_paths(num_paths, rights_taken, downs_taken + 1, max_rights, max_downs);
    return;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Usage: ./a.out [integer]" << std::endl;
    } else {
        clock_t t;
        t = clock();
        std::cout << "Calculating..." << std::endl;

        std::string s = argv[1];
        // std::cout << s << std::endl;
        int dimensions = std::stoi(s);
        int max_rights = dimensions;
        int max_downs  = dimensions;

        int rights_taken = 0;
        int downs_taken  = 0;

        int num_paths = 0;
        
        get_num_paths(num_paths, rights_taken, downs_taken, max_rights, max_downs);
        std::cout << num_paths << std::endl;
        t = clock() - t;
        float time = ((float)t)/CLOCKS_PER_SEC;

        std::cout << time << std::endl;

        std::ofstream myfile;
        myfile.open("results.txt");
        myfile << num_paths;
        myfile << "\n";
        myfile << time;
        myfile << "\n";
        myfile.close();
    }
    return 0;
}
