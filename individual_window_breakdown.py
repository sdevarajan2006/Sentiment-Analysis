'''
Individual window breakdown
'''
'''
API Key
'''
import requests
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	'''
	Query function which runs the sentiment analysis
	'''
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def individual_window_breakdown(text):
	'''
	This function takes a list of sentences, and returns the positive and negative sentiment
	for each sentence in the form of a list of dictionaries
	'''
	list_of_sentences_and_sentiments = []
	for i in text:
		output = query({"inputs" : i,
		  })
		if output[0][0]['label'] == 'POSITIVE':
			this_window = {
				"SENTENCES" : i,
				"POSITIVE" : output[0][0]['score'],
				"NEGATIVE" : output[0][1]['score']
            }
		else:
			this_window = {
				"SENTENCES" : i,
				"POSITIVE" : output[0][1]['score'],
				"NEGATIVE" : output[0][0]['score']
            }
		list_of_sentences_and_sentiments.append(this_window)
	return(list_of_sentences_and_sentiments)

if __name__ == '__main__':
	list_sample = ['Snakes are elongated, legless reptiles belonging to the suborder Serpentes. They are found in diverse habitats around the world, ranging from deserts to rainforests. Snakes have a flexible body and can move quickly, enabling them to catch prey and escape from predators.', ' They have a unique adaptation for killing prey - their jaws are hinged and can be opened wide, allowing them to swallow prey much larger than their head. Some species of snakes are venomous and their bite can be dangerous to humans, but many are harmless. Snakes play important roles in the ecosystems in which they live, serving as both predator and prey.', ' yqsssss']
	ans = individual_window_breakdown(list_sample)
	print(ans)
	