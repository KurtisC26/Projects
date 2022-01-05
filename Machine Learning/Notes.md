Ket notes on the concepts related to machine learning in python



<h2>Preprocessing:</h2>
* When preparing the data, we must only feature scale variables after we wplit the data. The reason is, scaling the data leverages key statistics such as the mean and standard deviation. If we feature scale before splitting, some of the statistics representing the train set will leak into the test set causing potential errors in the accuracy of the predictions


* There are two feature scaling options: Standardization and normalization
1) Standardization will result in values between -3 and +3 -> will work in most cases, not just normal distributions
2) Normalizzation will result in values between 0 and 1 --> recomended when you are scaling a normal distribution
![image](https://user-images.githubusercontent.com/58488172/148275297-31ba02e7-79b4-4780-ac2f-f4965ca1ea85.png)


