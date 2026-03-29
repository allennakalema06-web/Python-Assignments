# Write down steps each with code examples one can follow to create someone's net pay after tax
# Osman get a gross pay of 15,000,000 and he pays a tax of 25%, calculate Osman's net pay using code step by step.
# Step 1. define a function called gross_pay, this consists of the gross variable
def gross_pay():
    gross = 15000000
    # Use return to expose the gross value to make it accessible to anyone to use 
    return gross

# Step 2. define a function called tax_pay 
def tax_pay():
    # return exposes the gross and its multiplied by the tax rate to calculate the amount of tax Osman pays per month
    return gross_pay() * 0.25
# call the tax_pay function to be excecuted 
print(tax_pay())
# Step 3. define a function called net_pay
def net_pay():
    #call both the gross_pay and tax_pay functions and subtract them to calculate the net pay that Osman gets per month
    print(gross_pay() - tax_pay())
# call the net_pay function to be excecuted     
net_pay()    