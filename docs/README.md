# ios_push_engine
FastApi endpoint for ios push notifications
This API is a simple wrapper around ios myNotifier.
Just register account, install the app and enjoy 15 free push notifications on your registered ios device each month.
For details, see https://medium.com/mynotifier/python-sending-push-notifications-to-your-phone-feaeedcbaac1

## Instalation
1. Clone project onto a local folder
2. Cd to scripts folder
3. Create and activate venv environment
4. Install dependencies from requirements.txt

`pip install -r requirements.txt` 

5. Register your account and device at 

`https://medium.com/mynotifier/python-sending-push-notifications-to-your-phone-feaeedcbaac1`

6. Enter token given by registration into .env PUSH_ENGINE_API_KEY
7. Run host by 
`python __main.py__`

#### API request example
`curl -X 'POST' \
  'http://localhost:5000/v1/ios?message=Hello&description=cool&type=info' \
  -H 'accept: application/json' \
  -d ''` 
