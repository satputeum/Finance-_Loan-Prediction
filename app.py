import numpy as np
import sklearn
import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder
import pandas as pd
app = Flask(__name__)

model = pickle.load(open('Dt_loan.pkl', 'rb'))

@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')
label = LabelEncoder()
@app.route("/predict",methods=['GET','POST'])
def predict():
     if request.method=='POST':
         Loan_amnt = int (request.form["loan_amnt"])
         Int_rate = float(request.form["int_rate"])
         Emp_length = int(request.form["emp_length"])
         Annual_inc = int(request.form["annual_inc"])
         Dti = float(request.form["dti"])
         Delinq_2yrs = int(request.form["delinq_2yrs"])
         Revol_util = float(request.form["revol_util"])
         Total_acc = int(request.form["total_acc"])
         Longest_credit_length = int(request.form["longest_credit_length"])
         Term =(request.form['term'])
         if (  Term == ['60 months']):
              Term = 1
              Term =0
         else :
             Term  = 0
             Term = 1

         Verification_status_verified=(request.form['verification_status'])
         if(Verification_status_verified=='verified'):
             Verification_status_verified=1
             Verification_status_not_verified=0
         Purpose_Any=(request.form['purpose'])
         if (Purpose_Any == ['car'],Purpose_Any == ['credit_card'],Purpose_Any == ['debt_consolidation'],
             Purpose_Any == ['educational'],Purpose_Any == ['home_improvement'],
             Purpose_Any == ['house'],Purpose_Any == ['major_purchase'],
             Purpose_Any == ['medical'],Purpose_Any == ['moving'],
             Purpose_Any == ['other'],
             Purpose_Any == ['renewable_energy'],
             Purpose_Any == ['small_business'],
             Purpose_Any == ['vacation'],
             Purpose_Any == ['wedding']):
             Purpose_Any= 0
             Purpose_Any=1
             Purpose_Any=2
             Purpose_Any=3
             Purpose_Any=4
             Purpose_Any=5
             Purpose_Any=6
             Purpose_Any=7
             Purpose_Any=8
             Purpose_Any=9
             Purpose_Any=10
             Purpose_Any=11
             Purpose_Any=12
             Purpose_Any=13

         Addr_state_All = (request.form['addr_state'])
         if( Addr_state_All == ['AL'],Addr_state_All == ['AR'], Addr_state_All == ['AZ'],
            Addr_state_All == ['CA'],Addr_state_All == ['CO'],Addr_state_All == ['CT'],Addr_state_All == ['DC'],
            Addr_state_All == ['DE'],Addr_state_All == ['FL'],Addr_state_All == ['GA'],
            Addr_state_All == ['HI'],Addr_state_All == ['IA'],
            Addr_state_All == ['ID'],Addr_state_All == ['IL'],
            Addr_state_All == ['IN'],
            Addr_state_All == ['KS'],Addr_state_All == ['KY'],
            Addr_state_All == ['LA'],
            Addr_state_All == ['MA'],Addr_state_All == ['MD'],
            Addr_state_All == ['ME'],Addr_state_All == ['MI'],
            Addr_state_All == ['MN'],Addr_state_All == ['MO'],
            Addr_state_All == ['MS'],
            Addr_state_All == ['MT'],Addr_state_All == ['NC'],
            Addr_state_All == ['NE'],Addr_state_All == ['NH'],
            Addr_state_All == ['NJ'],Addr_state_All == ['NM'],
            Addr_state_All == ['NV'],
            Addr_state_All == ['NY'],Addr_state_All == ['OH'],
            Addr_state_All == ['OK'],Addr_state_All == ['OR'],
            Addr_state_All == ['PA'],
            Addr_state_All == ['RI'],Addr_state_All == ['SC'],
            Addr_state_All == ['SD'], Addr_state_All == ['TN'],
            Addr_state_All == ['TX'],Addr_state_All == ['UT'],
            Addr_state_All == ['VA'],Addr_state_All == ['VT'],
            Addr_state_All == ['WA'],Addr_state_All == ['WI'],
            Addr_state_All == ['WV'],Addr_state_All == ['WY']):

             Addr_state_All = 0
             Addr_state_All = 1

             Addr_state_All= 2
             Addr_state_All= 3
             Addr_state_All= 4
             Addr_state_All= 5
             Addr_state_All= 6
             Addr_state_All= 7
             Addr_state_All= 8
             Addr_state_All= 9
             Addr_state_All= 10
             Addr_state_All= 11
             Addr_state_All= 12
             Addr_state_All= 13
             Addr_state_All= 14
             Addr_state_All= 15
             Addr_state_All= 16
             Addr_state_All= 17
             Addr_state_All= 18
             Addr_state_All= 19
             Addr_state_All= 20
             Addr_state_All = 21
             Addr_state_All= 22
             Addr_state_All= 23
             Addr_state_All= 24
             Addr_state_All= 25
             Addr_state_All= 26
             Addr_state_All= 27
             Addr_state_All= 28
             Addr_state_All= 29
             Addr_state_All= 30
             Addr_state_All = 31
             Addr_state_All= 32
             Addr_state_All= 33
             Addr_state_All= 34
             Addr_state_All= 35
             Addr_state_All= 36
             Addr_state_All= 37
             Addr_state_All= 38
             Addr_state_All= 39
             Addr_state_All= 40
             Addr_state_All= 41
             Addr_state_All =42
             Addr_state_All = 43
             Addr_state_All = 44
             Addr_state_All = 45
             Addr_state_All = 46
             Addr_state_All= 47
             Addr_state_All = 48
             Addr_state_All = 49
         Home_ownership = (request.form['home_ownership'])
         if (Home_ownership ==['ANY'],
             Home_ownership == ['MORTGAGE'],
             Home_ownership == ['NONE'],
             Home_ownership == ['OTHER'],
             Home_ownership == ['OWN'],
             Home_ownership == ['RENT']):

             Home_ownership =0
             Home_ownership =1
             Home_ownership=2
             Home_ownership =3
             Home_ownership=4
             Home_ownership=5

     cols = [
         "loan_amnt",
         "term",
         "int_rate",
         "emp_length",
         "home_ownership",
         "annual_inc",
         "purpose",
         "addr_state",
         "dti",
         "delinq_2yrs",
         "revol_util",
         "total_acc",
         "longest_credit_length",
         "verification_status",
     ]
     test_data = pd.DataFrame(
         [
             [
             Loan_amnt,
             Int_rate,
             Emp_length,
             Annual_inc,
             Home_ownership,
             Purpose_Any,
             Addr_state_All,
             Dti,
             Delinq_2yrs,
             Revol_util,
             Total_acc,
             Longest_credit_length,
             Term,
             Verification_status_verified
             ]
         ],
         columns=cols,
     )
     pred = model.predict(test_data)
     if pred == 0:
         return render_template(
             "index.html",prediction_text="The Loan will not be a DEFAULTER",pred=pred
         )
     else:
            return render_template(
         "index.html",prediction_text="The Loan will be a DEFAULTER",pred=pred)

if __name__=="__main__":
     app.run(debug=True)
