import wolframalpha
app_id = wolframalpha.getfixture('5T67WJ-XHA853GWU3')
client = wolframalpha.Client(app_id)
res = client.query("Hello World")
print(res)