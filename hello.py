import streamlit as st

class BudgetApp:
    def __init__(self):
        self.money = 0
        self.plan = {
            "Rent/House": 0,
            "Food": 0,
            "Transport": 0,
            "Fun": 0,
            "Bills": 0,
            "Savings": 0
        }
        self.spent = {
            "Rent/House": 0,
            "Food": 0,
            "Transport": 0,
            "Fun": 0,
            "Bills": 0,
            "Savings": 0
        }

    def ask_income(self):
        st.subheader("Enter Your Monthly Income")
        self.money = st.number_input("How much money do you make in a month?", min_value=0.0, format="%.2f")

    def set_budget(self):
        st.subheader("Set Your Budget for Each Category")
        for item in self.plan:
            self.plan[item] = st.number_input(f"Budget for {item} ($)", min_value=0, value=self.plan[item])

    def enter_spending(self):
        st.subheader("Enter Your Actual Spending")
        for item in self.spent:
            self.spent[item] = st.number_input(f"Spent on {item} ($)", min_value=0, value=self.spent[item])

    def show_results(self):
        st.subheader("Budget Report")

        total_budget = sum(self.plan.values())
        total_spent = sum(self.spent.values())
        left_money = self.money - total_spent

        st.write(f"Total Money: ${self.money:.2f}")
        st.write(f"Total Budgeted: ${total_budget:.2f}")
        st.write(f"Total Spent: ${total_spent:.2f}")
        st.write(f"Money Left: ${left_money:.2f}")

        st.subheader("Category Breakdown")
        for item in self.plan:
            planned = self.plan[item]
            used = self.spent[item]
            extra = planned - used
            if used <= planned:
                status = "Stayed in budget"
            else:
                status = "Over budget"
            st.write(f"{item}: Planned ${planned:.2f}, Spent ${used:.2f}, Left ${extra:.2f} → {status}")

        savings = self.money - total_spent
        st.subheader("Savings & Spending")
        st.write(f"Total Savings: ${savings:.2f}")
        st.write(f"Saved: {((savings / self.money) * 100):.2f}%")
        st.write(f"Spent: {((total_spent / self.money) * 100):.2f}%")

        if total_spent > self.money:
            st.error("Warning: You spent more than you made! Be careful.")

    def run(self):
        st.title("Budget Planner App")
        self.ask_income()
        self.set_budget()
        self.enter_spending()

        if self.money > 0:
            self.show_results()

# Run the app
if __name__ == "__main__":
    app = BudgetApp()
    app.run()
