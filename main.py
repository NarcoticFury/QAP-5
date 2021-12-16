# QAP 5
# Author - Devon Lane
# Date - Nov 28, 2021
# Purpose - One Stop Insurance

import datetime

def add_month(date, add):
    CurrentMonth = date.month
    NextMonth = CurrentMonth + add
    if NextMonth > 12:
        NextMonth = NextMonth - 12
    return NextMonth

while True:

    f = open('OSICDef.dat', 'r') # Reads values from the OSICDef.dat File
    POLICY_NUM = int(f.readline()) # Policy Number
    BASIC_PREM = float(f.readline()) # Basic Premium
    DISCOUNT = float(f.readline()) # Discount Rate
    LIAB_COVERAGE = float(f.readline()) # Extra Liability Rate
    GLASS_COVERAGE = float(f.readline()) # Glass Coverage Rate
    LOAN_CAR_COVER = float(f.readline()) # Loaner Car Rate
    HST = float(f.readline()) # HST Tax (15%)
    PROCESS_FEE = float(f.readline()) # Process Fee
    f.close()
    #Constants
    COMP_NAME = ("One Stop Insurance Company").title() # Name of the company
    ALLOW_CHAR = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz - . '") # Set of allowed alphabetical values
    ALLOW_NUM = set("1234567890") # Set of allowed numerical values
    ALLOW_FULL = set("1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz - . ") # Set of both alpha and numerical values
    CUR_DATE = datetime.datetime.now().date() # Current Date
    while True:
        try:
            CustFirstName = "John"#input("Enter the customer's first name(Enter Exit to end data entry): ").title()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(CustFirstName).issubset(ALLOW_CHAR) == False and CustFirstName != "Exit": #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            elif CustFirstName == "Exit": #Allows user to exit the program
                exit()
            else:
                break

        break


    while True:
        try:
            CustLastName = "Smith"#input("Enter the customer's Last name: ").title()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(CustLastName).issubset(ALLOW_CHAR) == False: #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            else:
                break
    while True:
        try:
            StAdd = "19 Out of Luck Lane"#input("Enter the customer's street address: ").title().upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(StAdd).issubset(ALLOW_FULL) == False: #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            else:
                break

    while True:
        try:
            City = "St John's"#input("Enter the customer's home city name: ").title().upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(City).issubset(ALLOW_CHAR) == False: #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            else:
                break

    while True:
        try:
            Prov = "NL"#input("Enter the customer's home province: ").upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else: #Ensures only approved values are allowed.
            if (Prov != "NL" and Prov != "PE" and Prov != "NS" and Prov != "QC" and Prov != "ON" and Prov != "MB"
                    and Prov != "SK" and Prov != "AB" and Prov != "BC" and Prov != "YT" and Prov != "NT" and Prov != "NU"):
                print("Invalid Entry! Please enter Internationally approved alpha code (Ex: NL = Newfoundland and "
                              "Labrador, NB = NewBrunswick, PE = P.E.I., NS = Nova Scotia, QC = Quebec, ON = Ontario,"
                              "MB = Manitoba, SK = Saskatchewan, AB = Alberta, BC = British Columbia, YT = Yukon, "
                              "NT = Northwest, Territories, NU = Nunavut.")
            elif len(Prov) != 2: # Ensures the length of characters is the right amount
                print("Invalid entry - Prov Length must be 2 characters in length")
            else:
                break

    while True:
        try:
            PostCode = "A1A1A1"#input("Enter the customer's postal code(A1A1A1): ").title().upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(PostCode).issubset(ALLOW_FULL) == False: #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            elif len(PostCode) != 6: # Ensures the length of characters is the right amount
                print("Invalid Entry - PostCode must be 6 characters in length.")
            elif PostCode[0].isdigit() or PostCode[2].isdigit() or PostCode[4].isdigit(): # Ensure values are numerical
                print("Invalid Entry - Must Be Numerical Values.")
            elif PostCode[1].isalpha() or PostCode[3].isalpha() or PostCode[5].isalpha(): # Ensure values are alphabetical
                print("Invalid Entry - Must be Alphabetical Values.")
            else:
                PostCode = f"{PostCode[0:3]} {PostCode[3:6]}" # Format for the Postal Code: A1A-1A1
                break

    while True:
        try:
            PhoneNum = "7096996969"#input("Enter the customer's phone number: ")
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if set(PhoneNum).issubset(ALLOW_NUM) == False: #Ensures only approved values are allowed.
                print("Invalid Entry - Can only contain allowed characters.")
            elif len(PhoneNum) != 10: # Ensures the length of characters is the right amount
                print("Invalid Entry - Must be 10 characters in length.")
            else:
                PhoneNum = f"({PhoneNum[0:3]})-{PhoneNum[3:6]}-{PhoneNum[6:10]}" # Format for phone number: (999)-999-9999
                break

    while True:
        InsPrem = 0
        try:
            CarNum = 3#int(input("Enter the number of car's being insured: "))
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if CarNum == 1:
                InsPrem = BASIC_PREM # Insurance Premium for only 1 vehicle
                break
            elif CarNum > 1:
                InsPrem = BASIC_PREM + (((BASIC_PREM) * (CarNum - 1)) * DISCOUNT) # Insurance Premium applied for more
                                                                                  # than 1 vehicle, whereby all additional
                                                                                  # vehicles have a Discount of 25%
                break
            else:
                break

    while True:
        try:
            ExtraLiab = "Y"#input("Do you want extra liability coverage(enter Y for Yes or N for No): ").upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if ExtraLiab != "Y" and ExtraLiab != "N": # Ensures only approved values are allowed.
                print("Invalid Entry - Must be either Y for Yes or N for No.")
            elif ExtraLiab == "Y":
                ExtraLiabCost =LIAB_COVERAGE * CarNum # Extra Charge applied to each vehicle insured
                break
            else:
                ExtraLiabCost = 0
                break

    while True:
        try:
            GlassCover = "Y"#input("Do you want optional glass coverage(enter Y for Yes or N for No): ")
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if GlassCover != "Y" and GlassCover != "N": # Ensures only approved values are allowed.
                print("Invalid Entry - Must be either Y for Yes or N for No.")
            elif GlassCover == "Y":
                 GlassCoverCost = GLASS_COVERAGE * CarNum # Extra Charge applied to each vehicle insured
                 break
            else:
                GlassCoverCost = 0 # No charge applied
                break

    while True:
        try:
            LoanCar = "Y"#input("Do you want optional loaner car coverage(enter Y for Yes or N for No): ").upper()
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if LoanCar != "Y" and LoanCar != "N": # Ensures only approved values are allowed.
                print("Invalid Entry - Must enter Y for Yes or N for No.")
            elif LoanCar == "Y":
                 LoanCarCost = LOAN_CAR_COVER * CarNum # Extra Charge applied to each vehicle insured
                 break
            else:
                LoanCarCost = 0 # NO charge applied
                break

    # Calculations

    TotExtraCosts = (ExtraLiabCost + GlassCoverCost + LoanCarCost)
    TotInsPrem = InsPrem + TotExtraCosts
    TaxPaid = TotInsPrem * HST
    TotInsCost = TotInsPrem + TaxPaid + PROCESS_FEE
    TotInsCostForm = f"{TotInsCost:,.2f}"
    PayMonthly = (TotInsCost + PROCESS_FEE) // 12
    PayMonthlyForm = f"{PayMonthly:,.2f}"
    Subtotal = (TotInsCost - TaxPaid)


    while True:
        try:
            Payment = "F"#input("How do you wish to pay (enter F to pay in full or m to pay monthly): ")
        except ValueError: # Ensures something is entered.
            print("Invalid - Must enter something.")
        else:
            if Payment != "F" and Payment != "M": # Ensures only approved values are allowed.
                print("Invalid Entry - Must be either F and M")
            if Payment == "F":
                 PaymentType = TotInsCost  #
                 PaymentType1 = TotInsCostForm # Value to be appended into the Policies.dat File
                 break
            else:
                PaymentType = PayMonthly
                PaymentType1 = PayMonthlyForm # Value to be appended into the Policies.dat File
                break
    while True:
        try:
            PolicyDateInput = "2021-12-13"#input("Enter the purchase date(YYYY-MM-DD): ")
            PolicyDate = datetime.datetime.strptime(PolicyDateInput, "%Y-%m-%d")  # Convert time string into an object
            PolDate = CUR_DATE.replace(PolicyDate.year, PolicyDate.month, PolicyDate.day)  # Replace the datetime.now()
            # with the time object that was converted from the input to give it an accurate time and date of the
            # current time
            CurrentMonth = PolDate.month
        except ValueError:  # Check to ensure something is entered and not left blank
            print("Invalid Entry - please re-enter the date of purchase.")
        else:
            if PolDate < CUR_DATE:  # check to ensure invoice date does not pre date the current date
                print("Invalid Entry - Date of Purchase cannot occur in the past.")
            elif PolDate.day > 25:
                MonPayDate = PolDate.replace(month=add_month(PolDate, 2)).replace(day=1) #Payment Date scheduled for
                                                                                         #the 1st of the month following
                                                                                         #the next month
                break
            else: # PolDate.day <=25:
                MonPayDate = PolDate.replace(month=add_month(PolDate, 1)).replace(day=1) #Payment Date scheduled for
                                                                                         #the 1st of the following month
                break

    # Formatting
    CurDateForm = datetime.date.strftime(CUR_DATE, "%d-%B-%y")
    MonPayDateForm = datetime.date.strftime(MonPayDate, "%d-%B-%y")
    PolicyNumForm = f"{POLICY_NUM}-{CustFirstName[0]}{CustLastName[0]}"
    PolicyNumPad = f"{PolicyNumForm:>13}"
    CarNumPad = f"{CarNum:>9}"
    ExtraLiabCostForm = f"${ExtraLiabCost:,.2f}"
    ExtraLiabCostPad = f"{ExtraLiabCostForm:>16}"
    GlassCoverCostForm = f"${GlassCoverCost:,.2f}"
    GlassCoverCostPad = f"{GlassCoverCostForm:>17}"
    LoanCarCostForm = f"${LoanCarCost:,.2f}"
    LoanCarCostPad = f"{LoanCarCostForm:>14}"
    TotExtraCostsForm = f"${TotExtraCosts:,.2f}"
    TotExtraCostsPad = f"{TotExtraCostsForm:>16}"
    InsPremForm = f"${InsPrem:,.2f}"
    InsPremPad = f"{InsPremForm:>10}"
    TaxPaidForm = f"${TaxPaid:,.2f}"
    TaxPaidPad = f"{TaxPaidForm:>10}"
    PaymentPad = f"{Payment:>10}"
    TotInsCostForm1 = f"${TotInsCost:,.2f}"
    TotInsCostForm2 = f"{TotInsCost:,.2f}"
    PayMonthlyForm1 = f"${PayMonthly:,.2f}"
    PayMonthlyForm2 = f"{PayMonthly:,.2f}"
    HSTPad = f"{HST:>6}"
    SubtotalForm = f"${Subtotal:,.2f}"
    SubtotalPad = f"{SubtotalForm:>11}"
    PaymentTypeForm = f"${PaymentType:,.2f}"
    PaymentTypePad = f"{PaymentTypeForm:>14}"

    print()
    print()
    print(COMP_NAME)
    print()
    print(f"Date: {CurDateForm}")
    print("=" * 39)
    print("Customer Information:")
    print(f"    {CustFirstName} {CustLastName}")
    print(f"    {PhoneNum}")
    print(f"    {StAdd}")
    print(f"    {City}, {Prov} {PostCode}")
    print()
    print(f"Policy Number:            {PolicyNumPad}")
    print(f"Number Cars:                  {CarNumPad}")
    print("Extra Costs")
    print(f"Extra Liability Cost:  {ExtraLiabCostPad}")
    print(f"Glass Coverage Cost:  {GlassCoverCostPad}")
    print(f"Loaner Car Cost:         {LoanCarCostPad}")
    print(f" " * 29, "*" * 9)
    print(f"Total Extra Cost:      {TotExtraCostsPad}")
    print()
    print(f"Insurance Cost:              {InsPremPad}")
    print(f"Method of Payment:           {PaymentPad}")
    print(f"Tax Rate:                     {HSTPad}(%)")
    print(f"Subtotal:                   {SubtotalPad}")
    print(f" " * 29, "*" * 9)
    print(f"Total Cost:              {PaymentTypePad}")
    print()
    print("=" * 39)
    print("One Stop Insurance, If you don't Stop..\n "
          "   We still got you covered!!")
    print()
    print()

    anykey = input("Do you wish to enter in another customer? Yes (Y) or No (N): ").upper() # Check stop to allow user to
                                                                                            # re-enter data if something
                                                                                            # was incorrect
    print()
    if anykey == "": # Ensures something was entered.
        print("Invalid Entry - Must enter something.")
    elif anykey == "Y":
        continue # Return back to the start of the program
    else: # Allow information to be added into and continue where you the user left off
        f = open('Policies.dat', 'a') # Allows Input Information Appended to the Policies.dat File
        f.write(f"{PolicyNumForm},") # Policy Number Format
        f.write(f"{MonPayDate},") # Payment Date
        f.write(f"{CustFirstName},") # Customer's First Name
        f.write(f"{CustLastName},") # Customer's Last Name
        f.write(f"{StAdd},") # Customer's Street Address
        f.write(f"{City},") # City
        f.write(f"{Prov},") # Province
        f.write(f"{PostCode},") # Postal Code
        f.write(f"{PhoneNum},") # Customer's Phone Number
        f.write(f"{CarNum},") # Number of vehicles being insured
        f.write(f"{ExtraLiab},") # Extra Liability Coverage (Yes(Y) or No(N))
        f.write(f"{GlassCover},") # Glass Coverage (Yes(Y) or No(N))
        f.write(f"{LoanCar},") # Loaner Car Coverage (Yes(Y) or No(N))
        f.write(f"{Payment},") # Extra Liability Coverage (Full(F) or Monthly(M))
        f.write(f"{PaymentType1}\n")

        print("Saving...", end='') # Message to let the user know that the input information is being saved to the
                                   # Policies.dat File
        for wait in range(1,10):
            print('*', end='')

        print()
        print("Policy processed and saved.") # Message to the user to let them know the input information has been saved
                                             # to the Policies.dat File
        print()
        POLICY_NUM += 1 # Policy Number Counter

        f = open('OSICDef.dat', 'w') # Writes information back to the OSICDef.dat File
        f.write("{}\n".format(str(POLICY_NUM))) # Writes back the new Customer Policy number to the OSICDef.dat File
        f.write("{}\n".format(str(BASIC_PREM))) # Writes back the Basic Insurance Premium to the OSICDef.dat File
        f.write("{}\n".format(str(DISCOUNT))) # Writes back the Discount to the OSICDef.dat File
        f.write("{}\n".format(str(LIAB_COVERAGE))) # Writes back the Extra Liability Coverage to the OSICDef.dat File
        f.write("{}\n".format(str(GLASS_COVERAGE))) # Writes back the Glass Coverage to the OSICDef.dat File
        f.write("{}\n".format(str(LOAN_CAR_COVER))) # Writes back the Loaner Car Coverage to the OSICDef.dat File
        f.write("{}\n".format(str(HST))) # Writes back the HST(15%) to the OSICDef.dat File
        f.write("{}\n".format(str(PROCESS_FEE))) # Writes back the Process Fee to the OSICDef.dat File
        f.close()
        break

    anykey = input("Do you wish to enter in another customer? Yes (Y) or No (N): ").upper() # Check stop to allow user to
                                                                                            # re-enter data more data into
                                                                                            # the program by returning to
                                                                                            # the start of the program
    print()
    if anykey == "": # Ensures something was entered
        print("Invalid Entry - Must enter something.")
    elif anykey == "Y":
        continue # Return back to the start of the program
    else: # Print out Reports for all the current data added into the Policies.dat File
        print()
        print("ONE STOP INSURANCE COMPANY")
        print(f"POLICY LISTING AS OF {CurDateForm}")  # dd-Mon-yy

        print("POLICY  CUSTOMER               INSURANCE         EXTRA           TOTAL")
        print("NUMBER  NAME                    PREMIUM          COSTS          PREMIUM")
        print("=" * 71)

        PolicyCtr1 = 0 # Defining the start of the Policy Counter
        InsPremAcc = 0 # Defining the start of the Insurance Premium Accumulator
        ExtraCostsAcc = 0 # Defining the start of the Extra Costs Accumulator
        TotalPremAcc = 0  # Defining the start of the Total Premium Accumulator

        f = open("Policies.dat", 'r') # Opening the Policies.dat File to read information from within it

        for PolicyLineInfo in f: # For Loop to call information from the Policies.dat File
            PolicyData = PolicyLineInfo.split(',') # Removes the " , " out of the info in the Policies.dat File when called
            PolicyNum = PolicyData[0].strip() # Customer Policy Number called from Policies.dat File
            CustFirstName = PolicyData[2].strip() # Customer First name called from Policies.dat File
            CustLastName = PolicyData[3].strip() # Customer Last name called from Policies.dat File
            CustFullName = f"{CustFirstName} {CustLastName}" # Full Name of the customer for report alignment purposes
            print("{} {:<20}   ${:>3,.2f}        ${:>3,.2f}       ${:>3,.2f}".format(PolicyNumForm, CustFullName, InsPrem,
                                                                                     TotExtraCosts, TotInsCost))

            PolicyCtr1 += 1 # Policy Number Counter
            InsPremAcc += InsPrem # Insurance Premium Accumulator
            ExtraCostsAcc += TotExtraCosts # Extra Costs Accumulator
            TotalPremAcc += TotInsCost # Total Insurance Premium Accumulator

        print("=" * 71)
        print("Total Policies: {:<5}         ${:<12,.2f}  ${:<12,.2f}   ${:<12,.2f}".format(PolicyCtr1, InsPremAcc,
                                                                                            ExtraCostsAcc, TotalPremAcc))
        f.close()

        print()
        print()
        print()
        print("ONE STOP INSURANCE COMPANY")
        print(f"MONTHLY PAYMENT LISTING AS OF {MonPayDateForm}")  # dd-Mon-yy

        print("POLICY   CUSTOMER              TOTAL                          TOTAL        MONTHLY")
        print("NUMBER   NAME                 PREMIUM           HST            COST        PAYMENT")
        print("=" * 82)

        PolicyCtr2 = 0 # Defining the start of the Policy Counter
        TotInsPremAcc = 0 # Defining the start of the Total Insurance Premium Accumulator
        HSTAcc = 0 # Defining the start of the HST(Taxes Paid) Accumulator
        TotalCostAcc = 0 # Defining the start of the Total Cost Accumulator
        MonthPaymentAcc = 0 # Defining the start of the Monthly Payment Accumulator

        f = open("Policies.dat", 'r') # Opening the Policies.dat File to read information from within it
        for PolLineInfo in f: # For Loop to call information from the Policies.dat File
            PolicyData = PolLineInfo.split(',') # For Loop to call information from the Policies.dat File
            PolicyNum = (PolicyData[0].strip()) # Customer Policy Number called from Policies.dat File
            CustFirstName = (PolicyData[2].strip()) # Customer First name called from Policies.dat File
            CustLastName = (PolicyData[3].strip()) # Customer Last name called from Policies.dat File
            CustFullName = f"{CustFirstName} {CustLastName}" # Full Name of the customer for report alignment purposes
            print(
                "{} {:<20} ${:>5,.2f}        ${:>6,.2f}        ${:>5,.2f}       ${:>5,.2f}".format(PolicyNum, CustFullName,
                                                                                          TotInsPrem,
                                                                                          TaxPaid,
                                                                                          TotExtraCosts, PayMonthly))

            PolicyCtr2 += 1 # Policy Number Counter
            TotInsPremAcc += TotInsPrem # Total Insurance Premium Accumulator
            HSTAcc += TaxPaid # HST(Taxes Paid) Accumulator
            TotalCostAcc += TotExtraCosts # Total Cost Accumulator
            MonthPaymentAcc += PayMonthly # Monthly Payment Accumulator


        print("=" * 82)
        print(
            "Total policies: {:<5}       ${:<12,.2f}   ${:<12,.2f} ${:<12,.2f}  ${:<12,.2f}".format(PolicyCtr1,
                                                                                                     TotInsPremAcc,
                                                                                                     HSTAcc,
                                                                                                     TotalCostAcc,
                                                                                                     MonthPaymentAcc))
        f.close()
        break

