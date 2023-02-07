import requests
from vacancies.models import Vacancy, VacancySettings
import datetime
import random


day = datetime.datetime.now().date()

token = '5920626519:AAGmP8E8z74ApsvuP9RoJGn9Ke6UY62SXZM'
chat_id = "-800474353"

now = datetime.datetime.now()
print(now)

current_time = now.strftime("%H:%M:00")


def send_telegram(message) -> str:
    try:
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" \
                  + chat_id + "&text=" + str(message)
        results = requests.get(url_req)
        return results.json()
    except Exception as ex:
        print(ex)


def send_bot():
    vacancies = Vacancy.objects.filter(enable=True)
    print(vacancies)

    for i in vacancies:
        tt = VacancySettings.objects.filter(vacancy_id=i.id)
        for t in tt:
            message = {"title": i.title, "text": i.text, 'group': t.group.name, 'group_id': t.group.chat_id}
            managers_list = t.manager.all()
            managers_list = list(managers_list)
            if t.last_send_manager and len(managers_list) > 1:
                managers_list.remove(t.last_send_manager)
            random_index = random.randint(0, len(managers_list) - 1)
            manager = managers_list[random_index]
            message["manager_id"] = manager.id
            message['manager'] = manager.client_id
            times = t.random_time.all()
            print(message)

            tt = {'title': 'CKEDITOR',
             'text': '''<p>Всем привет это текст из ckeditora<strong>&nbsp;</strong></p>\r\n\r\n<p><strong>жирный шрифт</strong></p>\r\n\r\n<p><em>с наклоном&nbsp;</em></p>\r\n\r\n<p><em><u>подчеркнутый шрифт</u></em></p>''',
             'group': 'test-group-рассылки', 'group_id': '1001839749636', 'manager_id': 2, 'manager': '6017630571'}
            send_telegram(tt)
            for tt in times:
                if str(tt.time) == current_time:
                    print('Отправленно')
                    send_telegram(message)
                    t.last_send_manager_id = message["manager_id"]
                    t.save()


