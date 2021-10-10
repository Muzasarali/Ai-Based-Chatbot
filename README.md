# AI Based Chatbot

This chat bot is developed using Rasa open source Framework.

## Rasa Framework Installation

### Requirements

1. Anaconda
2. Python
3. Rasa

### Installation steps

Follow the steps to install rasa framework correctly.

- Download and install [Anaconda](https://www.anaconda.com/products/individual)
- Download and install [Microsoft Visual C++ Redistributable](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-160)
- create Conda environment
  with Navigator or Command Prompt

```
conda create --name rasabot python==3.8
```

- Activate conda environment in Command Prompt

```
conda activate rasabot
```

- install Tensorflow using "Conda"

```
conda install tensorflow
```

- install Rasa using "PIP"

```
pip install rasa
```

## Rasa Basic Commands

- Initialze basic Rasa bot

```
rasa init
```

- Train Rasa bot

```
rasa train
```

- Run Rasa bot on command prompt

```
rasa shell
```

- Run Rasa bot on command prompt with backend / python program
  (open another command prompt and run following command)

```
rasa run actions
```

- Enabel API endpoints

```
rasa run -m models --enable-api --cors "*" --debug
```

### How to use this repository

1. Install All Requirements
2. Clone or Download Project
3. Create MongoDB Database with (TravelBot) name and add (Hotel & Places) Collection.
4. Change Database.py if Mongodb client url is different
5. Train Model

```
rasa train
```

6. Run Chatbot in command Prompt [1]

```
rasa shell
```

7. Run Chatbot actions in command Prompt [2]

```
rasa run actions
```

### References

- Installation [Guide](https://youtu.be/4ewIABo0OkU)

- Rasa [Youtube](https://www.youtube.com/channel/UCJ0V6493mLvqdiVwOKWBODQ) Channel

- [Innovate Yourself](https://youtube.com/playlist?list=PLtFHvora00y80hvsNJ-6YkmfTMrxk5rOe)
