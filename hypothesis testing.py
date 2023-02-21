import math
# H0: mean trade openness of developed countries <= mean trade openness of developing countries
# H1: mean trade openness of developed countries > mean trade openness of developing countries
developed_countries_mean_tradeopeness = mean_trade_openness_developed['mean trade openness'].mean()
developing_countries_mean_tradeopeness = mean_trade_openness_developing['mean trade openness'].mean()

developed = mean_trade_openness_developed['mean trade openness'].to_numpy()
developing = mean_trade_openness_developing['mean trade openness'].to_numpy()

# drop na values
developed = developed[~np.isnan(developed)]
developing = developing[~np.isnan(developing)]

z_score , p_value = sm.stats.ztest(developed, developing, alternative='larger')
print('z-score: ', z_score)


# z-score:  3.887


# Test the hypothesis that the mean trade openness of developed countries is not equal to that of developing countries using z test (two sample test) at 5 per cent level of significance.

# H0: mean trade openness of developed countries = mean trade openness of developing countries
# H1: mean trade openness of developed countries != mean trade openness of developing countries
 
z_score , p_value = sm.stats.ztest(developed, developing, alternative='two-sided')
print('z-score: ', z_score)

# z-score:  3.887