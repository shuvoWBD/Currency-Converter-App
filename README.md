# Currency-Converter-App
A Python Tkinter GUI app that converts amounts between multiple currencies including USD, BDT, INR, EUR, GBP, and more. Features a user-friendly interface, colorful buttons, and real-time conversion results.  Technologies:  1.Python 3  2.Tkinter for GUI


Key Features:

Universal Currency Conversion:
The application can convert between any two supported currencies. All conversions use USD as the base currency, which allows cross-currency conversion without needing direct exchange rates between every pair.

Multiple Currency Support:
The app supports 17 international currencies including USD, BDT, INR, EUR, GBP, JPY, and more. Adding a new currency is easy. You only need to add a new entry to the rates dictionary.

Simple and User-Friendly Interface:
The GUI is built using Tkinter with large fonts, clear labels, and color-coded buttons. This makes the application easy to use even for beginners.

Input Validation and Error Handling:
The program handles invalid inputs such as non-numeric amounts or unsupported currency codes. In these cases, it shows a clear error message instead of crashing.

Reset and Exit Controls:

1.The Reset button clears all input fields and results

2.The Quit button safely closes the application




Technical Architecture

a. Programming Language and Library

b. Language: Python

GUI Library: Tkinter (built-in Python module)

Application Structure
The program follows a simple event-driven architecture:

a. User actions (button clicks) trigger specific functions

b. Each function performs a defined task such as conversion, reset, or exit

Data Layer (Exchange Rates)
Currency exchange rates are stored in a Python dictionary called rates, with USD as the base currency. This provides fast lookup and easy scalability.

Conversion Logic
The conversion process happens in two steps:

a. Convert the input amount from the source currency to USD

b. Convert the USD amount to the target currency

UI Layout Management
The .place() geometry manager is used to position labels, entry fields, buttons, and result text at fixed coordinates within the window.

Exception Handling
A try-except block is used in the conversion function to prevent runtime errors caused by invalid input or missing data.
