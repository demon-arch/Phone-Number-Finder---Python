
import tkinter as tk
from tkinter import ttk
import phonenumbers
from phonenumbers import geocoder, carrier

# Function to find phone number details
def find_phone_details():
    phone_number = phone_entry.get().strip()
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the country/region name
        location = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier name
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        # Display results on the page
        result_label.config(
            text=f"\u260E Phone Number: {phone_number}\n\ud83c\udfe2 Location: {location}\n\ud83d\udcde Carrier: {phone_carrier or 'Unknown'}"
        )
    except phonenumbers.NumberParseException as e:
        result_label.config(text=f"\u26a0 Error: Invalid phone number.\nDetails: {e}")

# Create the main application window
app = tk.Tk()
app.title("Phone Number Location Finder")
app.geometry("600x450")
app.configure(bg="black")  # Set the background color

# Style customization
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", 
                font=("Helvetica", 12, "bold"), 
                foreground="white", 
                background="pink", 
                borderwidth=0, 
                padding=8)
style.map("TButton", background=[("active", "#FF69B4")])

style.configure("TLabel", 
                font=("Helvetica", 12), 
                background="black", 
                foreground="pink")
style.configure("TEntry", 
                font=("Helvetica", 14), 
                padding=5, 
                fieldbackground="white")

# Header
header = tk.Label(app, 
                  text="\ud83d\udd0d Phone Number Location Finder", 
                  font=("Helvetica", 20, "bold"), 
                  bg="black", 
                  fg="pink")
header.pack(pady=20)

# Input field label
label = ttk.Label(app, 
                  text="Enter Phone Number (e.g., +919840358231):")
label.pack(pady=10)

# Input field
phone_entry = ttk.Entry(app, width=40, font=("Helvetica", 14))
phone_entry.pack(pady=10)

# Button
find_button = ttk.Button(app, text="Find Location", command=find_phone_details)
find_button.pack(pady=20)

# Results Label
result_label = tk.Label(app, 
                        text="", 
                        font=("Helvetica", 14), 
                        bg="black", 
                        fg="pink", 
                        justify="left")
result_label.pack(pady=20)

# Footer
footer = tk.Label(app, 
                  text="\u2764 Made with Python", 
                  font=("Helvetica", 10), 
                  bg="black", 
                  fg="pink")
footer.pack(side=tk.BOTTOM, pady=10)

# Run the application
app.mainloop()
