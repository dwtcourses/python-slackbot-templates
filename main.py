import os
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if data.get('user'): # not from self
        channel_id = data['channel']
        user = data['user']
        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi there <@{user}>!",
        )
      
# oauth & permission -> Bot User OAuth Access Token
slack_token = os.environ["LOCAL_SLACK_BOT_OAUTH_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
