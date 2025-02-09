from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)
model = pickle.load(open('savemodel.pkl', 'rb'))

@app.route('/')
def home():
    result = " "
    return render_template('index.html', result_text=result)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Player_Age = float(request.form['Player_Age'])
    Player_Weight = float(request.form['Player_Weight'])
    Player_Height = float(request.form['Player_Height'])
    Previous_Injuries = request.form['Previous_Injuries']
    Training_Intensity = float(request.form['Training_Intensity'])
    Recovery_Time = request.form['Recovery_Time']
    result = model.predict([[Player_Age, Player_Weight, Player_Height, Previous_Injuries, Training_Intensity, Recovery_Time]])[0]

    # Check if result indicates likelihood of injury
    if result == 1:
        result_text = "You might get injured."
    else:
        result_text = "You're less likely to get injured."

    # Pass the result_text to the template
    return render_template('index.html', result_text=result_text)

if __name__=='__main__':
    app.run(debug=True)
