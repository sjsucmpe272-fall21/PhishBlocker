# Team-Project-17

## Project Proposals

### Project 1
#### Mobile App - Music Genre Identificaiton

1. Introduction to the problem statement

    Have you ever visited a coffee shop and actually liked their taste in music? Maybe you enjoyed the music tempo, the vocals, or the lyrics. Whatever it was, you wanted to know what kind of music is being played (the genre). With the modern advancement in machine learning (and technology in general) it is possible to make computers listen to and identify sounds. So, can we build and deploy and ML model that can classify music into different genres?

2. Abstract (rough draft)

    In this project, we want to build and deploy a machine learning model that can classify a 30-second song recording into multiple categories (genres)
    The user can open the app and press a button to record a playing song for a pre-determined time. The model would then classify the recorded sound and notify the user of the genre of the song playing.


3. Approach
      1. Build and train a Deep Learning model to classify sound clips (wav format) into different genres.
      2. Build the app (front-end) that can record sounds.
      3. Build the back-end that 
          1. supports recieving sound recordings from the front end for model analysis.
          2. supports sending results of model analysis to the front end.
          3. supports caching requests. if a song that was previously processed is requested again, we can just send the results without having to re-process it.
    
4. Persona

    User with phone that wants to identify the genre of a currently-playing song.

5. Dataset links

    https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification

