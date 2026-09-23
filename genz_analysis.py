import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import ttest_ind

data = pd.read_csv("genz_dataset.csv")


# Deskriptive Statistik

data.info()

data.head()

data["age"].describe()

data["education"].value_counts(normalize=True) * 100

data["gender"].value_counts(normalize=True) * 100


# Vertrauen in Werbung

data["trust_traditional_ads_1to5"].value_counts(
    normalize=True
).sort_index() * 100

data["trust_influencers_1to5"].value_counts(
    normalize=True
).sort_index() * 100

data["trust_influencers_1to5"].describe()

data["trust_traditional_ads_1to5"].describe()


# Durchschnittliches Vertrauen nach Geschlecht

data.groupby("gender")[
    "trust_traditional_ads_1to5"
].mean()

data.groupby("gender")[
    "trust_influencers_1to5"
].mean()


# t-Test: Vertrauen in Influencer nach Geschlecht

male = data.loc[
    data["gender"] == "Male",
    "trust_influencers_1to5"
]

female = data.loc[
    data["gender"] == "Female",
    "trust_influencers_1to5"
]

t_stat, p_value = ttest_ind(
    male,
    female,
    equal_var=False
)

print("t =", t_stat)
print("p =", p_value)


# t-Test: Vertrauen in traditionelle Werbung nach Geschlecht

male = data.loc[
    data["gender"] == "Male",
    "trust_traditional_ads_1to5"
]

female = data.loc[
    data["gender"] == "Female",
    "trust_traditional_ads_1to5"
]

t_stat, p_value = ttest_ind(
    male,
    female,
    equal_var=False
)

print("t =", t_stat)
print("p =", p_value)


# Bevorzugter Shopping-Kanal

data["preferred_shopping_channel"].value_counts(
    normalize=True
) * 100

data.groupby("gender")[
    "preferred_shopping_channel"
].value_counts(
    normalize=True
) * 100


# Bildschirmzeit

data["daily_screen_hours"].describe()


# Zusammenhang Alter und Bildschirmzeit

plt.figure(figsize=(8, 6))

plt.scatter(
    data["age"],
    data["daily_screen_hours"],
    color="blue"
)

plt.xlabel("Alter")
plt.ylabel("Tägliche Bildschirmzeit")
plt.title("Tägliche Bildschirmzeit von GEN Z nach Alter")

plt.show()


# Bildschirmzeit nach Geschlecht

sns.boxplot(
    data=data,
    x="gender",
    y="daily_screen_hours"
)

plt.show()


# Durchschnittliche Bildschirmzeit nach Geschlecht

data.groupby("gender")[
    "daily_screen_hours"
].mean()

data["monthly_discretionary_usd"].describe()
data["annual_income_usd"].describe()
X = data[
    [
        "age",
        "annual_income_usd",
        "daily_screen_hours"
    ]
]

y = data["monthly_discretionary_usd"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())



