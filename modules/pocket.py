import urllib2
import json

def pocket(settings):

    developer_key = settings['settings']['modules']['pocket']['developer_key']
    user_key = settings['settings']['modules']['pocket']['user_key']

    unread_count = 0
    read_count = 0
    total_count = 0

    headers = {'Content-Type' : 'application/json; charset=UTF-8','X-Accept': 'application/json'}
    read_data = json.dumps({"consumer_key": developer_key, "access_token": user_key, "state": "archive", "detailType": "simple"})
    unread_data = json.dumps({"consumer_key": developer_key, "access_token": user_key, "state": "unread", "detailType": "simple"})
    url = 'https://getpocket.com/v3/get'

    request = urllib2.Request(url, read_data, headers)
    response = urllib2.urlopen(request)
    parsedResponse = json.load(response)

    for article in parsedResponse["list"]:
        read_count = read_count + 1

    request = urllib2.Request(url, unread_data, headers)
    response = urllib2.urlopen(request)
    parsedResponse = json.load(response)

    for article in parsedResponse["list"]:
        unread_count = unread_count + 1

    total_count = read_count + unread_count

    print "Unread articles: " + str(unread_count)
    print "Read articles: " + str(read_count)
    print ""
    print "Total: " + str(total_count)
