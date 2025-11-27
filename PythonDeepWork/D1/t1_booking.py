# TASK 1 — EXPLANATION (Booking Class for API Testing)

from datetime import datetime
from t2_logger import get_logger


class Booking:

    def __init__(self, firstname, lastname, totalprice, depositpaid, checkin, checkout):
        self.firstname = firstname
        self.lastname = lastname

        #Validate price to be non-negative
        if totalprice <= 0:
            get_logger().info("Total price must be postitive")
            raise Exception("Total price must be greater than zero")
        self.totalprice = totalprice

        self.depositpaid = depositpaid
        self.checkin = checkin
        self.checkout = checkout

    def calculate_total_with_tax(self, tax_rate):
        """
        tax_rate → percentage (e.g., 10 for 10%)
        """
        return self.totalprice + (self.totalprice * (tax_rate / 100))
        get_logger().info(f"Calculate todal tax with total price {self.totalprice} and tax rate {tax_rate}%")

    def apply_discount(self, percent):
        if percent <= 0 or percent > 100:
            get_logger().info("Percent must be between 0 and 100")
            raise Exception("Percent must be between 0 and 100")
        discount_amount = self.totalprice * (percent / 100)
        self.totalprice = self.totalprice - discount_amount
        return self.totalprice

    def validate_dates(self):
        """
        Raises exception if checkout < checkin
        """
        fmt = "%Y-%m-%d"
        checkin_dt = datetime.strptime(self.checkin, fmt)
        checkout_dt = datetime.strptime(self.checkout, fmt)
        get_logger().info("Validating booking dates")

        if checkout_dt < checkin_dt:
            get_logger().info("Date validation failed")
            raise Exception(f"Invalid dates: checkout {self.checkout} is earlier than checkin {self.checkin}")
            get_logger().info("Date validation passed")

    def get_duration(self):
        """
        Number of days between checkin and checkout.
        Example: 2025-01-10 -> 2025-01-15 = 5 days
        :return:
        """
        fmt = "%Y-%m-%d"
        checkin_dt = datetime.strptime(self.checkin,fmt) # line turns text string date into a real date.
        checkout_dt = datetime.strptime(self.checkout,fmt)
        duration = (checkout_dt - checkin_dt).days
        return duration

    def get_summary(self):
        return (
            f"Booking Summary:\n"
            f"Name: {self.firstname} {self.lastname}\n"
            f"Price: {self.totalprice}\n"
            f"Deposit Paid: {self.depositpaid}\n"
            f"Check-in: {self.checkin}\n"
            f"Check-out: {self.checkout}"
        )

    get_logger().info("Generating booking summary")


b1 = Booking("Sachin", "Mate", 2500, True, "2025-01-10", "2025-01-15")
b2 = Booking("Aditi", "Pawar", 3200, False, "2025-02-01", "2025-02-05")
b3 = Booking("Rani", "Chef", 4500, True, "2025-03-15", "2025-03-10")  # invalid dates

bookings = [b1, b2]

# Valid bookings
for b in bookings:
    b.validate_dates()
    print(b.apply_discount(10))
    print(b.get_duration())
    print(b.get_summary())
    print("Total with 10% tax:", b.calculate_total_with_tax(10))
    print("-" * 40)

# Invalid booking example
try:
    b3.validate_dates()
except Exception as e:
    print("Exception raised:", e)

#
# 🟦 TASK 1 — EXPLANATION (Booking Class for API Testing)
# 1️⃣ Why this class? (Real-world relevance)
#
# In API testing (like Restful Booker, real hotel systems, etc.)
# a Booking is the core object → every API uses this structure:
#
# Create booking
#
# Update booking
#
# Validate booking
#
# Calculate totals
#
# Validate dates (checkin < checkout)
#
# Creating a Python class for it allows:
#
# Clean object representation
#
# Reusable test data
#
# Easy method extensions (tax, summary, validation)
#
# OOP-style logic separation instead of hard-coded dictionaries
#
# This is exactly what interviewers expect from a QA Automation Engineer.
#
# 2️⃣ __init__ Method (Object Initialization)
#
# This is the constructor that runs whenever you create a Booking:
#
# def __init__(self, firstname, lastname, totalprice, depositpaid, checkin, checkout):
#
#
# It assigns attributes to the object:
#
# firstname
#
# lastname
#
# totalprice
#
# depositpaid
#
# checkin
#
# checkout
#
# This makes each Object behave like one booking record.
#
# 3️⃣ calculate_total_with_tax()
#
# Purpose:
# Add tax to base price.
#
# return self.totalprice + (self.totalprice * (tax_rate / 100))
#
#
# Why important?
# In real-world booking APIs, tax calculation is a common operation.
# By putting it in a method → you make the class reusable and realistic.
#
# 4️⃣ validate_dates()
#
# Purpose:
# Ensure checkout date is ALWAYS after checkin.
#
# Flow:
#
# Convert string → datetime
#
# Compare
#
# If checkout < checkin → raise Exception
#
# This is exactly what real hotel APIs check internally.
# Interviewers love when your models enforce validation.
#
# 5️⃣ get_summary()
#
# Creates a clean, readable summary:
#
# Booking Summary:
# Name: Sachin Mate
# Price: 2500
# ...
#
#
# This is useful for:
#
# Logging

# API response comparison
#
# Debugging failed tests
#
# 6️⃣ Object Creation
#
# You created 3 objects:
#
# b1 = Booking(...)
# b2 = Booking(...)
# b3 = Booking(...)  # invalid dates
#
#
# This shows:
#
# You know how to instantiate classes
#
# You know how to trigger and handle exceptions
#
# 7️⃣ Exception Handling
# try:
#     b3.validate_dates()
# except Exception as e:
#     print("Exception raised:", e)
#
#
# This proves you understand:
#
# Date validation
#
# Exception raising
#
# Exception catching
#
# Very important for API automation.
#
# 8️⃣ Why this solution is interview-strong
#
# Because it uses:
# ✔ OOP fundamentals
# ✔ Reusability
# ✔ Real API testing concepts
# ✔ Exception handling
# ✔ Datetime parsing
# ✔ Object instantiation
# ✔ Business logic implementation
#
# This is EXACTLY what a 3-year QA Automation Engineer should know.
#
# ⭐ Final Summary
#
# Task 1 teaches you how to build a realistic model class used in API testing.
#
# You covered:
#
# ✔ Class & attributes
# ✔ Constructor
# ✔ Methods with business logic
# ✔ Date validation with exception
# ✔ Object creation
# ✔ Handling invalid data
# ✔ Printing summary