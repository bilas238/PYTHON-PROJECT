import json

class DataManager:
    def __init__(self):
     
     #file name where score save
       
       self.file_name = "score_data.json"
        
     #dictionary for player data
        
        self.player_info = {"name": "Player1", "high_score": 0}

      def load_score(self):
        try:
         
         #file open 
           
           file = open(self.file_name, "r")
            self.player_info = json.load(file)
            file.close()
            return self.player_info["high_score"]
        
        except:
      
      #file doesn't exist, return 0
            
            return 0

    def save_score(self, current_score):
      
      # when new score is better, update the dictionary
      
      if current_score > self.player_info["high_score"]:
            
            self.player_info["high_score"] = current_score
            
            # save dictionary in json file
            
            file = open(self.file_name, "w")
            json.dump(self.player_info, file)
            file.close()
            print("New High Score Saved!")