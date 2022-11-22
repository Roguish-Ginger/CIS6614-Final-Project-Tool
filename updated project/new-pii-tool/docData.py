import pandas as pd
import re
import numpy as np
import ijson
import csv

class docData:
    df = None
    percent_critical = 0
    percent_high = 0
    percent_medium = 0
    percent_low = 0
    total = 0
    
    def __init__(self):
        pass
    
    def search_dicts(self, key, list_of_dicts):
       for item in list_of_dicts:
          if key in item.keys():
            return item
    
    def run(self, rules_dict, scores, filename):
        report_data = []
        per_column = []
        report_data = [['Rule matched', 'Field', 'Value', 'Mean', 'Max', 'Min', '%Critical', '%High', '%Medium', '%Low', 'Rule matched', 'Field', 'Score', 'Level', 'Variance']]
        overall = []
        running_scores = []

        min_rule = 1.0
        max_rule = 0
        critical = 1.0
        high = 0.8
        medium = 0.4
        low = 0.3
        level = 'UNDETERMINED'
    
    def get_level(self, level, low, medium, high, critical, score, matched_vals):
        if score == critical:
            level = 'CRITICAL'
            self.percent_critical += (matched_vals)

        if score >= high and score < critical:
            level = 'HIGH'
            self.percent_high += (matched_vals)

        if score >= medium and score < high:
            level = 'MEDIUM'
            self.percent_medium += (matched_vals)
                        
        if score <= low:
            level = 'LOW'
            self.percent_low += (matched_vals)

        return level
        
    def add_variances(self, overall_mean, vals, per_column):
        variances = []
        temp_vals = vals
        i = 0
        for val in temp_vals:
            val = (val - overall_mean)**2
        for val in temp_vals:
            variances.append(round(val/len(vals), 3))
        for l in per_column:
            l.append(variances[i])
            i += 1
        return per_column

    def run(self, rules_dict, scores, filename):
        report_data = []
        per_column = []
        report_data = [['Rule matched', 'Field', 'Value', 'Mean', 'Max', 'Min', '%Critical', '%High', '%Medium', '%Low', 'Rule matched', 'Field', 'Score', 'Level', 'Variance']]
        overall = []
        running_scores = []

        min_rule = 1.0
        max_rule = 0
        critical = 1.0
        high = 0.8
        medium = 0.4
        low = 0.3
        level = 'UNDETERMINED'

        ## rule based approach
        for rule in rules_dict:
            field = ""
            matched_vals = 0
            
            a = open(filename, 'r')
            for line in a:
                for word in line.split():
                    if re.search(rule, line, re.IGNORECASE):
                        if rules_dict.get(rule) != '':
                            r = re.compile(rules_dict.get(rule))
                            print(word)
                            if r.match(word):
                                matched_vals += 1
                                #string = "Location: %s, Value: %s" % (prefix, value)
                                report_data.append([rule, line, word, "", "", "", "", "", "", ""])
                                field = line
                                matched_rule = rule

        self.write_report(report_data)    


    def write_report(self, report_data):
        writefile = open('report.csv', 'w+')
        writer = csv.writer(writefile)
        writer.writerows(report_data)
    
    
