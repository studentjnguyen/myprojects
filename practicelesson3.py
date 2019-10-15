
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Jeremiah Eaten by Man",
             "Legislature Announces New Laws",
             "Jeremiah Discovers Boolean Inherent in System",
             "Cat Rescues Jeremiah Stuck in Tree",
             "Brave Knight Runs Away",
             "Paperbook Review Totally Traffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    if len(news_ticker) > 140:
        print(len(news_ticker))
    else:
        news_ticker += headline + " "
print(news_ticker)
