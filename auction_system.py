# auction_system.py

class AuctionSystem:
    def __init__(self):
        self.bids = {}
        self.running = True

    def display_logo(self, logo):
        print(logo)

    def collect_bid(self):
        name = input("What is your name? ")
        while True:
            try:
                price = int(input("Name your price: "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        self.bids[name] = price

    def check_more_bidders(self):
        response = input('Are there any other bidders? Type "Yes" or "No": ').strip().lower()
        if response == "no":
            self.running = False

    def determine_winner(self):
        highest_bid = 0
        winner = None
        for name, price in self.bids.items():
            if price > highest_bid:
                highest_bid = price
                winner = name
        print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")

    def run(self, logo):
        self.display_logo(logo)
        while self.running:
            self.collect_bid()
            self.check_more_bidders()
        self.determine_winner()
