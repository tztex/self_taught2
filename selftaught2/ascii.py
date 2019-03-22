# the ord function tells us value of ascii character
# print (ord('h'))
# each character represented by number 0-256 in 8 bits of memory
# unicode is universal code for millions of characters and character set
# utf-8 is best, either 1,2,3, or 4 characters. UTF overlaps with ascii and is recomended to
# exchange data between systems
# python sends data in bytes and decode goes from bytes to unicode.
# in python all strings are unicode when we use sockets to talk to network or db we must
# encode and decode usually to utf-8
# decode is method in bytes class

# urllib is a library that does all the socket work for us and makes web pages
# look like a file.
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in hand:
    #print(line.decode().strip())

