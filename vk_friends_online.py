import os
import vk
import getpass

APP_ID = os.environ.get('VFO_APP_ID')


def get_user_login():
    return input('Enter user login / e-mail / phone number > ')


def get_user_password():
    return getpass.getpass(prompt='Password: (will not be echoed) > ', stream=None)


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    """
    Неоптимальное использование внешнего АПИ.
    Запросы ко внешним сервисам - это самая медленная часть программы.
    Она во многие тысячи раз медленнее остального кода на Python
    из-за сетевых задержек и межпроцессного взаимодействия.
    Внешних запросов должно быть минимальное количество.
    (попробуй вытаскивать не всех друзей и потом фильтровать,
    а сразу вытаскивать только тех, кто онлайн)

    замечательно, был один вызов апи, теперь их будет два (вопрос зачем?)
    """
    return api.users.get(user_ids=friends_ids)


def output_friends_to_console(friends_online):
    if len(friends_online) != 0:
        print('Friends online: ')
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])
        print('Total friends online: ', len(friends_online))
    else:
        print('No friends online')

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
