from django.shortcuts import render
import pickle
import numpy as np


def home(request):
    if request.method == 'POST':
        from_explore = request.POST['from_explore']
        from_home = request.POST['from_home']
        likes = request.POST['likes']
        follows = request.POST['follows']
        saves = request.POST['saves']
        profile_visits = request.POST['profile_visits']
        shares = request.POST['shares'] 

        features = np.array([[from_explore, follows, likes, from_home, saves, profile_visits, shares]])

        linear_regression = pickle.load(open('static\Linear_Regression.pkl','rb'))

        prediction = linear_regression.predict(features)
        result = prediction[0]

        return render(request, 'index.html', {'result': result} )

    return render(request, 'index.html')  