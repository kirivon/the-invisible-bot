# Using discord.py:alpine build as a parent image
FROM gorialis/discord.py:3.7.1-alpine-rewrite-minimal

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file prior to pip
COPY requirements.txt ./

# Installs any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run bot.py when the container launches
CMD ["python", "main.py"]
