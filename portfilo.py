# TASK 2: Stock Portfolio Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

def calculate_investment():
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    total_investment = 0
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        elif stock not in stock_prices:
            print("Stock not found. Please choose from:", ", ".join(stock_prices.keys()))
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        
        investment = stock_prices[stock] * quantity
        total_investment += investment
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    print("\nYour Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}")
    print(f"\nTotal Investment Value: ${total_investment}")

    # Optionally save to file
    save_choice = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_choice == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Portfolio saved to portfolio_summary.txt")

# Run the tracker
if __name__ == "__main__":
    calculate_investment()
