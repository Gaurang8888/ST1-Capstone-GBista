#Submitted as part of ST1 Capstone Project
#Author: Gaurang Bista
#12/05/2023

import tkinter as tk
from Score_Model1 import *

from tkinter import ttk

win = tk.Tk()

#Create a window called Student grade outcome predictions and define windowsize
win.title('Student Grade Outcome Predictions')

win.geometry("900x900")

#Add labels for each feature being used and create a dropdown with possible outcomes
Age =ttk.Label(win,text="Age")
Age.grid(row=0,column=0,sticky=tk.W)
click_Age_var=tk.StringVar()
click_Age_var.set("1: 18-21")
Age_dropdown = ttk.OptionMenu(win, click_Age_var, "1: 18-21","1: 18-21", "2: 22-25", "3: Above 26")
Age_dropdown.grid(row=0,column=1)


sex=ttk.Label(win,text="Gender")
sex.grid(row=1,column=0,sticky=tk.W)
click_sex_var = tk.StringVar()
click_sex_var.set("1:female")
sex_dropdown = ttk.OptionMenu(win, click_sex_var, "1:female","1:female", "2:male")
sex_dropdown.grid(row = 1, column = 1)



graduated_h_school_type =ttk.Label(win,text="Graduated High school type: ")
graduated_h_school_type.grid(row=2,column=0,sticky=tk.W)
click_graduated_h_school_var = tk.StringVar()
click_graduated_h_school_var.set("1: Private")
grad_dropdown = ttk.OptionMenu(win, click_graduated_h_school_var, "1:Private","1:Private", "2:State", "3:Other")
grad_dropdown.grid(row = 2, column = 1)


scholarship_type =ttk.Label(win,text="Scholarship type: ")
scholarship_type.grid(row=3,column=0,sticky=tk.W)
click_scholarship_var = tk.StringVar()
click_scholarship_var.set("1:None")
scholarship_dropdown = ttk.OptionMenu(win, click_scholarship_var, "1:None","1:None", "2:25%", "3: 50%", "4:75%", "5:Full")
scholarship_dropdown.grid(row = 3, column = 1)

additional_work =ttk.Label(win,text="Additional work: ")
additional_work.grid(row=4,column=0,sticky=tk.W)
click_additional_work_var = tk.StringVar()
click_additional_work_var.set("1:Yes")
additional_work_dropdown = ttk.OptionMenu(win, click_additional_work_var, "1:Yes","1:Yes", "2:No")
additional_work_dropdown.grid(row = 4, column = 1)

activity = ttk.Label(win,text="Extracurricular activities: ")
activity.grid(row = 5, column = 0)
click_activity_var = tk.StringVar()
click_activity_var.set("1:Yes")
activity_dropdown = ttk.OptionMenu(win, click_activity_var, "1:Yes","1:Yes", "2:No")
activity_dropdown.grid(row = 5, column = 1)

partner = ttk.Label(win,text="Partner: ")
partner.grid(row = 6, column = 0)
click_partner_var = tk.StringVar()
click_partner_var.set("1:Yes")
partner_dropdown = ttk.OptionMenu(win, click_partner_var, "1:Yes","1:Yes", "2:No")
partner_dropdown.grid(row = 6, column = 1)

total_salary = ttk.Label(win,text="Total Salary: ")
total_salary.grid(row = 7, column = 0)
click_total_salary_var = tk.StringVar()
click_total_salary_var.set("1:135-200 USD")
partner_dropdown = ttk.OptionMenu(win, click_total_salary_var, "1:135-200USD","1:135-200USD", "2:201-270USD", "3:271-340USD", "4: 341-410USD", "5:Above 410 USD")
partner_dropdown.grid(row = 7, column = 1)

transport = ttk.Label(win,text="Transport: ")
transport.grid(row = 8, column = 0)
click_transport_var = tk.StringVar()
click_transport_var.set("1:Bus")
transport_dropdown = ttk.OptionMenu(win, click_transport_var, "1:Bus","1:Bus", "2:Private", "3:Bicycle", "4:Other")
transport_dropdown.grid(row = 8, column = 1)


accomodation = ttk.Label(win,text="Accomodation: ")
accomodation.grid(row = 9, column = 0)
click_accomodation_var = tk.StringVar()
click_accomodation_var.set("1:Rental")
accomodation_dropdown = ttk.OptionMenu(win, click_accomodation_var, "1:Rental","1:Rental", "2:Dormitory", "3:Family", "4:Other")
accomodation_dropdown.grid(row = 9, column = 1)


mother_ed = ttk.Label(win,text="Mothers education: ")
mother_ed.grid(row = 10, column = 0)
click_mother_ed_var = tk.StringVar()
click_mother_ed_var.set("1:Primary School")
mother_ed_dropdown = ttk.OptionMenu(win, click_mother_ed_var, "1:Primary School","1:Primary School", "2:Secondary School", "3:High School", "4:University", "5:MsC", "6:Ph.D.")
mother_ed_dropdown.grid(row = 10, column = 1)

father_ed = ttk.Label(win,text="Fathers education: ")
father_ed.grid(row = 11, column = 0)
click_father_ed_var = tk.StringVar()
click_father_ed_var.set("1:Primary School")
father_ed_dropdown = ttk.OptionMenu(win, click_father_ed_var, "1:Primary School","1:Primary School", "2:Secondary School", "3:High School", "4:University", "5:MsC", "6:Ph.D.")
father_ed_dropdown.grid(row = 11, column = 1)


weekly_study_hours = ttk.Label(win,text="Weekly Study Hours: ")
weekly_study_hours.grid(row = 12, column = 0)
click_weekly_study_hours_var = tk.StringVar()
click_weekly_study_hours_var.set("1:None")
weekly_study_hours_dropdown = ttk.OptionMenu(win, click_weekly_study_hours_var, "1:None","1:None", "2:<5 hours", "3:6-10 hours", "4:11-20", "5:More than 10")
weekly_study_hours_dropdown.grid(row = 12, column = 1)

reading_non_scientific = ttk.Label(win,text="Non Scientific reading frequency: ")
reading_non_scientific.grid(row = 13, column = 0)
click_reading_non_scientific_var = tk.StringVar()
click_reading_non_scientific_var.set("1:None")
reading_non_scientific_dropdown = ttk.OptionMenu(win, click_reading_non_scientific_var, "1:None","1:None", "2:Sometimes", "3:Often")
reading_non_scientific_dropdown.grid(row = 13, column = 1)


reading_scientific = ttk.Label(win,text="Scientific reading frequency: ")
reading_scientific.grid(row = 14, column = 0)
click_reading_scientific_var = tk.StringVar()
click_reading_scientific_var.set("1:None")
reading_scientific_dropdown = ttk.OptionMenu(win, click_reading_scientific_var, "1:None","1:None", "2:Sometimes", "3:Often")
reading_scientific_dropdown.grid(row = 14, column = 1)

seminar_attendance = ttk.Label(win,text="Attends Seminars: ")
seminar_attendance.grid(row = 15, column = 0)
click_seminar_attendance_var = tk.StringVar()
click_seminar_attendance_var.set("1:Yes")
seminar_attendance_dropdown = ttk.OptionMenu(win, click_seminar_attendance_var, "1:Yes","1:Yes", "2:No")
seminar_attendance_dropdown.grid(row = 15, column = 1)

impact_of_projects = ttk.Label(win,text="Impact of Projects: ")
impact_of_projects.grid(row = 16, column = 0)
click_impact_of_projects_var = tk.StringVar()
click_impact_of_projects_var.set("1:Positive")
impact_of_projects_dropdown = ttk.OptionMenu(win, click_impact_of_projects_var, "1:Positive","1:Positive", "2:Negative", "3:Neutral")
impact_of_projects_dropdown.grid(row = 16, column = 1)

class_attendance = ttk.Label(win,text="Class Attendance: ")
class_attendance.grid(row = 17, column = 0)
click_class_attendance_var = tk.StringVar()
click_class_attendance_var.set("1:always")
class_attendance_dropdown = ttk.OptionMenu(win, click_class_attendance_var, "1:always","1:always", "2:sometimes", "3:never")
class_attendance_dropdown.grid(row = 17, column = 1)

preparation_mid_term_company = ttk.Label(win,text="Preparation Midterm Company: ")
preparation_mid_term_company.grid(row = 18, column =0)
click_preparation_midterm_company_var = tk.StringVar()
click_preparation_midterm_company_var.set("1:alone")
preparation_mid_term_company_dropdown = ttk.OptionMenu(win, click_preparation_midterm_company_var, "1:alone","1:alone", "2:with friends", "3:other")
preparation_mid_term_company_dropdown.grid(row = 18, column = 1)

preparation_mid_term_time = ttk.Label(win,text="Preparation Midterm Time: ")
preparation_mid_term_time.grid(row = 19, column = 0)
click_preparation_mid_term_time_var = tk.StringVar()
click_preparation_mid_term_time_var.set("1:closest date to the exam")
preparation_mid_term_time_dropdown = ttk.OptionMenu(win, click_preparation_mid_term_time_var, "1:closest date to the exam","1:closest date to the exam", "2:regularly", "3:never")
preparation_mid_term_time_dropdown.grid(row = 19, column = 1)

taking_notes = ttk.Label(win,text="Taking notes: ")
taking_notes.grid(row = 20, column = 0)
click_taking_notes_var = tk.StringVar()
click_taking_notes_var.set("1:never")
taking_notes_dropdown = ttk.OptionMenu(win, click_taking_notes_var, "1:never","1:never", "2:sometimes", "3:always")
taking_notes_dropdown.grid(row = 20, column = 1)


listening = ttk.Label(win,text="Listening: ")
listening.grid(row = 21, column = 0)
click_listening_var = tk.StringVar()
click_listening_var.set("1:never")
listening_dropdown = ttk.OptionMenu(win, click_listening_var, "1:never","1:never", "2:sometimes", "3:always")
listening_dropdown.grid(row = 21, column = 1)

discussion_improves_interest = ttk.Label(win,text="Discussions increase interest in study: ")
discussion_improves_interest.grid(row = 22, column = 0)
click_discussion_improves_interest_var = tk.StringVar()
click_discussion_improves_interest_var.set("1:never")
discussion_improves_interest_dropdown = ttk.OptionMenu(win, click_discussion_improves_interest_var, "1:never","1:never", "2:sometimes", "3:always")
discussion_improves_interest_dropdown.grid(row = 22, column = 1)



flip_classroom = ttk.Label(win,text="Flip classroom: ")
flip_classroom.grid(row=23, column = 0)
click_flip_classroom_var=tk.StringVar()
click_flip_classroom_var.set("1:not useful")
flip_classroom_dropdown = ttk.OptionMenu(win, click_flip_classroom_var, "1:not useful","1:not useful", "2:useful", "3:N/A")
flip_classroom_dropdown.grid(row = 23, column = 1)


grade_previous = ttk.Label(win,text="Previous grade (GPA): ")
grade_previous.grid(row = 24, column = 0)
click_grade_previous_var = tk.StringVar()
click_grade_previous_var.set("1:<2.00")
grade_dropdown = ttk.OptionMenu(win, click_grade_previous_var, "1:<2.00","1:<2.00", "2:2.00-2.49", "3:2.50-2.99", "4:3.00-3.49", "5:above 3.49")
grade_dropdown.grid(row = 24, column=1)

l1 = ttk.Label(win, text = "", font=("Arial", 18))
l1.grid(row=26, column = 5)


#define a function to predict the grade
def predict_grade():
#Define the numeric keys present in the dataset for each feature
    age = click_Age_var.get()
    if age == "1: 18-21":
        age = 1
    elif age == "2: 22-25":
        age = 2
    elif age == "3: Above 26":
        age = 3

    sex = click_sex_var.get()
    if sex == "1:female":
        sex = 1
    else:
        sex = 2

    graduated_h_school_type = click_graduated_h_school_var.get()
    if graduated_h_school_type == "1:Private":
        graduated_h_school_type = 1
    elif graduated_h_school_type == "2:State":
        graduated_h_school_type = 2
    elif graduated_h_school_type == "3:Other":
        graduated_h_school_type = 3


    scholarship_type = click_scholarship_var.get()
    if scholarship_type == "1:None":
        scholarship_type = 1
    elif scholarship_type == "2:25%":
        scholarship_type = 2
    elif scholarship_type == "3:50%":
        scholarship_type = 3
    elif scholarship_type == "4:75%":
        scholarship_type = 4
    elif scholarship_type == "5:Full":
        scholarship_type = 5

    additional_work = click_additional_work_var.get()
    if additional_work == "1:Yes":
        additional_work = 1
    elif additional_work == "2:No":
        additional_work = 2


    activity = click_activity_var.get()
    if activity == "1:Yes":
        activity = 1
    else:
        activity = 2

    partner = click_partner_var.get()
    if partner == "1:Yes":
        partner = 1
    else:
        partner = 2


    total_salary = click_total_salary_var.get()
    if total_salary == "1:135-200USD":
        total_salary=1
    elif total_salary == "2:201-270USD":
        total_salary = 2
    elif total_salary == "3:271-340USD":
        total_salary = 3
    elif total_salary == "4: 341-410USD":
        total_salary = 4
    elif total_salary == "5:Above 410 USD":
        total_salary = 5


    transport = click_transport_var.get()
    if transport ==  "1:Bus":
        transport = 1
    elif transport == "2:Private":
        transport = 2
    elif transport == "3:Bicycle":
        transport = 3
    elif transport == "4:Other":
        transport = 4

    accomodation = click_accomodation_var.get()
    if accomodation == "1:Rental":
        accomodation = 1
    elif accomodation == "2:Dormitory":
        accomodation = 2
    elif accomodation == "3:Family":
        accomodation = 3
    elif accomodation == "4:Other":
        accomodation = 4


    mother_ed = click_mother_ed_var.get()
    if mother_ed == "1:Primary School":
        mother_ed = 1
    elif mother_ed == "2:Secondary School":
        mother_ed = 2
    elif mother_ed == "3:High School":
        mother_ed = 3
    elif mother_ed == "4:University":
        mother_ed = 4
    elif mother_ed == "5:MsC":
        mother_ed = 5
    elif mother_ed == "6:Ph.D.":
        mother_ed = 6

    father_ed = click_father_ed_var.get()
    if father_ed == "1:Primary School":
        father_ed = 1
    elif father_ed == "2:Secondary School":
        father_ed = 2
    elif father_ed == "3:High School":
        father_ed = 3
    elif father_ed == "4:University":
        father_ed = 4
    elif father_ed == "5:MsC":
        father_ed = 5
    elif father_ed == "6:Ph.D.":
        father_ed = 6


    weekly_study_hours = click_weekly_study_hours_var.get()
    if weekly_study_hours == "1:None":
        weekly_study_hours = 1
    elif weekly_study_hours == "2:<5 hours":
        weekly_study_hours = 2
    elif weekly_study_hours == "3:6-10 hours":
        weekly_study_hours = 3
    elif weekly_study_hours == "4:11-20":
        weekly_study_hours = 4
    elif weekly_study_hours == "5:More than 10":
        weekly_study_hours = 5



    reading_non_scientific = click_reading_non_scientific_var.get()
    if reading_non_scientific == "1:None":
        reading_non_scientific = 1
    elif reading_non_scientific == "2:Sometimes":
        reading_non_scientific = 2
    elif reading_non_scientific == "3:Often":
        reading_non_scientific = 3

    reading_scientific = click_reading_scientific_var.get()
    if reading_scientific == "1:None":
        reading_scientific = 1
    elif reading_scientific == "2:Sometimes":
        reading_scientific = 2
    elif reading_scientific == "3:Often":
        reading_scientific = 3


    seminar_attendance = click_seminar_attendance_var.get()
    if seminar_attendance == "1:Yes":
        seminar_attendance = 1
    else:
        seminar_attendance = 2


    impact_of_projects = click_impact_of_projects_var.get()
    if impact_of_projects == "1:Positive":
        impact_of_projects = 1
    elif impact_of_projects == "2:Negative":
        impact_of_projects = 2
    elif impact_of_projects == "3:Neutral":
        impact_of_projects = 3




    class_attendance = click_class_attendance_var.get()
    if class_attendance == "1:always":
        class_attendance= 1
    elif class_attendance == "2:sometimes":
        class_attendance = 2
    elif class_attendance == "3:never":
        class_attendance = 3



    preparation_mid_term_company = click_preparation_midterm_company_var.get()
    if preparation_mid_term_company == "1:alone":
        preparation_mid_term_company = 1
    elif preparation_mid_term_company == "2:with friends":
        preparation_mid_term_company=2
    elif preparation_mid_term_company == "3:other":
        preparation_mid_term_company =3



    preparation_mid_term_time  = click_preparation_mid_term_time_var.get()
    if preparation_mid_term_time == "1:closest date to the exam":
        preparation_mid_term_time = 1
    elif preparation_mid_term_time == "2:regularly":
        preparation_mid_term_time = 2
    elif preparation_mid_term_time == "3:never":
        preparation_mid_term_time = 3

    taking_notes = click_taking_notes_var.get()
    if taking_notes == "1:never":
        taking_notes = 1
    elif taking_notes == "2:sometimes":
        taking_notes = 2
    elif taking_notes == "3:always":
        taking_notes = 3


    listening = click_listening_var.get()
    if listening == "1:never":
        listening = 1
    elif listening == "2:sometimes":
        listening = 2
    elif listening == "3:always":
        listening = 3


    discussion_improves_interest = click_discussion_improves_interest_var.get()
    if discussion_improves_interest == "1:never":
        discussion_improves_interest = 1
    elif discussion_improves_interest == "2:sometimes":
        discussion_improves_interest= 2
    elif discussion_improves_interest == "3:always":
        discussion_improves_interest = 3


    flip_classroom = click_flip_classroom_var.get()
    if flip_classroom ==  "1:not useful":
        flip_classroom = 1
    elif flip_classroom ==  "2:useful":
        flip_classroom = 2
    elif flip_classroom == "3:N/A":
        flip_classroom = 3


    grade_previous = click_grade_previous_var.get()
    if grade_previous ==  "1:<2.00":
        grade_previous = 1
    elif grade_previous == "2:2.00-2.49":
        grade_previous = 2
    elif grade_previous == "3:2.50-2.99":
        grade_previous = 3
    elif grade_previous == "4:3.00-3.49":
        grade_previous = 4
    elif grade_previous == "5:above 3.49":
        grade_previous = 5


#List all the features and create a button which initiates the prediction
    Student_info = (age, sex, graduated_h_school_type, scholarship_type, additional_work, activity, partner, total_salary, transport, accomodation, mother_ed, father_ed, weekly_study_hours, reading_non_scientific, reading_scientific, seminar_attendance, impact_of_projects, class_attendance, preparation_mid_term_company, preparation_mid_term_time, taking_notes, listening, discussion_improves_interest, flip_classroom, grade_previous)
    grade_prediction = best_model.predict([Student_info])

    result = grade_prediction

    if (grade_prediction == "Fail"):
        l1.config(text = "Prediction: Fail")
    else:
        l1.config(text = "Prediction: Pass")


button = ttk.Button(win, text = "Predict", command = predict_grade)
button.grid(row=5, column = 3)


win.mainloop()