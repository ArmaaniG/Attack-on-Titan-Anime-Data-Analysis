import requests
import json

def get_data_from_api():
    url = "https://graphql.anilist.co" #AniList graphQL API endpoint

    #start the definition of the query of the GraphQL query
    #ask for data about a media object with the ID 16498(corresponds to attack on titan) and type ANIME
    query = """ 
    query {
       Media (id: 16498, type: ANIME) { 
        id
        title {
            romaji
            english
            native
        }
        description
        startDate {
            year
            month
            day
        }
        episodes
        genres
        averageScore
        characters {
            edges {
                node {
                    name {
                        full
                    }
                }
            }
        }
       } 
    }
    """

    #use the post function from the requests library in Python to send a POST request to the specified URL
    #the data for the post request (the GraphQL query) is passed as JSON in the body of the request
    #POST is a request method supported by HTTP (used when you want to send data to a server to create/update a resource)
    #use request.post() function sends a POST request to the specified URL, store is response variable
    response = requests.post(url, json={'query' : query})

    #if the request is successful, the status code will be 200
    #check if the HTTP status code of the response is 200(In HTTP, 200 status code means the request was successful)
    #return json response text "response.text" contians respose from server in text format
    #parse this text into the Python Dictionary
    if response.status_code == 200:
        print("yay i think that worked")
        return json.loads(response.text)
    else:
        print(f"Query failed. Status code: {response.status_code}.")
        print(f"Message: {response.text}")
        return None

    #run the api request and save the data
    #call the function get_data_from_api() and assign data to data variable

data = get_data_from_api()
print(data)

    #Save data to the JSON file
    #open file called anime_data.json in write mode
    #use the dump function to write JSON data to a file-like object
with open('anime_data.json', 'w') as f:
    json.dump(data, f)