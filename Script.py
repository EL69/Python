# The Boredless Tourist

# Recommendation engine for venues, restaurants, historical sites
# 4. List of destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
# 5. Creating a test traveller & assign to a list
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
# 8. Function to ascertain the location index of the user
def get_destination_index(destination):
# 9. finding the index of destination & saving into a variable
  destination_index = destinations.index(destination)
# 10. Return destination index
  return destination_index
# 11 to 14. Call the function with the destination argument & print
#print(get_destination_index('Paris, France'))
# 15. Function to get traveller location
def get_traveler_location(traveler):
# 16. Access traveler’s destination string and save it into variable
  traveler_destination = traveler[1]
# 17. Get and save  the index of the traveller's destination
  traveler_destination_index = get_destination_index(traveler_destination)
# 18. return traveller_destination_index
  return traveler_destination_index
# 19. 
test_destination_index = get_traveler_location(test_traveler)
# 20.
#print(test_destination_index)
# 25
attractions = [[], [], [], [], []]
# 26
#print(attractions)
# 27
def add_attractions(destination, attraction):
# 28
  destination_index = get_destination_index(destination)
# 31
  attractions_for_destination = attractions[destination_index].append(attraction)
  #32
  return add_attractions
  #33
add_attractions('Los Angeles, USA', ['Venice Beach', ['beach']])
  #34
#print(attractions)
#35
add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#38
def find_attractions(destination, interests):
#39
  destination_index = get_destination_index(destination)
#40
  attractions_in_city = attractions[destination_index]
#41
  attractions_with_interest = []
#42
  for attraction in attractions_in_city:
    possible_attraction = attraction
# 43
    attraction_tags = attraction[1]
# 44
    for interest in interests:
#45 & #49
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
#46
  return attractions_with_interest
#47
la_arts = find_attractions("Los Angeles, USA", ['art'])
#48 & #50
print(la_arts)
#53
def get_attractions_for_traveler(traveler):
#54
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
#55
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
#56 & #57 & #58
  interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places around " + traveler[1] + ': '
#59
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += 'the ' + traveler_attractions[i] + '. '
    else:
      interest += 'the ' + traveler_attractions[i] + ', '
#60
  return interests_string
#61
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
#62
print(smills_france)