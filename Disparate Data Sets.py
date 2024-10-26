import sys
import csv
from collections import defaultdict

def parse_input():
    input = sys.stdin.read().strip().split('\n')
    records = []
    for line in input:
        records.append(next(csv.reader([line], skipinitialspace=True)))
    return records

def organize_events(records):
    parents = {}
    children = defaultdict(list)
    standalone = []
    
    for record in records:
        event_id, title, acronym, project_code, three_digit_code, record_type = record
        if record_type == "Parent Event":
            parents[event_id] = {
                "title": title,
                "acronym": acronym,
                "project_code": project_code,
                "three_digit_code": three_digit_code,
                "children": []
            }
        elif record_type == "IEEE Event":
            if project_code and three_digit_code:
                children[acronym].append({
                    "event_id": event_id,
                    "title": title,
                    "acronym": acronym,
                    "project_code": project_code,
                    "three_digit_code": three_digit_code,
                    "parent_id": None
                })
            else:
                standalone.append(record)
    
    return parents, children, standalone

def apply_exclusion_conditions(parents, children):
    valid_sets = {}
    
    for acronym, child_events in children.items():
        parent_ids = set()
        for child in child_events:
            for parent_id, parent in parents.items():
                if parent["acronym"] == acronym:
                    parent_ids.add(parent_id)
                    child["parent_id"] = parent_id
                    parent["children"].append(child)
        
        if len(parent_ids) == 1:
            parent_id = parent_ids.pop()
            parent = parents[parent_id]
            if parent["children"]:
                valid_sets[parent_id] = parent
    
    return valid_sets

def update_parent_codes(valid_sets):
    for parent_id, parent in valid_sets.items():
        child_codes = set(child["three_digit_code"] for child in parent["children"])
        if len(child_codes) == 1:
            parent["three_digit_code"] = child_codes.pop()
        else:
            parent["three_digit_code"] = "???"

def output_results(valid_sets):
    sorted_parents = sorted(valid_sets.values(), key=lambda x: x["acronym"])
    
    for parent in sorted_parents:
        print(f'{parent["event_id"]},"{parent["title"]}","{parent["acronym"]}",,{parent["three_digit_code"]},"Parent Event"')
        sorted_children = sorted(parent["children"], key=lambda x: (x["title"], x["event_id"]))
        for child in sorted_children:
            print(f'{child["event_id"]},"{child["title"]}","{child["acronym"]}",{child["project_code"]},{child["three_digit_code"]},"IEEE Event",{parent["event_id"]}')

def main():
    records = parse_input()
    parents, children, standalone = organize_events(records)
    valid_sets = apply_exclusion_conditions(parents, children)
    update_parent_codes(valid_sets)
    output_results(valid_sets)

if __name__ == "__main__":
    main()