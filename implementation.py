from CloseToUs import CloseToUs

"""
#Local file
app = CloseToUs(
    filename='test_data/customers.txt',
    localFile=True,
    outfile='TestOut.txt'
)


sorted_result = app.run()

"""

#File from URL
app = CloseToUs(
    filename='https://s3.amazonaws.com/intercom-take-home-test/customers.txt',
    localFile=False,
    outfile='TestOut_url.txt'
)

#Get sorted result
sorted_result = app.run()

