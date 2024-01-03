
from django.shortcuts import render,redirect, get_object_or_404

from .models import REPORT
def report(request):
    if request.user.is_authenticated:
        try:
            report = REPORT.objects.filter(user=request.user)
            # report = report_list.order_by('reportID').last()
            user = report[1].user
            script = report[1].script
            reportID = report[1].reportID
            questions = report[1].questions
            answers = report[1].answers
            voice_analysis = report[1].voice_analysis
            attitude_analysis = report[1].attitude_analysis
            script_analysis = report[1].script_analysis
            date = report[1].rDatetime
            
            #Q & A split
            questions = questions.split(',')
            answers = answers.split(',')
            q1 = questions[0].lstrip("['").rstrip("'")
            q2 = questions[1].strip("'")
            q3 = questions[2].lstrip("'").rstrip("']")
            a1 = answers[0].lstrip("['").rstrip("'")
            a2 = answers[1].strip("'")
            a3 = answers[2].lstrip("'").rstrip("']")
            
            return render(request,'report.html', {'user': user, 'script': script, 'reportID': reportID,
                                                  'q1': q1, 'q2': q2, 'q3': q3,
                                                  'a1': a1, 'a2': a2, 'a3': a3,
                                                  'voice_analysis': voice_analysis, 'attitude_analysis': attitude_analysis, 'script_analysis': script_analysis,
                                                  'date': date, 'report_list': report})
        except:
            print('error, multiple returns')
            redirect('/')
    return redirect('/')

# def detail(request, no):
#     if request.user.is_authenticated:
#         try:
#             report = REPORT.objects.filter(user=request.user)
#             user = report[no].user
#             script = report[no].script
#             reportID = report[no].reportID
#             questions = report[no].questions
#             answers = report[no].answers
#             voice_analysis = report[no].voice_analysis
#             attitude_analysis = report[no].attitude_analysis
#             script_analysis = report[no].script_analysis
#             date = report[no].rDatetime
            
#             #Q & A split
#             questions = questions.split(',')
#             answers = answers.split(',')
#             q1 = questions[0].lstrip("['").rstrip("'")
#             q2 = questions[1].strip("'")
#             q3 = questions[2].lstrip("'").rstrip("']")
#             a1 = answers[0].lstrip("['").rstrip("'")
#             a2 = answers[1].strip("'")
#             a3 = answers[2].lstrip("'").rstrip("']")
            
#             return render(request,'report.html', {'user': user, 'script': script, 'reportID': reportID,
#                                                   'q1': q1, 'q2': q2, 'q3': q3,
#                                                   'a1': a1, 'a2': a2, 'a3': a3,
#                                                   'voice_analysis': voice_analysis, 'attitude_analysis': attitude_analysis, 'script_analysis': script_analysis,
#                                                   'date': date, 'report_list': report})
#         except:
#             print('error, multiple returns')
#             redirect('/')
#     return redirect('/')