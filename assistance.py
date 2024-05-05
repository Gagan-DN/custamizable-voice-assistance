def voice_assistance(assistance_Name,male_or_female,):
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    import pywhatkit
    import datetime
    import wikipedia
    import pyjokes
    if male_or_female==("male"or"m"):
        male_or_female=0
    elif male_or_female==("female"or"f"):
        male_or_female=1
    else:
        male_or_female=0
    listener=sr.Recognizer()
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[male_or_female].id)
    engine.say('Hey , I am '+assistance_Name)
    engine.say('what can i do for you')
    engine.runAndWait()
    def talk(text):
        engine.say(text)
        engine.runAndWait()
    def take_command():
     try:
         with sr.Microphone() as source:
            print('listening...........')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if assistance_Name in command:
              print(command)
     except:
         pass
     return command
    def run_assistance():
        command = take_command()
        if ('hai'|'hello'|'hey') in command:
            talk('hello, how are you')
        elif 'how are you' in command:
            talk('I am fine, how can I help you')
        elif 'who are you' in command:
            talk('I am drag, your sweetest voice assistant')
        elif 'I like you' in command:
            talk('Do not try to flirt with me , under section 509 of the IPC , flirting is an offence')
        elif 'Are you single' in command:
            talk('No , I am committed with wifi')
        elif 'I love you' in command:
            talk('please do not waste your time, I am already committed with wifi')
        elif 'Do you have feelings' in command:
            talk('offcourse, but not as much as you')
        elif 'crazy' in command:
            talk ('not as much as you')
        elif 'you are beautiful' in command:
            talk('Thank you, But you can not discribe me physicaly but you can discribe my tune')
        elif 'dance' in command:
            talk('sorry I can not dance but I can make you dance and get relax by playing wounderful songs')
        elif 'play' in command:
             song=command.replace('play','')
             talk('playing'+song)
             pywhatkit.playonyt(song)
        elif 'time' in command:
             time=datetime.datetime.now().strftime('%I:%M %p')
             talk('current time is'+time)
        elif 'about' in command:
             information=command.replace('wikipedia','')
             info=wikipedia.summary(information,3)
             talk(info)
        elif 'joke' in command:
             talk(pyjokes.get_joke())
        elif 'child helpline' in command:
             talk('child helpline is 1098')
        else:
            talk('sorry, could you please repeat')
    while True:
        run_assistance()
voice_assistance("alexa","female")