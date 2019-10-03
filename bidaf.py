import os
import slack

from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if data.get('user'): # not from self

        print("predicting", data.get('text'))
        prediction = predictor.predict(
          passage="The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.",
          question=data.get('text')
        )
        print("predicted")
        channel_id = data['channel']
        user = data['user']
        web_client.chat_postMessage(
            channel=channel_id,
            text=prediction["best_span_str"],
        )
      
# oauth & permission -> Bot User OAuth Access Token
print("starting server")
slack_token = os.environ["LOCAL_SLACK_BOT_OAUTH_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
