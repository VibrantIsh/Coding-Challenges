# https://www.codechef.com/practice/course/arrays-cpp/PCPPAR01/problems/CS2023_STK

class StreakTracker:
    def __init__(self, om_values, addy_values):
        self.om_values = om_values
        self.addy_values = addy_values
        self.max_om_chain = 0
        self.max_addy_chain = 0

    def analyze_streaks(self):
        om_chain = 0
        addy_chain = 0

        for day in range(min(len(self.om_values), len(self.addy_values))):
            if self.om_values[day] > 0:
                om_chain += 1
                self.max_om_chain = max(self.max_om_chain, om_chain)
            else:
                om_chain = 0

            if self.addy_values[day] > 0:
                addy_chain += 1
                self.max_addy_chain = max(self.max_addy_chain, addy_chain)
            else:
                addy_chain = 0

        for day in range(len(self.om_values), len(self.addy_values)):
            if self.addy_values[day] > 0:
                addy_chain += 1
                self.max_addy_chain = max(self.max_addy_chain, addy_chain)
            else:
                addy_chain = 0

    def determine_outcome(self):
        if self.max_om_chain > self.max_addy_chain:
            return "OM"
        elif self.max_addy_chain > self.max_om_chain:
            return "ADDY"
        else:
            return "DRAW"

def run_streak_examination():
    num_days_om = int(input("Enter the number of days for Om: "))
    om_values = list(map(int, input("Enter Om's daily achievements (space-separated): ").split()))

    num_days_addy = int(input("Enter the number of days for Addy: "))
    addy_values = list(map(int, input("Enter Addy's daily achievements (space-separated): ").split()))

    streak_tracker = StreakTracker(om_values, addy_values)
    streak_tracker.analyze_streaks()
    result = streak_tracker.determine_outcome()

    print(f"Outcome: {result}\n")
run_streak_examination()

