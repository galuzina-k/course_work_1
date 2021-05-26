import pyttsx3
import speech_recognition as sr
import sys
import time
import webbrowser
from random import randint

from IOMH import *

# Form, Window = uic.loadUiType("IOMH.ui")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
form = Ui_MainWindow()
form.setupUi(MainWindow)
MainWindow.show()
browser_text = "Маша: Вас приветсвует МАША v1.0 " \
               "Пока я разбираюсь только в стажировках, так что если Вам интересна эта тема, скажите 'Стажировки'\n"
clear = ""
stflag = 0
flag = 0
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


def talk(words):
    engine.say(words)
    engine.runAndWait()


def upd_browser_text_bot(answer):
    new = (browser_text + "Маша: " + answer + "\n")
    return new


def bot_output(ans):
    global browser_text
    browser_text = upd_browser_text_bot(ans)
    form.textBrowser.setText(browser_text)
    talk(ans)


def bot(response):
    global stflag
    flagans = False
    if ("привет" in response):
        bot_output("Привет, друг")
        flagans = True
    if (response == "стажировки") & (stflag == 1) & ("привет" not in response):
        bot_output("Подбор стажировок уже включен\nЧем могу помочь?")
        flagans = True
    if (response == "стажировки") & (stflag == 0) & ("привет" not in response):
        stflag = 1
        bot_output("Включаю подбор стажировок")
        time.sleep(0.5)
        bot_output(
            "Я могу рассказать Вам о стажировках в Яндексе, Лаборатории Касперского, Райффайзен банке, Банке ВТБ и Самсунге\nЧто конкретно Вас интересует?")
        flagans = True
    if ("яндекс" in response) & ("сбер" not in response) & (stflag == 1) & ("привет" not in response):
        bot_output("Это сайт стажировки Young and Yandex")
        url = "https://yandex.ru/yaintern/"
        webbrowser.open_new_tab(url)
        bot_output("В этом году предлагается принять участие в четырёх направлениях стажировки")
        bot_output("Машинное обучение")
        bot_output("Разработка интерфейса")
        bot_output("Бэкэнд разработка")
        bot_output("Разработка мобильных приложений")
        bot_output("Аналитика")
        bot_output("Функционаьное тестирование")
        bot_output("Информационная безопасность")
        # url = "https://yandex.ru/yaintern/int_01"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/yaintern/int_04"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/yaintern/int_03"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/yaintern/int_05"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/yaintern/int_02"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/jobs/vacancies/interns/intern_test_poisk/"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        # url = "https://yandex.ru/jobs/vacancies/interns/service_security_trainee/"
        # webbrowser.open_new_tab(url)
        # time.sleep(4)
        flagans = True
    if ("сбер" in response) & (stflag == 1) & ("привет" not in response):
        bot_output(
            " Sberseasons это оплачиваемая стажировка для студентов таких направлений как IT, экономика, финансы, право"
            "На их сайте представлены следующие направления")
        url = "https://sbergraduate.ru/sberseasons-moscow/"
        webbrowser.open_new_tab(url)
        bot_output("На главной странице вы можете подать заявление на любое из направлений")
        time.sleep(1)
        bot_output(
            "Также я покажу ссылку на сайт, на котором собраны многие из необходимых для успешной подготовки материалов")
        url = "https://sbergraduate.ru/articles/"
        webbrowser.open_new_tab(url)
        flagans = True
    if ("касперск" in response) & (stflag == 1) & ("привет" not in response):
        bot_output("Лаборатория Касперского предлагает оплачиваемую стажировку для студентов IT направлений")
        url = "https://safeboard.kaspersky.ru"
        webbrowser.open_new_tab(url)
        time.sleep(1)
        bot_output("Я нашла интересный раздел, в котором собраны статьи о стажировке и о том, как подготовиться к ней")
        url = "https://safeboard.kaspersky.ru/special-projects/"
        webbrowser.open_new_tab(url)
        flagans = True
    if ("райффайз" in response) & (stflag == 1) & ("привет" not in response):
        bot_output(
            "Райффайзен банк приглашает студентов экономической, финансовой, IT и правовой напрвленностей на стажировку на следующие вакансии")
        url = "https://raiffeisen-evolve.ru/#!/tab/242335165-6"
        webbrowser.open_new_tab(url)
    if ("втб" in response) & (stflag == 1) & ("привет" not in response):
        bot_output(
            "ВТБ предлагает шестимесячную стажировку для студентов IT, экономического и правового направлений")
        bot_output("Заполнить заявку вы можете на данной странице")
        url = "https://www.vtbcareer.com/internship/it-yunior/"
        webbrowser.open_new_tab(url)
        flagans = True
    if ("samsung" in response) & (stflag == 1) & ("привет" not in response):
        bot_output(
            "Samsung Research Russia предлагает стажировку студентам аналитического, физического и IT направлений")
        url = "https://www.samsung.com/ru/aboutsamsung/careers/srr/internship/"
        webbrowser.open_new_tab(url)
        time.sleep(1)
        bot_output("Вот основные направления")
        bot_output("Искусственный интеллект")
        bot_output("Медиа")
        bot_output("Разработка алгоритмов")
        bot_output("Внутренние системы")
        bot_output("Оптика")
        bot_output("Бизнес")
        url = "https://www.samsung.com/ru/aboutsamsung/careers/srr/internship/#media"
        webbrowser.open_new_tab(url)
        time.sleep(1)
        bot_output("Заполнить резюме вы можете на следующей странице")
        url = "https://www.samsung.com/ru/aboutsamsung/careers/srr/internship/#resume"
        webbrowser.open_new_tab(url)
        flagans = True
    if ("сайт" in response) & ("проект" in response) & ("привет" not in response):
        bot_output("Перенаправляю Вас на сайт проекта")
        url = "http://mashadevs.fun/"
        webbrowser.open_new_tab(url)
        flagans = True
    if not flagans:
        phrase1 = "Хм, сейчас попробую найти"
        phrase2 = "Уже ищу"
        phrase3 = "Обратимся за помощью к Яндексу"
        phrase4 = "Я на такое не подписывалась, но сейчас что-нибудь придумаю"
        phrase5 = "Сейчас найдем что-нибудь хорошее"
        rand = randint(1, 5)
        if rand == 1:
            bot_output(phrase1)
        if rand == 2:
            bot_output(phrase2)
        if rand == 3:
            bot_output(phrase3)
        if rand == 4:
            bot_output(phrase4)
        if rand == 5:
            bot_output(phrase5)
        url = "https://yandex.ru/search/?lr=213&text=" + response
        time.sleep(0.5)
        webbrowser.open_new_tab(url)


def get_text():
    return (form.textEdit.toPlainText())


def upd_browser_text():
    new = (browser_text + "Вы: " + get_text() + "\n")
    return new


def main():
    global browser_text
    browser_text = upd_browser_text()
    form.textBrowser.setText(browser_text)
    bot(get_text().lower())
    form.textEdit.setText(clear)


def Rec():
    recognizer = sr.Recognizer()
    message = ""
    global flag
    flag = 1
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        try:
            audio = recognizer.listen(mic)
        except sr.WaitTimeoutError:
            bot_output("Произошла ошибка записи, проверьте микрофон")
        try:
            message = recognizer.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            bot_output("Извините, я Вас не поняла")
    flag = 0
    return message


def upd_browser_text_audio(input):
    new = (browser_text + "Вы: " + input + "\n")
    return new


def listen():
    global browser_text
    input = Rec()
    if (input != ""):
        browser_text = upd_browser_text_audio(input)
        form.textBrowser.setText(browser_text)
        bot(input.lower())


def PushToTalk():
    listen()


def AboutDevs():
    url = "http://mashadevs.fun/"
    webbrowser.open_new_tab(url)


def Manual():
    url = "http://mashadevs.fun/manual"
    webbrowser.open_new_tab(url)


def CommandList():
    url = "http://mashadevs.fun/commands"
    webbrowser.open_new_tab(url)


form.textBrowser.setText(browser_text)
form.pushButton.clicked.connect(main)
form.action_5.triggered.connect(AboutDevs)
form.action_9.triggered.connect(CommandList)
form.action_10.triggered.connect(Manual)
form.pushButton_2.clicked.connect(PushToTalk)
app.exec()
