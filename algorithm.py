import random, openai, pandas as pd, requests, secrets, base64, comtypes.client, pdfkit
from pytube import YouTube

# Set your API key
openai.api_key = "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"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message


# while True:
#     # Get the user's input
#     user_input = input("User: ")
#
#     # Generate a response
#     response = generate_response(user_input)
#     print("Bot:", response)

# Set the URL of the YouTube video you want to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = YouTube(url)

# Get the first video stream
stream = yt.streams.first()


# Download the video to the current working directory

class TokenGenerator:
    def __init__(self):
        self.length = 6

    def init(self, length):
        self.length = length

    def generate_otp(self):
        """Generates a one-time password"""
        return secrets.token_hex(self.length // 2)

    @staticmethod
    def mobile_otp():
        return random.randint(10000, 99999)

    @staticmethod
    def email_otp():
        return random.randint(10000, 99999)

    def generate_email_verification_token(self):
        """Generates an email verification token"""
        return base64.urlsafe_b64encode(secrets.token_bytes(self.length)).decode("utf-8")


# Example usage
generator = TokenGenerator()
str_otp = generator.generate_otp()
email_verification_token = generator.generate_email_verification_token()
mobile_otp = generator.mobile_otp()
email_otp = generator.email_otp()
print(
    f"str_otp ; {str_otp}, email_verification_token : {email_verification_token}, mobile_otp : {mobile_otp}, email_otp : {email_otp}")

# Convert the PDF to a Word document
comtypes.client.GetActiveObject("Word.Application").Documents.Open("input.pdf", ReadOnly=1).SaveAs("output.docx",
                                                                                                   FileFormat=16)
# Convert the Word document to a PDF
comtypes.client.GetActiveObject("Word.Application").ActiveDocument.SaveAs("output.pdf", FileFormat=17)

# Convert the HTML file to PDF
pdfkit.from_file("input.html", "output.pdf")

# You can also specify options as a dictionary
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
pdfkit.from_file("input.html", "output.pdf", options=options)

import requests
import json


class WeatherStream:
    def init(self, city, country):
        self.city = city
        self.country = country
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}"

    def get_weather(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data['main']['temp']


# Example usage
weather_stream = WeatherStream("New York", "US")
temp = weather_stream.get_weather()
# print(temp)  # Prints the current temperature in New York

import pandas as pd

# Load the database into a DataFrame
df = pd.read_csv("database.csv")

# Check for missing values
missing = df.isnull().sum()
print(missing)

# Drop rows with missing values
df = df.dropna()

# Check for outliers
statistics = df.describe()
print(statistics)

# Remove outliers
df = df[(df > (statistics['mean'] - 2 * statistics['std'])) & (df < (statistics['mean'] + 2 * statistics['std']))]

# Check for duplicate rows
duplicates = df.duplicated()
print(duplicates)

# Drop duplicate rows
df = df.drop_duplicates()

# Save the cleaned DataFrame to a new file
df.to_csv("cleaned_database.csv", index=False)

#  NEW 

# Load the database into a DataFrame
df = pd.read_csv("database.csv")

# Check for missing values
missing = df.isnull().sum()
print(missing)

# Drop rows with missing values
df = df.dropna()

# Check for outliers
statistics = df.describe()
print(statistics)

# Remove outliers
df = df[(df > (statistics['mean'] - 2 * statistics['std'])) & (df < (statistics['mean'] + 2 * statistics['std']))]

# Check for duplicate rows
duplicates = df.duplicated()
print(duplicates)

# Drop duplicate rows
df = df.drop_duplicates()

# Save the cleaned DataFrame to a new file
df.to_csv("cleaned_database.csv", index=False)


# NEW

class DataFrameAnalyzer:
    def init(self, df):
        self.df = df

    def get_min_max_mean_avg(self):
        result = {}
        result['day'] = {
            'min': self.df.groupby(pd.Grouper(freq='D')).min(),
            'max': self.df.groupby(pd.Grouper(freq='D')).max(),
            'mean': self.df.groupby(pd.Grouper(freq='D')).mean(),
            'avg': self.df.groupby(pd.Grouper(freq='D')).mean()
        }
        result['week'] = {
            'min': self.df.groupby(pd.Grouper(freq='W')).min(),
            'max': self.df.groupby(pd.Grouper(freq='W')).max(),
            'mean': self.df.groupby(pd.Grouper(freq='W')).mean(),
            'avg': self.df.groupby(pd.Grouper(freq='W')).mean()
        }
        result['month'] = {
            'min': self.df.groupby(pd.Grouper(freq='M')).min(),
            'max': self.df.groupby(pd.Grouper(freq='M')).max(),
            'mean': self.df.groupby(pd.Grouper(freq='M')).mean(),
            'avg': self.df.groupby(pd.Grouper(freq='M')).mean()
        }
        result['quarterly'] = {
            'min': self.df.groupby(pd.Grouper(freq='Q')).min(),
            'max': self.df.groupby(pd.Grouper(freq='Q')).max(),
            'mean': self.df.groupby(pd.Grouper(freq='Q')).mean(),
            'avg': self.df.groupby(pd.Grouper(freq='Q')).mean()
        }
        result['half_yearly'] = {
            'min': self.df.groupby(pd.Grouper(freq='6M')).min(),
            'max': self.df.groupby(pd.Grouper(freq='6M')).max(),
            'mean': self.df.groupby(pd.Grouper(freq='6M')).mean(),
            'avg': self.df.groupby(pd.Grouper(freq='6M')).mean()
        }
        return result


# Example usage
df = pd.read_csv("data.csv")
analyzer = DataFrameAnalyzer(df)
result = analyzer.get_min_max_mean_avg()
print(result)


# Todo class to store individual to-do items
class Todo:
    def init(self, task, completed=False):
        self.task = task
        self.completed = completed

    def str(self):
        return self.task

    def complete(self):
        self.completed = True

    def is_completed(self):
        return self.completed


# TodoList class to store and manage a list of to-do items
class TodoList:
    def init(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)

    def get_todos(self):
        return self.todos

    def get_completed_todos(self):
        completed = []
        for todo in self.todos:
            if todo.is_completed():
                completed.append(todo)
        return completed

    def get_incomplete_todos(self):
        incomplete = []
        for todo in self.todos:
            if not todo.is_completed():
                incomplete.append(todo)
        return incomplete


# Example usage
todo_list = TodoList()
todo_list.add_todo(Todo("Buy milk"))
todo_list.add_todo(Todo("Finish homework"))
todo_list.add_todo(Todo("Call mom"))

print("All to-dos:")
for todo in todo_list.get_todos():
    print(todo)

print("\nCompleted to-dos:")
for todo in todo_list.get_completed_todos():
    print(todo)

print("\nIncomplete to-dos:")
for todo in todo_list.get_incomplete_todos():
    print(todo)

todo_list.remove_todo(Todo("Finish homework"))

print("\nAll to-dos after removing one:")
for todo in todo_list.get_todos():
    print(todo)


class Client:
    def __init__(self):
        self.device = None
        self.location = None
        self.ip_address = None

    def init(self, ip_address):
        self.ip_address = ip_address
        self.location = self.get_location()
        self.device = self.get_device()

    def get_location(self):
        """Returns the location of the client based on their IP address"""
        url = f"https://ipapi.co/{self.ip_address}/json/"
        response = requests.get(url)
        data = response.json()
        return data["city"] + ", " + data["region"] + ", " + data["country_name"]

    def get_device(self):
        """Returns the device information of the client based on their IP address"""
        url = f"https://ipapi.co/{self.ip_address}/agent/"
        response = requests.get(url)
        return response.text


# Example usage
client = Client("8.8.8.8")
print(client.ip_address)  # prints 8.8.8.8
print(client.location)  # prints Mountain View, California, United States
print(
    client.device)  # prints something like "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
