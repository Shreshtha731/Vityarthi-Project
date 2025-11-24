# Vityarthi-Project
 
# Title of the project-Hotel Management System
 
 
 # Overview of the project:-Develop a software named Hotel Management System to 
   Automate manual functions of a Hotel. The software should helps to 
   manage the entire Hotel operations from maintaining Rooms records, 
   Customers record to check-in and check-out in the Hotel. Introduce 
   various kinds or analysis and data visualization too. Make it easier to 
   search for rooms, customers and booking details for Hotel Management 
   staff instantly.
 
 
 # Features:- Simple and easy to operate 
   -Increase Hotel’s staff efficiencies 
   -Search, add, update, and view Room’s and booking details 
   -Helps to manage Hotel’s functions constructively 
   -Saves time and reduces overheads 
   -Reduce Hotel’s operating cost 
   -Customized reports for better management 
   -Remove manual processes to book rooms, check-in & check-out 
   and maintain records and produce daily reports.
 
 
 # Technologies/tools used-Python Version 3.13.7 and later version.
   -Data handling via Python.
   -Standard python data structures (dictionaries,list)for in memory storage.
 
 
 # Steps to install and run the projects:-
  -Clone or download the repository to your local computer.
  -Ensure Python 3.x is installed. (Test with python --version)
  -Ensure Dbms app such as mysql is installed in the system.
  -Navigate to the project directory in a terminal.
  -Pandas library preinstalled 
  -Matplotlib library preinstalled 
  -Ms-Office Pre-installed for documentation
                         

 #Instructions for testing:-

 
 Phase 1: Setup & Initialization
 -Goal: Ensure the system creates the necessary storage files.
 -Run the code.
 
-Check your folder: Look for three new files created automatically:
 rooms.csv
 customer.csv
 transaction.csv
Phase 2: Add Master Data (Prerequisites)
-You need data to work with before performing transactions.
-Test A: Add a Room
-Select Option 1 (ROOMS) -> Option 1 (Add New Rooms).
-Enter Inputs:
-Room no: 101
-Floor no: 1
-Room Type: Deluxe
-Charge: 5000
-Facilities: Wifi,AC
-Status: V (Crucial: Must be 'V' for Vacant)
-Validation: Open rooms.csv (or use the Analytics menu) to see if this row exists.
-Test B: Add a Customer
-Select Option 2 (CUSTOMERS) -> Option 1 (Add Customers).
-Note the ID: The system should auto-generate an ID (likely 1 if it's the first customer).
-Enter Inputs:
-Name: Rahul
-Age: 25
-Contact: 9876543210
-Address: Mumbai

Phase 3: The Check-In Process (Booking)
-Goal: Link a Customer to a Room.
-Select Option 3 (CHECK-IN/CHECK-OUT) -> Option 1 (Check-in a Room).
-Enter Inputs:
-Customer ID: 1 (Or whatever ID was generated in Phase 2).
-Room No: 101.
-Date Input: Be careful with the format!
-Date of booking: 20/11/2025 (Format: dd/mm/yyyy).
-Verification:
-Go to Option 5 (ANALYTICS) -> Option 1 (All Rooms).
-Look at Room 101. The status should now be 'O' (Occupied).

Phase 4: The Check-Out Process (Billing)
-Goal: Release the room and calculate the bill.
-Select Option 3 (CHECK-IN/CHECK-OUT) -> Option 2 (Check-out).
-Enter Inputs:
-Customer ID: 1
-Room No: 101
-Date Input: Enter a date after the check-in date.
-Date of check-out: 25/11/2025
-Expected Output:
-The system calculates 5 days.
-Bill: 5 * 5000 = 25000.
"Check out done Successfully..."
-Verification:
-Check Option 5 (ANALYTICS) -> Option 1. Room 101 should be 'V' (Vacant) again.

Phase 5: Analytics & Search
-Goal: Test if the query system works.
-Select Option 5 (ANALYTICS).
-Try Option 3 (Search Rooms) -> Enter 101.
-Try Option 5 (Search Customer) -> Enter 1.
-Try Option 7 (Booked Room Date wise) -> Enter 20/11/2025.

Phase 6: Edge Case Testing (Trying to Break It)
-Good testing involves trying to crash the system. Try these inputs:
-Invalid Room Check-in: Try to Check-in Room 101 while it is already Occupied.
-Expected: System should say "Room not Vacant".
-Non-Existent Data: Try to Delete Customer ID 999.
-Expected: System should say "Customer is not found".
-Wrong Date Format: Enter date as 2025-11-20 instead of 20/11/2025.
-Expected: The program will crash (ValueError) because the code specifically looks for %d/%m/%Y.
                         
                            
                        
