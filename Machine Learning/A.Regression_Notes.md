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
1) Linearity --> Relationship between variables appears to be linear<br>
2) Homoscedasticity --> Meaning the residuals are equal across the regression line<br>
3) Multivariate normality --> Are each one of the variables normally distributed (goodness of fit or Kolmogorov-Smirnov test)<br>
4) Independence of errors --> occurs when the residuals are not independent from each other.  In other words when the value of y(x+1) is not independent from the value of y(x) <br>
5) Lack of multicollinearity --> Correlation matrix, Tolerance and Variance inflation factor

<br>
<br>
<h2>Statistically Building Linear Models :</h2>
There are 5 methods we can use to build models: (The term "stepwise regression" refers to options 2,3,4<br>
1) All-in <br>
   All your variables. Should only do if you have prior knowlegde of variable influence or if you have to<br><br>
2) Backward elimination <br>
   Select significance level to stay in model. <br>
   Fit the full model,consider the predictor with highest p-value. <br>
   If P value is grater than significant level, remove it. <br>
   Repeat until all values are under significance level <br><br>
3) Forward selection <br> 
   Select significance model to enter the model
   Fit all simple regression models, select the one with the lowest p-value
   Keep the variable and fit all possible models with the one extra predictor added to the ones you already have
   Consider the predictor with the lowest p-value, if P < significance level, got back to step 3 otherwise model is done<br><br>
                                                                     
4) Bidirectional elimination <br>
  Select the significance level to enter and to stay in the model
  Fit all simple regression models, select the one with the lowest p-value based on the significance level to enter
  Once that is complete, similar to the forward selection, Then you do the backwards elimination with the pvalue to stay in the model
  
  
  
5) All possible models (Score comparison) <br>
  Most resource intensive approach -> 2^n-1 models
  Select a criterion of goodness (ex. R2)
  Contruct all possible regression models
  Select the one with the best 
  
  


 

