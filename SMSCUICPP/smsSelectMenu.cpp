#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <any>
#include <typeinfo>
#include "smscmds.h"
#include "sqlite3Commands.h"

struct Result {
    std::map<int, std::any> fL;
    std::string selectMenu;
};

template <typename T>
void executeFunction(std::any& func) {
    try {
        auto f = std::any_cast<std::function<T()>>(func);
        if constexpr (!std::is_same_v<T, void>) {
            T result = f();
            std::cout << "Function returned: " << result << std::endl;
        } else {
            f();
        }
    } catch (const std::bad_any_cast& e) {
        std::cerr << "Error: Function call type mismatch.\n";
    }
}

Result selectMenuUI(std::map<std::string, std::any> options) {
    int numberOfOptions = options.size();
    std::map<int, std::any> functionLinks;
    int i = 0;

    for (const auto& pair : options) {
        functionLinks[i + 1] = pair.second;
        ++i;
    }

    std::string menu;
    int j = 0;
    for (const auto& pair : options) {
        menu += std::to_string(j + 1) + ") " + pair.first + "\n";
        ++j;
    }
    menu += std::to_string(numberOfOptions + 1) + ") Quit\n";

    return Result{functionLinks, menu};
}

void checkSelectMenu(std::map<std::string, std::any> userOptions) {
    bool flag = true;
    int choice = 0;

    Result menuParameters = selectMenuUI(userOptions);
    std::cout << "\n" << menuParameters.selectMenu << "\n";

    int rangeOfChoices = menuParameters.fL.size();

    while (flag) {
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        if (choice >= 1 && choice <= rangeOfChoices) {
            std::any& func = menuParameters.fL[choice];

            if (func.type() == typeid(std::function<void()>)) {
                executeFunction<void>(func);
            } else if (func.type() == typeid(std::function<int()>)) {
                executeFunction<int>(func);
            } else if (func.type() == typeid(std::function<std::string()>)) {
                executeFunction<std::string>(func);
            } else {
                std::cerr << "Unsupported function type.\n";
            }
        }
        else if (choice == rangeOfChoices + 1) {
            flag = false;
            break;
        }
        else {
            std::cout << "Invalid option selected. Please try again.\n";
        }
    }
}

/*void addStudentRecord();
void deleteStudentRecord();
void searchStudentRecord();
void seeAllStudentRecords();*/


int main() {

    openDatabase();
    createTable();


    std::map<std::string, std::any> options;
    options["Add"] = std::function<void()>(addStudentRecord);
    options["Delete"] = std::function<void()>(deleteStudentRecord);
    options["Search"] = std::function<void()>(searchStudentRecord);
    options["SeeAll"] = std::function<void()>(seeAllStudentRecords);

    checkSelectMenu(options);

    return 0;
}