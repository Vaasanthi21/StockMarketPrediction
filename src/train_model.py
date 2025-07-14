from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model(df):
    df['Tomorrow'] = df['Close'].shift(-1)
    df = df.dropna()
    X = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = df['Tomorrow']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model