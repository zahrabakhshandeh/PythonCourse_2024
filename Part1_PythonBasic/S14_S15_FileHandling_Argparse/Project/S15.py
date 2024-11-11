import argparse
import json
import sys
import datetime
def setup():
    parser = argparse.ArgumentParser(description="weather forecast CLI")
    parser.add_argument("--all", action="store_true", help="Display all data")
    parser.add_argument("--city", type=str, help="Get name of the city")
    parser.add_argument("--forecast",action="store_true", help="forecast 5-days")
    parser.add_argument("--details",action="store_true", help="Display details")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    return parser

def log_command(cmd):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now()
        time_now = time_now.strftime("%Y-%m-%d")
        text = f"{cmd}: {time_now}\n"
        file.write(text)

def show_log(file_name = "commands.log"):
    with open(file_name, "r") as file1:
        data = file1.read()
    print(data)

def load_data(file_name = "weather_data.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def display_all(data):
    for city, value in data.items():
        text = f'{city}: {value["current_condition"]}  {value["condition_percent"]}%'
        print(text)

def display_forecast(city, data):
    data = data[city]['forecast']
    for day in data:
        for k, v in day.items():
            print(f"{k}: {v}")
        print()

def display_details(city, data):
    print(f"Weather details of {city}")
    info = data[city]
    print(f"Currect: {info['current_condition']} {info['condition_percent']}%")
    display_forecast(city, data)


parser = setup()
args = parser.parse_args()
#print(10*"*")
#print(args)
cmd = " ".join(sys.argv)
log_command(cmd)
dict_data = load_data()
if args.all:
    display_all(dict_data) 
elif args.city:
    name = args.city
    if name not in dict_data:
        print(f"{name}: not found!")
    elif args.forecast:
        display_forecast(name, dict_data)
    elif args.details:
        display_details(name, dict_data)
    else:
        print("command not found!")
elif args.show_logs:
    show_log()