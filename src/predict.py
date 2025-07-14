def predict_price(model, latest_data):
    return model.predict([latest_data])[0]