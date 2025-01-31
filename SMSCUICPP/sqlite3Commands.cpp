#include <iostream>
#include "sqlite3.h"


sqlite3 *db;

int openDatabase() {
    int rc = sqlite3_open("sms.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 0;  // Failure
    }
    std::cout << "Opened database successfully" << std::endl;
    return 1;  // Success
}

void createTable() {
    const char *sql = "CREATE TABLE IF NOT EXISTS StudentRecords ("
                      "ID INTEGER PRIMARY KEY, "
                      "Name TEXT NOT NULL, "
                      "\"Final Grade\" DOUBLE NOT NULL);";

    char *errMsg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &errMsg);  
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg); 
    } else {
        std::cout << "Table created successfully" << std::endl;
    }
}

void insertRecord(int id, const std::string &name, double finalGrade) {
    std::string sql = "INSERT OR IGNORE INTO StudentRecords (ID, Name, \"Final Grade\") "
                      "VALUES (?, ?, ?);";  // Use placeholders for values

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);  // Prepare the statement
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    // Bind values to the placeholders in the SQL statement
    sqlite3_bind_int(stmt, 1, id);  // Bind ID to the first placeholder
    sqlite3_bind_text(stmt, 2, name.c_str(), -1, SQLITE_STATIC);  // Bind Name to the second placeholder
    sqlite3_bind_double(stmt, 3, finalGrade);  // Bind Final Grade to the third placeholder

    // Execute the statement
    rc = sqlite3_step(stmt);
    if (rc != SQLITE_DONE) {
        std::cerr << "Failed to insert record: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "Record inserted successfully" << std::endl;
    }

    // Finalize the statement to release resources
    sqlite3_finalize(stmt);
}

void deleteRecord(int id) {
    std::string sql = "DELETE FROM StudentRecords WHERE ID = ?;";  // SQL query

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);  // Prepare the SQL statement
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    sqlite3_bind_int(stmt, 1, id);  // Bind the ID to the query

    rc = sqlite3_step(stmt);
    if (rc != SQLITE_DONE) {
        std::cerr << "Failed to delete record: " << sqlite3_errmsg(db) << std::endl;
    } else {
        int changes = sqlite3_changes(db);  // Check number of rows affected
        if (changes > 0) {
            std::cout << "Record with ID " << id << " deleted successfully." << std::endl;
        } else {
            std::cout << "No record found with ID " << id << "." << std::endl;
        }
    }

    sqlite3_finalize(stmt);  // Finalize statement
}


void searchRecordByID(int id) {
    std::string sql = "SELECT ID, Name, \"Final Grade\" FROM StudentRecords WHERE ID = ?;";  // SQL query to search by ID

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);  // Prepare the SQL statement
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    // Bind the ID to the SQL query placeholder
    sqlite3_bind_int(stmt, 1, id);

    // Execute the query and fetch the result
    rc = sqlite3_step(stmt);
    if (rc == SQLITE_ROW) {
        // Record found, display it
        int foundID = sqlite3_column_int(stmt, 0);  // Get the ID
        const char *name = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));  // Get the Name
        double finalGrade = sqlite3_column_double(stmt, 2);  // Get the Final Grade

        std::cout << "Record Found: ID: " << foundID << ", Name: " << name << ", Final Grade: " << finalGrade << std::endl;
    } else if (rc == SQLITE_DONE) {
        // No record found
        std::cout << "No record found with ID: " << id << std::endl;
    } else {
        std::cerr << "Error while searching: " << sqlite3_errmsg(db) << std::endl;
    }

    // Finalize the statement to release resources
    sqlite3_finalize(stmt);
}


void displayAllStudentRecords() {
    std::string sql = "SELECT ID, Name, \"Final Grade\" FROM StudentRecords;";  

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0); 
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0);  
        const char *name = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));  
        double finalGrade = sqlite3_column_double(stmt, 2);  

        
        std::cout << "ID: " << id << ", Name: " << name << ", Final Grade: " << finalGrade << std::endl;
    }

    if (rc != SQLITE_DONE) {
        std::cerr << "Failed to fetch data: " << sqlite3_errmsg(db) << std::endl;
    }

    sqlite3_finalize(stmt);
}
