from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import pickle
def home(request):
    return render(request, 'home.html')

def predictor(request):
    if request.POST:
        model = pickle.load(open('gradient_boost_regression_model.pkl','rb'))
        venue = request.POST['venue']
        battingteam = request.POST['batting-team']
        bowlingteam = request.POST['bowling-team']
        if battingteam == bowlingteam:
            messages.success(request, 'Do not select same batting and bowling team at the same time')
            return redirect('predictor')
        runs = request.POST['runs']
        wickets = request.POST['wickets']
        overs = request.POST['overs']
        runs_in_prev_5 = request.POST['runs_in_prev_5']
        wickets_in_prev_5 = request.POST['wickets_in_prev_5']
        stadium = float(venue)
        bat = float(battingteam)
        ball = float(bowlingteam)
        score = float(runs)
        player_down = float(wickets)
        finished_overs = float(overs)
        if player_down == 10:
            context = {'output':score}
            return render(request,'predict.html',context)
        if finished_overs == 20:
            context = {'output':score}
            return render(request,'predict.html',context)
        if finished_overs<5.0:
            messages.success(request,'please enter overs greater than 5.0 for more precise prediction')
            return redirect('predictor')
        score_in_prev_5 = float(runs_in_prev_5)
        w_in_prev_5 = float(wickets_in_prev_5)
        if score<0 or player_down<0 or finished_overs<0:
            messages.success(request,'please enter positive number only')
            return redirect('predictor')
        if score<score_in_prev_5:
            messages.success(request,'please enter correct runs scored in previous 5 overs, it can not be greater than total runs scored')
            return redirect('predictor')
        if player_down<w_in_prev_5:
            messages.success(request,'please enter correct wickets taken in previous 5 overs, it can not be greater than total wickets fallen')
            return redirect('predictor')
        list = [stadium,bat,ball,score,player_down,finished_overs,score_in_prev_5,w_in_prev_5]
        ans = model.predict([list])
        output = int(ans)
        context = {'output':output,'stadium':stadium,'bat':bat,'ball':ball,'score':score,'player_down':player_down,'finished_overs':finished_overs,'score_in_prev_5':score_in_prev_5,'w_in_prev_5':w_in_prev_5}
        return render(request, 'predict.html', context)

    return render(request, 'predict.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_pdf(request):
    fs = FileSystemStorage()
    filename = 'IPL_dashboard.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="IPL_dashboard.pdf"'
            response['Content-Disposition'] = 'inline; filename="IPL_dashboard.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
