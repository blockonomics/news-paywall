# Blockonomics Payment Widget Demo using Django.

This demo uses the Payment Widget provided by Blockonomics to receive Bitcoin payments. It can be easily integrated with your online store. The video tutorial for this demo can be found [here](//link).

## Installing Guide

<details>
<summary> Installing dependencies </summary>

* Create a virtual environment using python3.9 `python3.9 -m venv env`
* Activate the virtual environment `source env/bin/activate`
* Install the requirements `pip install -r requirements.txt`

</details>

<details>
<summary> Setting up API Configurations </summary>

* Place your Blockonomics API Key in the `API_KEY` field in the settings.py of NewsPayWall folder, found [here](https://github.com/SyedAnas26/news-paywall/blob/5857c3ea7069e3410d0c021312f525d26955eab2/NewsPayWall/settings.py#L29)

</details>

<details>
<summary> Migration Code </summary>

* `python manage.py migrate`

</details>

<details>
<summary> Blockonomics Website Setup </summary>

* Create your [Blockonomics payment widget](https://www.blockonomics.co/merchants#/buttons?products). Get the UUID of the product and paste in the premium_news.html page, found [here](https://github.com/SyedAnas26/news-paywall/blob/5857c3ea7069e3410d0c021312f525d26955eab2/templates/dashboard/premium_news.html#L69). 
* Go to `OPTIONS` in the PAYMENT BUTTONS/URL tab on [merchants page](https://www.blockonomics.co/merchants). You need to setup the `ORDER HOOK URL` and `Redirection URL`.
* To test the code locally, follow instructions from [this](https://www.youtube.com/watch?v=6Ydk32avIgo) video and make sure to place the `<domain>/payment-webhook` as your order hook url and `<domain>/dashboard` as redirection url. Here `<domain>` is the domain you get from reverse proxy (Ngrok/localtunnel).
* Make sure to save your changes!

</details>

<details>
<summary> The Last Line! </summary>

* `python manage.py runserver`

<p> Now you are all set to locally run the demo! </p>

</details>
