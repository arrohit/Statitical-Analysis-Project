# Statitical-Analysis-Project
Statistics Inference project on Diet Dataset


## Project Description:
In the recent years, nutrition and diet have been proven to play an
important role in weight loss for young adults. This has resulted in
controlling the intake of various food constituents and has allowed various
nutritionists to perform detailed analysis to enhance decision making. The
objective of our project is to perform hypothesis testing on various factors
to decide the significance between each factor based on 3 different diet
plans. We derive at our conclusions using the statsmodel api python library.
Solution Design:
Our project is divided into the following sections:
● Data Collection
● Exploratory Analysis
● Multi-way ANOVA
● Model Building (Linear Regression w/ Ordinary Least Squares)
● Conclusions/ Statistical Inferences

## Data Collection:
The publicly available data was collected from the University of Sheffield
website. The data set ‘Diet.sav ’ contains information on 78 people who
undertook one of three diets. There is background information such as age,
gender and height as well as weight lost on the diet (a positive value
means they lost weight). The period during which a person underwent a
diet plan is 6 weeks after which their weight was noted. The weight loss
was calculated by subtracting a person’s weight before and after the diet.
The dataset is non-partitioned and the single data set is used to perform
analysis.
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture1.PNG)
Metadata Description:
Person : Index for each person
Gender : Male=0 Female =1
Age : Age of a person in years
Height : height in cm
Diet : Type of the Diet (1,2,3)
pre.weight : Weight before diet in Kg
weight6weeks: Weight after taking diet in Kg
Weight_loss: pre.weight - weight6weeks in Kg (Dependant Variable)

## Data Summary
The below table gives an overall description of the data giving quantitative
measures like mean,median and quartile ranges
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture2.PNG)

## Box Plot for Distribution of Weight Loss for 3 Diet types:
The below plot shows the range of weight losses for different diet types
Inferences obtained from the boxplot:
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture3.PNG)

1. We can see that the medians of weight loss for diet 1 and 2 are
similar, but there is a significant increase in weight loss for diet 3 and
has a higher range of values.
2. Diet type 1 has 2 outliers (8.5,9)

## Correlation Plot
The Following heatmap shows the correlation between the different
variables and weight loss
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture4.PNG)

We can see that the diet type,weight before/after 6 weeks,gender,height
have the high correlation to weight loss(dependant variable)

## Hypothesis Testing and ANOVA:
3 way anova with Diet type,gender,height as the 3 factors along with
interaction between the factors.
Parameter of Interest :
αi - Effect of each factor under consideration
Null Hypothesis:
Ho : α1 = α2 = α3… = αi
β1= β2= β3... = βj
γ1 =γ2 = γ3…. = γk
Where, αi - Effect of factor diet at level i(1,2,3)
βj - Effect of factor Age at level j(1,2)
γk - Effect of factor Height at level k
Alternate Hypothesis:
H1 : Atleast one α i, βj,γk is unequal
We perform ANOVA using the OLS model we created with Height , Age
and Diet as the predictor variables.
ANOVA Output:
From the ANOVA Table ,
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture5.PNG)

P value (Diet) =0.020865 < 0.05 So we fail to accept null hypothesis
resulting in our conclusion that weight loss is affected by diet

Following Anova we are performing Tukey’s Procedure to identify
significantly different diet type since its the only categorical variable under
consideration
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture6.PNG)

We can see that diet types 1,3 and 1,2 have absolute mean difference
greater than W (critical value) .Hence we can clearly say that diet type 3 is
significantly different from 1 and 2.

## Model Building:
From our exploratory analysis we found out that the most significant
predictors for regression were Diet, Age and Height. We perform an OLS
regression to fit our predicted values using these independent variables.
Intercepts of linear regression:
### Model Output:
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture7.PNG)

## Quantile-Quantile Plot
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture9.PNG)
We can see that the residuals in the qq plot follow linearity thus satisfying
the assumption of normality between predictor variables

## Boxplot of Residuals:
![](file:///C:/Users/arroh/OneDrive/Pictures/Statistics%20project/Capture10.PNG)
The boxplot depicts the range of residuals of each data type. We can
confidently say that the error residual median for diet 3 is positive whereas
for diet 2, median is negative suggesting positive and negative difference
between the fitted weight loss and actual weight loss respectively

## Statistical Inferences Obtained:
From the Above Analysis we have found Following Outcomes
● 3 Way Anova concluded that weight loss (dependant variable) is
related to diet type. (other variables do effect weight loss for this
dataset)
● Tukey’s Procedure shows that diet type 3 is significantly different
from 1 and 2 diet types based on the absolute mean differences.
