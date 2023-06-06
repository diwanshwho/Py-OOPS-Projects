class Bill:
    """
    Class having information about the bill such as bill amount, period of the bill.
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Create a Flatmate person with information as name, days they stay, and a method to calculate respective pay.
    """

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days = days_in_flat

    def pays(self, bill, other_flatmate):
        proportion = self.days / (self.days + other_flatmate.days)
        return round(bill.amount * proportion,2)