import allure

@allure.id("29120")
@allure.title("Auth via Google(clone)")
@allure.tag("web", "smoke")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
@allure.feature("Auth")
def test_google_auth():
    with allure.step("Открываем главную страницу "):
        pass
    with allure.step("Выбираем способ авторизации через Google"):
        pass
    with allure.step("Авторизуемся как пользователь 'Ms. Random'"):
        with allure.step("Вводим логин 'random-user@gmail.com'"):
            pass
    with allure.step("Вводим пароль 'random-pass'"):
        pass
    with allure.step("Нажимаем кнопку Войти"):
        pass
    with allure.step("Проверяем что авторизовались успешно"):
        pass
    with allure.step("Проверяем что данные профиля обновились из Google "):
        with allure.step("Имя: 'Ms. Random'"):
            pass
    with allure.step("Email: random-user@gmail.com"):
        pass