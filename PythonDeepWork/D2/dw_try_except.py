#Why? Handle errors cleanly, raise meaninfful error, use custom excetion names.

#Example 1: Basic try-except
class BookingError(Exception):
    """Custom exception for Booking errors."""
    pass

def valid_price(price):
    """Check if the price is valid or not"""
    if price<0:
        raise BookingError("Invalid price")
    return price

try:
    valid_price(500)
    valid_price(-50)
except BookingError as e:
    print("Booking error occurred",e)

# ⭐ Typical SDET-style pattern
#
# You’ll see this kind of structure in automation frameworks:
#
# class APIError(Exception):
#     pass
#
#
# def call_api():
#     # pretend something went wrong
#     raise APIError("Failed to call API")
#
#
# try:
#     call_api()
# except APIError as e:
#     print("API call failed:", e)
    # add logging, retry logic, etc.