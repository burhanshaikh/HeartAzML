PatientData.csv is a data set of 10801 Patients which consists of the following parameters/features :
AVGHEARTBEATSPERMIN 	PALPITATIONSPERDAY 	 CHOLESTEROL  	BMI 	 HEARTFAILURE 	 AGE  	SEX 	 FAMILYHISTORY 	 SMOKERLAST5YRS 	EXERCISEMINPERWEEK

This data set has been trained on Azure Machine Learning Studio using a Two-Class Boosted Decision Tree to predict whether a patient will suffer
from a heart failure or not.

Some details about the Two-Class Boosted Decision Tree used :

Maximun number of leaves per tree: 20

Learning Rate: 0.2

Number of trees constructed : 100

The second tree corrects the errors of the first tree, the third tree corrects the errors of the first and second trees, and so forth. 
This means that the trees should get better as the "Number of Trees Constructed" parameter is increased,
but this would mean that trees later in the process have a much higher risk of "Overfitting" than trees earlier in the process.  

"Overfitting" is a situation where the model has been trained so heavily that it can extremely accurately predict the training data 
but will be very poor at predicting new observations. 

Fortunately, the algorithm accounts for this by not just taking the prediction from the final tree in the set but it also takes predictions from every tree and averages them together. This greatly lessens the effect of "Overfitting" while still providing accurate predictions.


MLApp.py is a request-response code to use this machine learning model. 

In the response :

"Scored Labels" returns Y or N which shows whether the patient has a high risk for a heart failure.

"Scored Probability" shows the confidence of the prediction.
