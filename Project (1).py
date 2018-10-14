# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 15:48:44 2018

@author: Rohit Appandaraju
"""
# Packages for modelling and Statistical Analysis

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import statsmodels.api as sm
import seaborn as sns
import scipy.stats as sc

# Reading the Dataset
df = pd.read_csv("C:/Users/arroh/Downloads/stcp-Rdataset-Diet.csv")

#calculating weight loss
df["Weight_Loss"] =df["pre.weight"]-df["weight6weeks"]

# Finding Correlation between each variable
correlation = df.corr()

#heatmap
sns.heatmap(correlation,annot = True)

#The heatmap shows the correlation between the different variables and weight loss.
#We see that the diet type,weight before/after 6 weeks,gender,height have the highest correlation to weoght loss

sns.boxplot(df["Diet"],df["Weight_Loss"])

#The boxplot shows the range of weight loss for different diet types.
# We can see that the medians of weight loss for diet 1 and 2 are similar,
# but there is a significant increase in weight loss for diet 3 and has a higher range of values.
#diet 1 has 2 outliers

df.describe()
#Descriptive Statistics to give the summary of the data and its distribution

# 3 way anova with Diet type,gender,height as the 3 factors

model = ols("Weight_Loss ~ Diet*gender*Height", df).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)

#Residuals

fitted_values = model.predict()
residuals = df["Weight_Loss"]-fitted_values
sm.qqplot(residuals,line='45',fit =True)
sns.boxplot(df["Diet"],residuals)

#Model Summary
df1=df.drop(['Person','pre.weight','weight6weeks'],axis=1)
model1 = sm.OLS(df1["Weight_Loss"],df1.iloc[:,1:4])
result = model1.fit()
result.summary()

sc.linregress(df1["Diet"],df1["Weight_Loss"])

#Tukeys Method for Comparison of means between different diet types

tukey = pairwise_tukeyhsd(endog=df1["Weight_Loss"],     # Data
                          groups=df1["Diet"],   # Groups
                          alpha=0.05)
print(tukey)
#we see 3 is significantly different from others