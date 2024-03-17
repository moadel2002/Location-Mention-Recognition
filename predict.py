import flair
import json
from flair.data import Sentence
from flair.models import SequenceTagger



def parse_json(path):

  lines = open(path, encoding='utf-8').read().splitlines()
  model = SequenceTagger.load('final-model.pt')

  for line in lines:
      tweet = json.loads(line)

      print("Input")
      print(tweet)

      sentence = Sentence(tweet["text"])
      model.predict(sentence)
      print("Model Prediction")
      print(sentence.to_tagged_string())

      loc_list = []
      for entity in sentence.get_spans('ner'):
        if entity.get_label("ner").value == 'LOC':
          loc_dict = {"text": entity.text,
                      "start_offset": entity.start_position,
                      "end_offset": entity.end_position
                      }
          loc_list.append(loc_dict)                                  

      d = {
          "tweet_id": tweet["tweet_id"],
          "location_mentions": loc_list
          }        

      print("Output")
      print(d)

      j = json.dumps(d)
      with open('output.jsonl', 'a') as f:
        f.write(j)
        f.write('\n')

parse_json("input.jsonl")