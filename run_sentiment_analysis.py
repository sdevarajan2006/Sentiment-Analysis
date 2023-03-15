'''
Run sentiment analysis
'''
import requests

'''
API Key
'''
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	'''
	Query function which runs the sentiment analysis
	'''
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def run_sentiment_analysis(text):
	'''
	This function runs a sentiment analysis on a list of groups of sentences, and returns the 
	average positive and negative sentiment
	'''
	number_of_sections = len(text)
	positive_counter = 0
	negative_counter = 0
	for i in text:
		output = query({"inputs" : i,
		  })
		if output[0][0]['label'] == 'POSITIVE':
			positive_counter += output[0][0]['score']
			negative_counter += output[0][1]['score']
		else:
			positive_counter += output[0][1]['score']
			negative_counter += output[0][0]['score']
	average_positive_score = positive_counter/number_of_sections
	average_negative_score = negative_counter/number_of_sections
	return("POSITIVE: " + str(average_positive_score) + "\n" + "NEGATIVE: " + str(average_negative_score))
	
	
if __name__ == '__main__':
	list_sample = ['Snakes are elongated, legless reptiles belonging to the suborder Serpentes. They are found in diverse habitats around the world, ranging from deserts to rainforests. Snakes have a flexible body and can move quickly, enabling them to catch prey and escape from predators.', ' They have a unique adaptation for killing prey - their jaws are hinged and can be opened wide, allowing them to swallow prey much larger than their head. Some species of snakes are venomous and their bite can be dangerous to humans, but many are harmless. Snakes play important roles in the ecosystems in which they live, serving as both predator and prey.', ' yqsssss']
	ans = run_sentiment_analysis(list_sample)
	print(ans)