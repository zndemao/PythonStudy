import urllib.request

#response = urllib.request.urlopen("http://placekitten.com/g/200/300")
response = urllib.request.urlopen("http://placekitten.com.s3.amazonaws.com/homepage-samples/200/286.jpg")
cat_img = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_img)
