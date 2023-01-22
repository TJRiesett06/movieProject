from flask import Blueprint, render_template, request, flash, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #defines route of home page, main page of the website
def home():
    if request.method == 'POST':
        gender = request.form.get('gender')
        current_weight = request.form.get('weight')
        height = request.form.get('height')
        weight_type = request.form.get('weight_type')
        days = request.form.get('days')
        intensity = request.form.get('intensity')
        weight_change = request.form.get('weight_change')
        duration = request.form.get('duration')
        diet_type = request.form.get('diet_type')
        #print(current_weight)
        #print(weight_change)

        # Below are all of the possible error messages if the user doesnt fill out the form correctly or completely.
        if len(current_weight) == 0:
            flash('Please enter a valid weight.', category= 'error')
        elif int(current_weight) < 90 or int(current_weight) > 450:
            flash('Please enter a valid weight.', category= 'error')
        elif gender == "NONE":
            flash('Please enter a gender.', category='error')
        elif height == "NONE":
            flash('Please enter a height.', category='error')
        elif weight_type == "NONE":
            flash('Please enter a weight goal.', category='error')
        elif weight_change == "NONE":
            flash('Please enter a goal weight.', category='error')
        elif days == "NONE":
            flash('Please enter a number of days.', category='error')
        elif intensity == "NONE":
            flash('Please enter an intensity.', category='error')
        elif duration == "NONE":
            flash('Please enter a duration period.', category='error')
        elif diet_type == "NONE":
            flash('Please enter a diet restriction.', category='error')
        elif weight_type == "lose" and weight_change == "0":
            flash('Please enter a valid goal weight.', category = 'error')
        elif weight_type == "gain" and weight_change == "0":
            flash('Please enter a valid goal weight.', category = 'error')
        elif weight_type == "maintain" and weight_change != "0":
            flash('Please select 0 pounds if you wish to maintain weight.', category = 'error')
        elif days == "0" and intensity != "0":
            flash('Please enter a valid intensity level.', category = 'error')
        elif intensity == "0" and days != "0":
            flash('Please enter a valid days of the week.', category = 'error')
        else:
            flash("Success!", category = 'success')

            # begin by calculating BMI Index
            weight_kg = int(current_weight)/2.205
            bmi = (weight_kg/((int(height)) * (int(height))))*10000
            #print(bmi)

            # next find the exercise fitness level
            exer = int(days) * int(intensity)
            #print(exer)

            #begin formulas for different result pages
            # three main categories based off main goal (gain/lose/maintain)

            # if goal is to maintain weight
            if gender == "Male":
                if weight_type == "maintain":
                    if bmi < 20:
                        fitness = 0
                    elif bmi < 28:
                        fitness = 10
                    elif bmi < 32:
                        fitness = 20
                    else:
                        fitness = 30
                    outcome = (fitness + exer) + int(diet_type)
                    # higher outcome value indicates higher level of activity and fitness level
                    #print(outcome)
                    if outcome < 15:
                        return redirect(url_for('results1.result'))
                    elif outcome < 30:
                        return redirect(url_for('results2.result'))
                    elif outcome < 45:
                        return redirect(url_for('results3.result'))
                    elif outcome < 70: #outcome between 90-115
                        return redirect(url_for('results4.result'))
                    #following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400: #vegetarian
                        return redirect(url_for('results15.result'))
                    elif outcome < 800: #vegan
                        return redirect(url_for('results16.result'))
                    else:           #keto
                        return redirect(url_for('results17.result'))

                # if goal is to lose weight
                if weight_type == "lose":
                    if bmi < 18:
                        fitness = 1.5
                    elif bmi < 29:
                        fitness = 1
                    else:
                        fitness = .75

                    d = float(duration)

                    outcome = (fitness * int(weight_change))/(1 + (exer/35) * d) + int(diet_type)
                    # higher outcome = harder to lose weight
                    #print (outcome)
                    if outcome < 5:
                        return redirect(url_for('results5.result'))
                    elif outcome < 13:
                        return redirect(url_for('results6.result'))
                    elif outcome < 17:
                        return redirect(url_for('results7.result'))
                    elif outcome < 20:
                        return redirect(url_for('results8.result'))
                    elif outcome < 90: #outcome between 65-85.5
                        return redirect(url_for('results9.result'))
                    # following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400: #vegetarian
                        return redirect(url_for('results18.result'))
                    elif outcome < 800: #vegan
                        return redirect(url_for('results19.result'))
                    else:           #keto
                        return redirect(url_for('results20.result'))



                # if goal is to gain weight
                if weight_type == "gain":
                    d = float(duration)
                    if bmi < 18:
                        fitness = 3
                    elif bmi < 29:
                        fitness = 2
                    else:
                        fitness = 1

                    if exer < 10:
                        activity = 10
                    elif exer < 20:
                        activity = 8
                    elif exer < 30:
                        activity = 6
                    else:
                        activity = 4

                    if weight_change == "5":
                        diff = 8
                    elif weight_change =="10":
                        diff = 5
                    else:
                        diff = 1

                    outcome = ((activity + diff) * d * fitness) + int(diet_type)
                    #print (outcome)
                    #higher outcome = less calories needed
                    if outcome < 10:
                        return redirect(url_for('results10.result'))
                    elif outcome < 25:
                        return redirect(url_for('results11.result'))
                    elif outcome < 50:
                        return redirect(url_for('results12.result'))
                    elif outcome < 75:
                        return redirect(url_for('results13.result'))
                    elif outcome <109:
                        return redirect(url_for('results14.result'))
                    #max value before special diet is 108
                    # following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400: #vegetarian
                        return redirect(url_for('results21.result'))
                    elif outcome < 800: #vegan
                        return redirect(url_for('results22.result'))
                    else:           #keto
                        return redirect(url_for('results23.result'))


            # the following code is for women

            #female
            else:
                if weight_type == "maintain":
                    if bmi < 20:
                        fitness = 0
                    elif bmi < 28:
                        fitness = 10
                    elif bmi < 32:
                        fitness = 20
                    else:
                        fitness = 30
                    outcome = (fitness + exer) + int(diet_type)
                    # higher outcome value indicates higher level of activity and fitness level
                    # ranges from 0-65
                    #65 requires most calories
                    #print(outcome)
                    if outcome < 15:
                        return redirect(url_for('results24.result'))
                    elif outcome < 30:
                        return redirect(url_for('results25.result'))
                    elif outcome < 45:
                        return redirect(url_for('results26.result'))
                    elif outcome < 70:  # outcome between 90-115
                        return redirect(url_for('results27.result'))
                    # following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400:  # vegetarian
                        return redirect(url_for('results38.result'))
                    elif outcome < 800:  # vegan
                        return redirect(url_for('results39.result'))
                    else:  # keto
                        return redirect(url_for('results40.result'))

                # if goal is to lose weight
                if weight_type == "lose":
                    if bmi < 18:
                        fitness = 1.5
                    elif bmi < 29:
                        fitness = 1
                    else:
                        fitness = .75

                    d = float(duration)

                    outcome = (fitness * int(weight_change)) / (1 + (exer / 35) * d) + int(diet_type)
                    # higher outcome = harder to lose weight
                    #print(outcome)
                    if outcome < 5:
                        return redirect(url_for('results28.result'))
                    elif outcome < 13:
                        return redirect(url_for('results29.result'))
                    elif outcome < 17:
                        return redirect(url_for('results30.result'))
                    elif outcome < 20:
                        return redirect(url_for('results31.result'))
                    elif outcome < 90:  # outcome between 65-85.5
                        return redirect(url_for('results32.result'))
                    # following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400:  # vegetarian
                        return redirect(url_for('results41.result'))
                    elif outcome < 800:  # vegan
                        return redirect(url_for('results42.result'))
                    else:  # keto
                        return redirect(url_for('results43.result'))

                # if goal is to gain weight
                if weight_type == "gain":
                    d = float(duration)
                    if bmi < 18:
                        fitness = 3
                    elif bmi < 29:
                        fitness = 2
                    else:
                        fitness = 1

                    if exer < 10:
                        activity = 10
                    elif exer < 20:
                        activity = 8
                    elif exer < 30:
                        activity = 6
                    else:
                        activity = 4

                    if weight_change == "5":
                        diff = 8
                    elif weight_change == "10":
                        diff = 5
                    else:
                        diff = 1

                    outcome = ((activity + diff) * d * fitness) + int(diet_type)
                    #print(outcome)
                    # higher outcome = less calories needed
                    if outcome < 10:
                        return redirect(url_for('results33.result'))
                    elif outcome < 25:
                        return redirect(url_for('results34.result'))
                    elif outcome < 50:
                        return redirect(url_for('results35.result'))
                    elif outcome < 75:
                        return redirect(url_for('results36.result'))
                    elif outcome < 109:
                        return redirect(url_for('results37.result'))
                    # max value before special diet is 108
                    # following outcomes will be for keto, vegan, and vegetarian
                    elif outcome < 400:  # vegetarian
                        return redirect(url_for('results44.result'))
                    elif outcome < 800:  # vegan
                        return redirect(url_for('results45.result'))
                    else:  # keto
                        return redirect(url_for('results46.result'))


    return render_template("home.html")




