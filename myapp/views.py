from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
import time

global users
users = []
global offer
offer = []
global answer
answer = []
global candidate1
candidate1 = []
global candidate2
candidate2 = []
global flag
flag = 0
# Create your views here.

def homepage(request):
	return render(request, 'myapp/homepage.html', {})


def login(request):
    global flag
    print request.GET.get('text')
    data = json.loads(request.GET.get('text'))
    print "000000000000000000000000000000"
    print data
    print "333333333333333333333333333333"
    if data['name'] == 'user1':
        if (data['type'] == "login"):
            print 'User is requesting to log in'
            # Inform user this name is already exist
            if data['name'] in users:
                jsonData = {'type': "login",'success': False}
                return JsonResponse(jsonData, safe=False)
            # log user in and inform user 
            else:
                jsonData = {'type': 'login','success': True}
                print "%s Added to Group" % data['name']
                users.append(data['name'])
                return JsonResponse(jsonData, safe=False)

        elif data['type'] == 'offer':
        # if the connection type is offer from user to another
            print "storing offer"
            # If another user is logged in then forward this offer
            offer.append(data['offer'])
            return JsonResponse({'type': 'receivedOffer'})

        elif (data['type'] == "candidate"):
            print 'Storing candidate'
            candidate1.append(data['candidate'])
            return JsonResponse({'type': 'receivedCandiadate'})
        elif (len(answer)>0):
            print "Got an answer"
            jsonData = {'type': 'answer',
                        'answer': answer.pop()}
            return JsonResponse(jsonData, safe=False)
        elif (len(candidate2)>0):
            print "Got an candidate"
            jsonData = {'type': 'candidate',
                        'candidate': candidate2.pop(0)}
            return JsonResponse(jsonData, safe=False)
        else:
            print "Nothing here"
            return JsonResponse({'type': 'Junk'})

            '''
            jsonData = {'type': 'answer',
                        'answer': data['answer']}
            return JsonResponse(jsonData, safe=False) 
            '''
        '''
        # if the connection type is answer, then forward it to another
        elif (data['type'] == "answer"):
            answer.append(data['answer'])
            print 'Forwarding answer to'
            flag = 1
            jsonData = {'type': 'AtAnswer'}
            return JsonResponse(jsonData, safe=False)
        '''
    elif data['name'] == 'user2':
        print "[][][][][][][][][][][][][][][][][]"
        print data['type']
        print "[][][][][][][][][][][][][][][][][]"
        
        if (data['type'] == "login"):
            print 'User is requesting to log in'
            # Inform user this name is already exist
            if data['name'] in users:
                jsonData = {'type': "login",'success': False}
                return JsonResponse(jsonData, safe=False)
            # log user in and inform user 
            else:
                jsonData = {'type': 'login','success': True}
                print "%s Added to Group" % data['name']
                users.append(data['name'])
                return JsonResponse(jsonData, safe=False)

        # if the connection type is answer, then forward it to another
        elif (data['type'] == "answer"):
            answer.append(data['answer'])
            print 'Storing answer [][][][][][][][][][][][][][][][][][][]'
            jsonData = {'type': 'recievedAnswer'}
            return JsonResponse(jsonData, safe=False)

        elif (data['type'] == "candidate"):
            print 'Storing candidate'
            candidate2.append(data['candidate'])
            return JsonResponse({'type': 'receivedCandiadate'})

        elif (len(offer)>0):
            print "Got an offer"
            jsonData = {'type': 'offer',
                        'offer': offer.pop(),
                        'name': 'user2'}
            return JsonResponse(jsonData, safe=False)
        elif (len(candidate1)>0):
            print "Got an candidate"
            jsonData = {'type': 'candidate',
                        'candidate': candidate1.pop(0)}
            return JsonResponse(jsonData, safe=False)
        else:
            print "Nothing here"
            return JsonResponse({'type': 'Junk'})

#    print data
#    print "11111111111111111111111111111111111111"
#    print data['type']
#    print "11111111111111111111111111111111111111"
    
    #    print 'From: %s' % users[hash(str(message.reply_channel))]
    '''
        jsonData = {'type': 'candidate',
                    'candidate': data['candidate']}
        jsonData = {'type': 'AtCandidate'}
        return JsonResponse(jsonData, safe=False)
	'''

    '''
    jsonData = {'type': 'answer',
                'answer': data['answer']}
    return JsonResponse(jsonData, safe=False)
    '''

