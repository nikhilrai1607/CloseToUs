from CloseToUs import CloseToUs

app = CloseToUs(
    filename='test_data/customers.txt',
    localFile=True,
    outfile='TestOut.txt'
)


sorted_result = app.run()

if len(sorted_result)>0 and sorted_result is not None:
    app.write_result(sorted_result)


app = CloseToUs(
    filename='https://s3.amazonaws.com/intercom-take-home-test/customers.txt',
    localFile=False,
    outfile='TestOut_url.txt'
)


sorted_result = app.run()

if len(sorted_result)>0 and sorted_result is not None:
    app.write_result(sorted_result)