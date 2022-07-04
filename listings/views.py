from django.shortcuts import render

# Create your views here.
def createListing(request):
    #Logic for receiving listing submission
    if request.method == 'POST':
        #Access data and then store it in models
        #May also be able to use cleaned data here
        #Title
        title = request.POST['title']
        #Text-based description
        text = request.POST['text']
        #Starting-bid
        startBid = request.POST['startBid']
        #Image url
        image = request.POST['image']
        #Category
        category = request.POST['category']

        #If I'm not mistaken I'm going to then need to save this data into the models

    #Logic for returning listing submission page for user
    return render(request, "listings/listings.html")

