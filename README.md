# Stock Portfolio Tracker 📈

## Overview
The Stock Portfolio Tracker is a simple Python program that calculates the total investment value based on user input. It uses a hardcoded dictionary of stock prices and allows users to enter stock symbols and quantities to generate a portfolio summary.

## Features
- Hardcoded dictionary for stock prices (e.g., AAPL, TSLA, MSFT, GOOGL).
- User inputs stock symbols and quantities.
- Calculates and displays total investment value.
- Optionally saves portfolio summary to a `.txt` file.
- Beginner-friendly and console-based.

## How to Run
1. Save the program as `portfolio_tracker.py`.
2. Run it in your Python environment (`python portfolio_tracker.py`).
3. Enter stock symbols and quantities when prompted.
4. Type `done` when finished to see your portfolio summary.
5. Choose whether to save the results to a file.

## Example Interaction
Welcome to the Stock Portfolio Tracker!
Available stocks: AAPL, TSLA, MSFT, GOOGL
Enter stock symbol (or type 'done' to finish): AAPL
Enter quantity of AAPL: 10
Enter stock symbol (or type 'done' to finish): TSLA
Enter quantity of TSLA: 5
Enter stock symbol (or type 'done' to finish): done

Your Portfolio Summary:
AAPL: 10 shares → $1800
TSLA: 5 shares → $1250

Total Investment Value: $3050
Do you want to save the result to a file? (yes/no): yes
Portfolio saved to portfolio_summary.txt

## Concepts Used
- **Dictionary**: Stores stock prices.
- **Input/Output**: Handles user interaction.
- **Arithmetic**: Calculates investment values.
- **Loops & Conditionals**: Manage program flow.
- **File Handling**: Saves portfolio summary.

## Future Enhancements
- Add support for `.csv` file export.
- Fetch real-time stock prices via API.
- Include portfolio performance tracking.

---

This project is ideal for beginners learning Python fundamentals like dictionaries, loops, conditionals, and file handling, while applying them to a practical finance-related use case.
