
from django.shortcuts import render,redirect, get_object_or_404
from .models import REPORT
import json

def report(request):
    print(request)
    if request.user.is_authenticated:
        try:
            report = REPORT.objects.filter(user=request.user)
            no = report.count()
            report_last = report.order_by('reportID').last()
            user = report_last.user
            reportID = report_last.reportID
            questions = report_last.questions
            answers = report_last.answers
            voice_analysis = report_last.voice_analysis
            attitude_analysis = report_last.attitude_analysis
            script_analysis = report_last.script_analysis
            total_analysis = report_last.total_analysis
            static_rate = report_last.static_rate
            face_recog_rate = report_last.face_recog_rate
            gap_rate = report_last.gap_rate
            speed_rate = report_last.speed_rate
            surplus_rate = report_last.surplus_rate
            date = report_last.rDatetime
            
            #Q & A split
            questions = json.loads(questions)
            answers = json.loads(answers)
            q1 = questions[0]
            q2 = questions[1]
            q3 = questions[2]
            a1 = answers[0]
            a2 = answers[1]
            a3 = answers[2]
            
            return render(request,'report/report.html', {'user': user, 'reportID': reportID,
                                                    'q1': q1, 'q2': q2, 'q3': q3,
                                                    'a1': a1, 'a2': a2, 'a3': a3,
                                                    'voice_analysis': voice_analysis, 'attitude_analysis': attitude_analysis, 
                                                    'script_analysis': script_analysis, 'total_analysis':total_analysis,
                                                    'date': date, 'report_list': report, 'no':no,
                                                    'static_rate':static_rate, 'face_recog_rate':face_recog_rate,
                                                    'gap_rate':gap_rate, 'speed_rate':speed_rate, 'surplus_rate':surplus_rate})
        except:
            return render(request,'report/zeroReport.html')
    return render(request,'report/zeroReport.html')

def detail(request, no):
    if request.user.is_authenticated:
        try:
            no-=1
            report = REPORT.objects.filter(user=request.user)
            report_pick = report.order_by('reportID')[no]
            user = report_pick.user
            reportID = report_pick.reportID
            questions = report_pick.questions
            answers = report_pick.answers
            voice_analysis = report_pick.voice_analysis
            attitude_analysis = report_pick.attitude_analysis
            script_analysis = report_pick.script_analysis
            total_analysis = report_pick.total_analysis
            static_rate = report_pick.static_rate
            face_recog_rate = report_pick.face_recog_rate
            gap_rate = report_pick.gap_rate
            speed_rate = report_pick.speed_rate
            surplus_rate = report_pick.surplus_rate
            date = report_pick.rDatetime
            
            #Q & A split
            questions = json.loads(questions)
            answers = json.loads(answers)
            q1 = questions[0]
            q2 = questions[1]
            q3 = questions[2]
            a1 = answers[0]
            a2 = answers[1]
            a3 = answers[2]
            
            return render(request,'report/report.html', {'user': user, 'reportID': reportID,
                                                  'q1': q1, 'q2': q2, 'q3': q3,
                                                  'a1': a1, 'a2': a2, 'a3': a3,
                                                  'voice_analysis': voice_analysis, 'attitude_analysis': attitude_analysis, 
                                                  'script_analysis': script_analysis, 'total_analysis':total_analysis,
                                                  'date': date, 'report_list': report,'no':no+1,
                                                  'static_rate':static_rate, 'face_recog_rate':face_recog_rate,
                                                  'gap_rate':gap_rate, 'speed_rate':speed_rate, 'surplus_rate':surplus_rate,})
        except:
            return render(request,'report/zeroReport.html')
    else:
        return redirect('/login')