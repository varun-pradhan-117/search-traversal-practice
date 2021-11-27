#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

// utility for code optimization
struct pair_hash {
    inline std::size_t operator()(const std::pair<int, char> & v) const {
        return v.second;
    }
};

bool steepestAscentHillClimb(
    unordered_map<char, unordered_set<pair<int, char>, pair_hash>> &graph,
    char source,
    char dest,
    unordered_map<char, int> &nodeH
)
{
    if (source == dest)
        return true;

    char currentState = source;
    cout << currentState << "->";

    while (currentState != dest) 
    {
        // find minimum child
        char minChild = currentState;
        int minH = nodeH[currentState];
        for (auto child : graph[currentState])
        {
            if (minH > nodeH[child.second])
            {
                minH = nodeH[child.second];
                minChild = child.second;
            }
        }
        // plateau
        if (currentState == minChild) {
            cout << endl << "Cannot proceed currentState == minChild" << endl;
            return false;
        }
        cout << minChild << "->";
        currentState = minChild;
    }
    return true;
}

int main()
{
    unordered_map<char, unordered_set<pair<int, char>, pair_hash>> graph = {
        {'S', {{3, 'A'}, {2, 'B'}}},
        {'A', {{4, 'C'}, {1, 'D'}}},
        {'B', {{3, 'E'}, {1, 'F'}}},
        {'C', {}},
        {'D', {}},
        {'E', {{5, 'H'}}},
        {'F', {{2, 'I'}, {3, 'G'}}},
        {'G', {}},
        {'H', {}},
        {'I', {}}
    };
    unordered_map<char, int> nodeHeuristic = {
        {'A', 12},
        {'B', 4},
        {'C', 7},
        {'D', 3},
        {'E', 8},
        {'F', 2},
        {'H', 4},
        {'I', 9},
        {'S', 13},
        {'G', 0}
    };
    if (steepestAscentHillClimb(graph, 'S', 'G', nodeHeuristic)) cout << endl << "NODE FOUND" << endl;
    else cout << endl << "NODE NOT FOUND"<< endl;;
}