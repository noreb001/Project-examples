import os, sys
from flask import Flask, request
from pymessenger import Bot
from utils import wit_response

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAGxzMEDAJEBAH2r10TNZADCkZBlei8vOZA9ywrUul3TBnOAJHl0ojQ4VLTZAuZBfOZB7jRyNIWwAZBmA7cngLWFLJ9Q5QS8jM7P34XgdAO1bjjmI1GTRru11jWiMgyQhcMTkUwYFtNDc7UZAQCwW6eT0gL2b2wZAHGoqdvKfwGZA4wXeWTXj6DArT"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hi":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
  

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # Sender ID
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                # checking for text
                if messaging_event.get('message'):
                    global response
                    response = None
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                        entity, value = wit_response(messaging_text)

                        if entity == 'food':
                            if value == 'vegan':
                                response = "We are indeed vegan friendly and have a dedicated vegan menu section. I'm sending you a link to our vegan menu\n\n" \
                                           "https://www.facebook.com/cafeofcanterbury/photos/a.2873890905982308/2873891102648955/?type=3&theater" \
                                           "\n\n -Eleto Canterbury team"
                            else:
                                response = "We offer a wide range of food and drink. This includes deserts, hot food, hot drinks, alcoholic drinks and soft drinks. Below is a link to our menu: \n\n" \
                                           "https://www.facebook.com/pg/cafeofcanterbury/photos/?tab=album&album_id=2873890905982308\n\n -Eleto Canterbury team"
                        elif entity == "working_hours":
                            response = "We are open from 8:40AM each morning and do last orders at 22:00 - 22:30PM. You are welcome to stay until 23:00, when the cafe closes\n\n -Eleto Canterbury team "
                        elif entity == "dogs":
                            response = "We allow all dogs downstairs as long as they are kept on a lead. \n\n -Eleto Canterbury team "
                        elif entity == "jobs":
                            response = "Hey, its always a good idea to send a copy of your CV to info@eleto.co.uk. Furthermore, always keep an eye on our social media page where we announce when we are hiring \n\n -Eleto Canterbury team "
                        elif entity == "booking":
                            if value == "tickets":
                                response = "Hi there - \n\nFor more information it’s best to message the Folkestone branch on Facebook: https://www.facebook.com/eletofolkestone/" \
                                           " \n\nOr email at info@eleto.co.uk with the heading as Folkestone for more information.\n\n -Eleto Canterbury team "
                            else:
                                response = "Hi there - \n\nBoth the Canterbury and Folkestone cafés " \
                                           "have private rooms that you can hire out"
                                bot.send_text_message(sender_id, response)
                                response = "We can host events such as adult (baby showers, " \
                                           "birthday's," \
                                           "hen parties) and Kids party (birthday).\n\nFurthermore" \
                                           ", we also rent the room out for events for £35 p/h. Roo" \
                                           "m contains a projector and speaker and fits about 15-20 people max.\n\n"
                                bot.send_text_message(sender_id, response)
                                response = "If you would like more information - email " \
                                           "info@eleto.co.uk with which café you're interested in and the Events Manager for the corresponding " \
                                           "café will be in touch.\n\nThank you -\n\n Canterbury Eleto Team "

                        else:
                            response = None

                    bot.send_text_message(sender_id, response)

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug=True, port=80)
