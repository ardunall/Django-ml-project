from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required
from .models import DiabetesPrediction
import pandas as pd

from data_model.data_model import make_prediction


import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def index(request):
    return render(request, "index.html")


@login_required
def diabetes_prediction(request):
    make_prediction()
    if request.method == "POST":

        age = float(request.POST.get("age"))
        sex = float(request.POST.get("sex"))
        bmi = float(request.POST.get("bmi"))
        bp = float(request.POST.get("bp"))
        tc = float(request.POST.get("tc"))
        ldl = float(request.POST.get("ldl"))
        hdl = float(request.POST.get("hdl"))
        tch = float(request.POST.get("tch"))
        ltg = float(request.POST.get("ltg"))
        glucose = float(request.POST.get("glucose"))
        user = request.user

        diabetes_model = pd.read_pickle("C:/Users/Asus/Desktop/xxx/projem/data_model/mo3del.pickle")
        result = diabetes_model.predict(
            [[age, sex, bmi, bp, tc, ldl, hdl, tch, ltg, glucose]])
        if result >= 0.75:
            result = "Diabetic"
        else:
            result = "No Diabetes"

        prediction = DiabetesPrediction(
            age=age,
            sex=sex,
            bmi=bmi,
            bp=bp,
            tc=tc,
            ldl=ldl,
            hdl=hdl,
            tch=tch,
            ltg=ltg,
            glucose=glucose,
            result=result,
            user=user)
        prediction.save()

        return HttpResponseRedirect(reverse("diabetes_result"))

    return render(request, "ml.html")

@login_required
def diabetes_result(request):
    prediction = DiabetesPrediction.objects.filter(user=request.user).order_by("-created_at")
    
    has_positive_prediction = any(predict.result == "Diabetic" for predict in prediction)

    positive_message = ""  
    appointment_link = "" 
    blog_link = ""  

    if has_positive_prediction:
        positive_message = "Diyabetiniz var! Lütfen bir doktora danışın ve aşağıdaki linkleri kontrol edin:"
        appointment_link = reverse("home")  
        blog_link = reverse("home") 
    return render(request, "ml2.html", {
        "prediction": prediction,
        "has_positive_prediction": has_positive_prediction,
        "positive_message": positive_message,
        "appointment_link": appointment_link,
        "blog_link": blog_link
    })




def download(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    prediction = DiabetesPrediction.objects.all()
    user = request.user
    prediction = prediction.filter(user=user)

    lines = []

    for predict in prediction:
        lines.append("age " + str(predict.age))
        lines.append("sex " + str(predict.sex))
        lines.append("bmi " + str(predict.bmi))
        lines.append("bp " + str(predict.bp))
        lines.append("tc " + str(predict.tc))
        lines.append("ldl " + str(predict.ldl))
        lines.append("hdl " + str(predict.hdl))
        lines.append("tch " + str(predict.tch))
        lines.append("ltg " + str(predict.ltg))
        lines.append("glucose " + str(predict.glucose))
        lines.append("date " + str(predict.created_at))
        lines.append("result " + str(predict.result))

        lines.append(" ")
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='diabetesresult.pdf')



@login_required
def previous_results(request):
    user = request.user
    predictions = DiabetesPrediction.objects.filter(user=user).order_by('-created_at')
    return render(request, 'previous_results.html', {'predictions': predictions})
