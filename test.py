# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib
from responses import responses

# df=pd.read_csv('data/intent.csv')
# x=df["text"]
# y=df["intent"]

# vectorizer=TfidfVectorizer()
# vector_x=vectorizer.fit_transform(x)

# model=LogisticRegression()
# model.fit(vector_x,y)

products=pd.read_csv("data/products.csv")

model=joblib.load("model/chatbot_model.pkl")
vectorize=joblib.load("model/vectorizer.pkl")

cart=[]

#intent
message=input("You: ")
vector_message=vectorize.transform([message])
pred=model.predict(vector_message)
intent=pred[0]

product_name=None
for i in products["name"]:
    if(i in message.lower()):
        product_name=i
        break

if(intent=="product_price"):
    product=products[products["name"].str.lower()==product_name.lower()]
    if not product.empty:
        price=product.iloc[0]["price"]
        print(f"Bot: {product_name} costs rupees {price} per unit")
    else:   
        print("Bot: Sorry, I couldn't find the product price.")

if(intent=="greeting"):
    print("Bot: ",responses[intent])

if(intent=="goodbye"):
    print("Bot: ",responses[intent])

if(intent=="product_search"):
    if(product_name):
        product=products[products["name"].str.lower()==product_name.lower()]

        if not product.empty:
            print(f"Bot: Yes we have the {product_name} in our store")
        else:
            print("Bot: Sorry I cant find the product")

    else:
        print("This product is not available")

# if(intent=="view_cart"):
#     if len(cart)==0:
#         print("Bot: Your cart is empty.")
#     else:
#         print("Bot: Your cart contains:")
#         for item in cart:
#             print("-", item)

# found=False
# if(intent=="remove_item"):
#     if(product_name):
#         for i in cart:
#             if(i.lower()==product_name):
#                 cart.remove(i)
#                 found=True
#                 print(f"Bot: The {product_name} is removed from your cart")
#         if not found:
#             print(f"Bot: The product is not in your cart")

#     else:
#         print("Bot: Which product would you like to remove?")

#confidence
prob=model.predict_proba(vector_message)
confidence=max(prob[0])

print("Intent: ",intent)
print("Confidence: ",confidence)

# print("Bot: ",responses[intent])
print("Produc: ",product_name)