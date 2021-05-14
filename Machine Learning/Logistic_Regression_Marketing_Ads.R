"""
Logistic regression model to predict whether or not user will puchase product based on social media add data
By: Kurtis Campbell
Last updated: May 2021
"""

# 1) Set working directory and load dependencies:
setwd("~/Desktop/My Projects GitHib")
library(caTools)
library(ElemStatLearn)


# 2) Loa our data:
data <- read.csv("data/Social_Network_Ads.csv")
data <- data[,2:5]


# 3) Train / Test Split
set.seed(88)
split <- sample.split(data$Purchased, SplitRatio = 0.75)
training <- subset(data,split==TRUE)
test <- subset(data,split==FALSE)

# Feature scalling and factorization
training[,2:3] <- scale(training[,2:3])
test[,2:3] <- scale(test[,2:3])
training$Gender <- ifelse(training$Gender == "Male",1,0)
test$Gender <- ifelse(test$Gender == "Male",1,0)

# 5) Fitting the logistic regression model
classifier <- glm(formula = Purchased ~ .,
                  family = binomial,
                  data = training)

# 6) Predicting the test set results
prob_preb <- predict(classifier,type = 'response',newdata = test[-4])
y_pred <- ifelse(prob_preb > 0.5,1,0)

predictions <- y_pred

# 7) BONUS: showing the results in comparison to the predicted values
test$Predicted_prob <- round(prob_preb*100,2)
test$prediction <- y_pred

# 8) Confusion matrix to evaluate results
cm <- table(test[,4],y_pred)
cm









