# Mark: Mostly complete — the calculation and 2-decimal rounding are correct.
# Improvement: Use the requested names euro_rate and dollar_rate, and label each output as euros or US dollars.
euro = 1.17
dollar = 1.26
pounds = float(input("amount in pounds: "))
print(round(pounds * euro, 2))
print(round(pounds * dollar, 2))
