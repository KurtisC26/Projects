Ket notes on the concepts related to machine learning in python



<h2>1-Preprocessing:</h2>
When preparing the data, we must only feature scale variables after we wplit the data. The reason is, scaling the data leverages key statistics such as the mean and standard deviation. If we feature scale before splitting, some of the statistics representing the train set will leak into the test set causing potential errors in the accuracy of the predictions
<br>
<br>
There are two feature scaling options: Standardization and normalization
1) Standardization will result in values between -3 and +3 -> will work in most cases, not just normal distributions
2) Normalizzation will result in values between 0 and 1 --> recomended when you are scaling a normal distribution

![image](https://user-images.githubusercontent.com/58488172/148275297-31ba02e7-79b4-4780-ac2f-f4965ca1ea85.png)

<b>
When using dummy variables, it is important to sometimes omit one of the dummy variables because it will result in a colinar feature. Direct  opposite of another column

<br>
<br>
<h2>2-Linear Regression:</h2>
In simple linear regression, we are trying to find the minimum sum of squares between observed and predicted variables --> Ordinary Least Squares Model

![image](https://user-images.githubusercontent.com/58488172/148277600-c8df0654-340a-4160-8bba-d9cf15388c13.png)


<br>
<br>
<h2>3-Multiple Linear Regression:</h2>
Linear regression has 5 assumptions that we need to verify before we actually build and deploy a model:<br>
1) Linearity<br>
2) Homoscedasticity<br>
3) Multivariate normality<br>
4) Independence of errors<br>
5) Lack of multicollinearity

<br>
<br>
<h2>Statistically Building Linear Models :</h2>
There are 5 methods we can use to build models: (The term "stepwise regression" refers to options 2,3,4<br>
1) All-in --> All your variables. Should only do if you have prior knowlegde of variable influence or if you have to<br>
2) Backward elimination --> 1.Select significance level to stay in model, fit the full model,consider the predictor with highest p-value. If P value is grater than significant level, remove it. Repeat until all values are under significance level <br>
3) Forward selection <br> 
4) Bidirectional elimination <br>
5) Score comparison <br> 
  


 

