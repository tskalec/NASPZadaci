#include <iostream>
#include <vector>

enum Action{
    exchange = 1, nothing = 0
};

std::pair<double, std::vector<Action>> maximizeProfit(const std::vector<double> &exchangeRate, double initialBitcoin) {
    int n = exchangeRate.size();
    std::vector<double> maxBtc(n+1, 0);
    std::vector<double> maxLtc(n+1, 0);
    maxBtc[0] = initialBitcoin;
    maxLtc[0] = 0;
    std::vector<std::pair<Action, Action>> taken(n, std::make_pair(Action::nothing, Action::nothing));
    for (int i = 1; i < n+1; i++) {
        maxBtc[i] = std::max(maxBtc[i-1], maxLtc[i-1]*(1.0/exchangeRate[i-1]));
        maxLtc[i] = std::max(maxLtc[i-1], maxBtc[i-1]*exchangeRate[i-1]);
        taken[i-1].first = (maxBtc[i] == maxBtc[i-1]) ? Action::nothing : Action::exchange;
        taken[i-1].second = (maxLtc[i] == maxLtc[i-1]) ? Action::nothing : Action::exchange;
    }

    std::vector<Action> actions(n, Action::nothing);
    bool inBitcoin = true;
    for (int i = n-1; i >= 0; i--) {
        actions[i] = inBitcoin ? taken[i].first : taken[i].second;
        if (actions[i] == Action::exchange) inBitcoin = !inBitcoin;
    }

    return make_pair(maxBtc[n], actions);
}

int main() {
    double initial;
    int n;
    std::vector<double> exchangeRate;
    std::cin >> initial >> n;
    for (int i = 0; i < n; i++) {
        double e;
        std::cin >> e;
        exchangeRate.push_back(e);
    }

    auto result = maximizeProfit(exchangeRate, initial);
    std::cout << result.first << std::endl;
    for (Action a : result.second) {
        std::cout << a << std::endl;
    }
}
