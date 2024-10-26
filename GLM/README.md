#### **Project Overview**

This project aims to predict **Items Purchased** by e-commerce customers using a **Poisson Regression** model. The goal was to understand how various features such as age, total spend, city, membership type, satisfaction level, and other factors influence the number of items purchased.

---

### **Dataset Description**

The dataset contains the following features:

| Column Name                  | Description                             | Type          |
|------------------------------|-----------------------------------------|---------------|
| Age                          | Age of the customer                     | Integer       |
| Total Spend                   | Total amount spent by the customer      | Numeric       |
| Items Purchased               | Number of items purchased               | Integer (Target)|
| Average Rating                | Average rating of the customer's reviews| Numeric       |
| Discount Applied              | Whether a discount was applied          | Boolean       |
| Days Since Last Purchase      | Days since the last purchase            | Integer       |
| Gender                        | Gender of the customer                  | Categorical   |
| City                          | City where the customer is located      | Categorical   |
| Membership Type               | Customer's membership type              | Categorical   |
| Satisfaction Level            | Satisfaction level of the customer      | Categorical   |

---

### **Steps Followed**

#### **1. Data Preprocessing**
   - **Dropping irrelevant columns**: The `Customer ID` was dropped since it doesn’t provide predictive information.
   - **Encoding categorical variables**: One-hot encoding was used to convert categorical variables like `Gender`, `City`, `Membership Type`, and `Satisfaction Level` into numeric columns.
   - **Binary encoding**: The `Discount Applied` feature was converted into binary (0 or 1).
   - **Handling missing values**: No missing values were present, so no further imputation was necessary.
   
   **Data Example after Preprocessing**:
   | Age | Total Spend | Items Purchased | Average Rating | Discount Applied | Days Since Last Purchase | Gender_Male | City_Houston | ... |
   |-----|-------------|-----------------|----------------|------------------|-------------------------|-------------|--------------|-----|
   | 29  | 1120.20     | 14              | 4.6            | 1                | 25                      | 0           | 0            | ... |

#### **2. Splitting the Data**
   - The dataset was split into **80% training data** and **20% testing data** to evaluate the model’s performance.

#### **3. Model Selection**
   - We used **Poisson Regression**, which is suitable for predicting **count data** like the number of items purchased.
   - The **Generalized Linear Model (GLM)** was implemented using the **statsmodels** library in Python, with Poisson as the family and log as the link function.

#### **4. Model Training**
   The following features were used to predict `Items Purchased`:
   - **Age**
   - **Total Spend**
   - **Average Rating**
   - **Discount Applied**
   - **Days Since Last Purchase**
   - **Gender**
   - **City**
   - **Membership Type**
   - **Satisfaction Level**

   **Poisson Regression Formula**:
    log(E[Items Purchased | Features]) = β0 + β1 * Age + β2 * Total Spend + ... 



   The model was trained using **Iteratively Reweighted Least Squares (IRLS)** to maximize the log-likelihood.

#### **5. Model Evaluation**
   - **Metrics Used**:
     - **Mean Squared Error (MSE)**: \( 0.3587 \)
     - **Root Mean Squared Error (RMSE)**: \( 0.5989 \)
     - **Deviance**: \( 5.11 \) (lower deviance indicates better fit)
   - **Residual Analysis**: Residuals were analyzed, showing a good fit with minimal deviations.

#### **6. Model Results**
   - The table below provides the **coefficients** and their corresponding **p-values**. Positive coefficients indicate an increase in the predicted number of items purchased, while negative coefficients indicate a decrease.
   
   | Feature                          | Coefficient | p-value | Interpretation                             |
   |-----------------------------------|-------------|---------|---------------------------------------------|
   | **Total Spend**                   | 0.0016      | 0.036   | Spending more increases items purchased     |
   | **Discount Applied**              | 0.2389      | 0.154   | Discounts have a positive but not significant effect |
   | **City_Houston**                  | 0.5165      | 0.011   | Houston residents purchase more items       |
   | **Satisfaction Level_Unsatisfied**| 0.3955      | 0.020   | Unsatisfied customers tend to purchase more |
   | **Age**                           | -0.0109     | 0.462   | Age has a very weak negative effect         |
   | **Average Rating**                | -0.0298     | 0.858   | Average rating does not significantly affect purchases |

   The **Total Spend** and living in **Houston** were significant predictors. Interestingly, **unsatisfied customers** were predicted to purchase more items.

---

### **Findings**
   - **Total Spend** had a significant and positive effect on the number of items purchased. For each dollar spent, the expected number of items purchased increases slightly.
   - **City Location** also had a notable impact, with Houston showing a higher number of items purchased than other cities.
   - **Discount Applied** was positive, suggesting that discounts encourage more purchases, though this effect was not statistically significant.
   - **Satisfaction Level** showed an interesting result where **unsatisfied customers** tend to buy more, which might be worth further investigation.
   
   Other features like **Age**, **Average Rating**, and **Membership Type** were not statistically significant, meaning their impact on purchasing behavior is negligible in this model.

---

### **Usage**

1. **Preprocessing**:
   - Ensure all categorical variables are encoded and boolean fields are transformed into numeric values.
   
2. **Model Training**:
   - Use Poisson Regression (`GLM` with Poisson family) to fit the model.
   
3. **Model Evaluation**:
   - Calculate MSE, RMSE, and deviance for model accuracy.
   
4. **Model Deployment**:
   - This model can be integrated into an e-commerce platform to predict the expected number of items a user will purchase based on their interaction data.

---

### **Conclusion**
This project successfully built a **Poisson Regression Model** to predict e-commerce user behavior, identifying key features that influence the number of items purchased.