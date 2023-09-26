import pandas as pd
from sklearn.model_selection import train_test_split

# Load threat data and security log data
threat_data = pd.read_csv("threat_data.csv")
security_log_data = pd.read_csv("security_log_data.csv")

# Prepare training data
# Label the security log data as normal or malicious
security_log_data["label"] = security_log_data["activity"].apply(lambda x: "malicious" if x in threat_data["indicator"] else "normal")

# Split the training data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(security_log_data.drop("label", axis=1), security_log_data["label"], test_size=0.25, random_state=42)
