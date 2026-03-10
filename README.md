Budget App (FreeCodeCamp)

A Python application for managing budget categories and tracking finances, developed as the third project for the Scientific Computing with Python certification.

      Project Overview
The goal of this project was to create a 'Category' class that can instantiate different budget objects (like food, clothing, or entertainment). The application allows for depositing funds, withdrawing money with balance checks, and transferring amounts between categories, all while maintaining a detailed transaction ledger.

      Key Features
- Object-Oriented Ledger:
    Each category maintains its own ledger of transactions as a list of dictionaries.
- Automated Balance Tracking:
    Includes a check_funds utility to prevent overdrafts during withdrawals or transfers.
- Formatted Output:
    The class features a custom __str__ method that displays a professional, aligned receipt-style table of all transactions.
- Spending Visualization:
    Includes a standalone function create_spend_chart that generates an ASCII bar chart showing the percentage of total expenses across all categories.

      Technical Skills Applied
- Object-Oriented Programming (OOP):
    Implemented classes, methods, and dunder methods (__init__, __str__) to model real-world financial behavior.
- Advanced String Formatting:
    Utilized f-strings with specific alignment modifiers (e.g., ':<23', ':>7.2f') and the .center() method for clean UI output.
- Data Transformation:
    Leveraged zip(*args) to transpose text data, allowing category names to be printed vertically on the chart.
- List Comprehensions:
    Optimized data processing using concise Pythonic syntax for calculating totals and padding strings.

      Learning Reflections
This project deepened my understanding of how to structure internal logic within a class and the importance of data encapsulation. I learned how to handle complex string manipulations for CLI tools and realized that using built-in functions like sum() and max() with generator expressions makes code significantly more readable and efficient compared to manual loops.

Created by Chicot-q
