from flask import Flask,request,jsonify
from flask_cors import CORS
from responses import responses
import joblib
import pandas as pd

app=Flask(__name__)
CORS(app)

model=joblib.load('model/chatbot_model.pkl')
vectorize=joblib.load('model/vectorizer.pkl')

products=pd.read_csv("data/products.csv")

@app.route("/api/chat",methods=["POST"])
def chat():
    data=request.json
    message=data["message"]
    print("User:",message)
    vector_message=vectorize.transform([message])
    pred=model.predict(vector_message)
    intent=pred[0]

    probability=model.predict_proba(vector_message)
    confidence=max(probability[0])

    print("Confidence:",confidence) 

    product_name = None

    for i in products["name"]:
        if i in message.lower():
            product_name = i
            break

    print("Product:", product_name)

    if intent == "product_price":
        if product_name:
            product = products[products["name"].str.lower() == product_name.lower()]

            if not product.empty:
                price = product.iloc[0]["price"]
                response = f"{product_name.capitalize()} costs ₹{price} per unit."
            else:
                response = "Sorry, I couldn't find the product price."
        else:
            response = "Sorry, I couldn't find the product price."

    elif(intent=="greeting"):
        response="Hello! How can I help you?"

    elif(intent=="goodbye"):
        response="Thank you! Have a nice day."

    elif(intent=="product_availability"):
        if(product_name):
            product=products[products["name"].str.lower()==product_name.lower()]

            if not product.empty:
                response=f"Yes we have the {product_name} in our store"
            else:
                response="Sorry I cant find the product"

        else:
            response="This product is not available"

    return jsonify({
        "response": response
    })

if __name__=="__main__":
    app.run(debug=True)