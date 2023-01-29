# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a requests

import urllib.request as urllib


def main(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to" , url , " Succesfully")
    print("The response code was: " , response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

if __name__ == '__main__':
    main(input_url)
