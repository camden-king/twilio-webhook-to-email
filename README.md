This is a simple python flask app that uses twilio to recieve text messages and then sends them in an email via sendgrid to the desired email address. This email address is hardcoded in. This is done for simplicity as it does not require the use of any databases. It was designed as a quick fix for my dad (limited mobility) who used to use siri to email himself so that he can copy and paste it to where he needs. Siri recently stopped supporting emailing and until I am with him to set up something else this will hopefully work. Any feedback or improvements are welcome.

To run:
python3 application.py
And set up your twilio webhook to send to url/sms