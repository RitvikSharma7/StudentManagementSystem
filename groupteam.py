class GroupTeam:
    
    sep = " TEAM "
    
    def __init__(self, team, group_size):
        self.team = team
        self.group_size = group_size
        self.groups = self.group()  # Call group() on initialization
        
    def group(self):
        total_team_size = len(self.team)
        whole_team_size = total_team_size // self.group_size
        rem_team_size = total_team_size % self.group_size
        
        whole_list = [tuple(self.team[i * self.group_size : (i + 1) * self.group_size]) for i in range(whole_team_size)]
    
        if rem_team_size != 0:
            whole_list.append(tuple(self.team[whole_team_size * self.group_size:]))
        
        return whole_list
        
    def __str__(self):
        result = ""
        for i, group in enumerate(self.groups):
            result += f"{'-'*7}{self.sep}{'-'*7}\n"
            for member in group:
                result += f" Member: {member}\n"
            result += "-"*7 + "-"*len(self.sep) + "-"*7 + "\n"
        return result
            
            
if __name__ == "__main__":
    pass

        