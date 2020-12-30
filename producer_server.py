from kafka import KafkaProducer
import json
import time

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            json_data = json.load(f)
            for line in json_data:
                message = self.dict_to_binary(line)
                # TODO send the correct data
                self.send(self.topic, message)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        json_dict['crime_id'] = int(json_dict['crime_id'])
        json_dict['agency_id'] = int(json_dict['agency_id'])
        print("sending: %s", json.dumps(json_dict, indent=4, sort_keys=True))
        return json.dumps(json_dict).encode() 
