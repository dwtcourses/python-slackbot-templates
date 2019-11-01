# Slackbot Template
Base Slackbot Template

## How To Use
1. Clone this repo

2.
  - Go to https://api.slack.com/apps, and create new app. Then onn the left, click on Bot Users. Add the user

  - Get your `LOCAL_SLACK_BOT_OAUTH_TOKEN` by going to https://api.slack.com/apps, `oauth & permission -> Bot User OAuth Access Token`. Run
```
export LOCAL_SLACK_BOT_OAUTH_TOKEN=<bot user oath access token>
```

3. run with 
```
python3 main.py
```

4. Install your bot via slack and talk to it
