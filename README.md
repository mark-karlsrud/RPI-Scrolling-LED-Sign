# RPI-Scrolling-LED-Sign
Display weather, tweets, news headlines, weather, and more on a scrolling LED sign hooked up to a Raspberry Pi

Setup

1. Install pip

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py`

2. Install Python packages

`sudo pip install requests`

Modules

1. New York Subway MTA API

`sudo pip install --upgrade gtfs-realtime-bindings
sudo pip install protobuf3_to_dict
sudo pip install -U python-dotenv`


To configure this, you'll need to add the files "MTA_API_KEY.env" to the nyc-mta-arrival directory with the contents "API_KEY=<your api key>". Obtain your API key at https://datamine.mta.info/user/register.
Next, configure the MTA.env file with the appropriate train information that you want displayed.

2. Weather

3. Twitter

4. News