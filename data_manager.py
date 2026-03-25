import json

class DataManager:
    def __init__(self):
        self.file_name = "game_data.json"
       
       # for no change Tuple
        
        self.defaults = ("Player1", 0) 
        
        # use dictionary for key values
        
        self.player_info = {"name": self.defaults[0], "score": self.defaults[1]}

    def load_score(self):
        try:
            file = open(self.file_name, "r")
            self.player_info = json.load(file)
            file.close()
            return self.player_info["score"]
        except:
            return self.defaults[1]

    def save_score(self, current_score):
      
      if current_score > self.player_info["score"]:
            self.player_info["score"] = current_score
            file = open(self.file_name, "w")
            json.dump(self.player_info, file)
            file.close()
            print("High score updated!")