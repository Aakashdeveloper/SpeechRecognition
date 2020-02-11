import speech_recognition as sr
import webbrowser as wb 

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[Search on edureka: search on youtube')
    print('Speak Now')
    audio = r3.listen(source)


if 'edureka' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('Search Your Query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            #Open web broswer with user search
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('err')
        except sr.RequestError as e:
            print('Faild'.format(e))


