from flask import Flask


app=Flask (__name__)
@app.route("/Api/<text_req>", methods=['GET'])
def Hello(text_req):
    return str("پیام شما دریافت شد :"+Ai_Local_Server(text_req)+"You Little Piece Of Shit")

if __name__== '__main__':
    app.run(port=1)
