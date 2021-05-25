import pyowm
owm = pyowm.OWM('6dfd5610a3de02c4bc9727cdb60996fd') # generated API key | name: gforce

mgr = owm.weather_manager() #initialized weather manager object
place = input("Enter name of a city: ")
obs = mgr.weather_at_place(place)
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']
cloud_cov=weather.clouds
winds=weather.wind()['speed']
print (f'The temperature of {place} is {temperature} celsius')
print(f'The current cloud coverage for {place} is {cloud_cov}%')
print(f'The current wind speed for {place} is {winds}mph')



mgr = owm.weather_manager() #initialized weather manager object
place = int(input("Enter name of a city PinCode: "))

obs = mgr.weather_at_zip_code(str(place),"in")
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']
print (f'The temperature of {place} is {temperature} celsius')



