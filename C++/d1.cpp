int main() {
    string line;
    int res = 0;
    ifstream input("inputd1.txt");
    if(input.is_open()) {
        while(input.is_good()) {
            getline(input, line);
            int mass = atoi(line);
            int fuel = mass / 3;
            if(fuel > 2) res += (fuel -2);
        }
        input.close();
    }
}