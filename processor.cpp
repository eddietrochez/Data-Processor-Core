#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

// Simple high-performance core to process data
int main() {
    std::vector<double> data = {10.5, 20.0, 15.75, 30.2, 45.1, 12.3};
    
    double sum = std::accumulate(data.begin(), data.end(), 0.0);
    double avg = sum / data.size();
    double max_val = *std::max_element(data.begin(), data.end());

    std::cout << "--- Backend Core Results ---" << std::endl;
    std::cout << "Total Sum: " << sum << std::endl;
    std::cout << "Average: " << avg << std::endl;
    std::cout << "Max Value: " << max_val << std::endl;

    return 0;
}
