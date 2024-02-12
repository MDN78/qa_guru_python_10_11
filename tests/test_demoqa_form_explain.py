from selene import browser, have, be, by
import os
import time
from selene.core import command


# Стили комментариев:
# 1) AAA - Arrange, Act, Assert
# 2) BDD - Given, When, Then

def test_student_registration_form():
    '''
    Разбор занятия. Разобраны селекторы и более качественное оформление кода.
    Подход к выбору селекторов - чтобы они так же помогали понять что ищем и над чем работает строчка
    '''
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).send_keys('Ivan')
    browser.element('#lastName').should(be.blank).send_keys('Ivanov')
    browser.element('#userEmail').should(be.blank).send_keys('Ivanov@test.com')
    # Так когда более понятен - вводим переменную и селекторы помогают понять что ищем
    '''
    male_radio = browser.element('[name=gender][value=Male]')
    male_radio.double_click()
    
    Другой вариант - тк тут есть перекрытие элемента - тогда не нужен двойной клик:  
    male_radio = browser.element('[name=gender][value=Male]+label')
    male_radio.click()
    
    Так записать правильней и короче - мы понимаем что есть кнопка Гендер - там несколько значений
    И среди этих значений выбираем именно Male. Так же разделяя селекторы - при падении и ошибке - проще понять на каком селекторе
    споткнулся код. Но при разбивке селекторов не получится дописать сиблинга только через Xpath
    те кликаем на следующий идущий элемент:
    male_radio = browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::*')
    male_radio.click()
    '''
    # Так же можем кликнуть по иву выше - это проще не надо писать xpath - указать '..' - это значит на элемент выше
    # те найти Родителя. "+" - это найти соседа
    male_radio = browser.all('[name=gender]').element_by(have.value('Male')).element('..')
    male_radio.click()
    browser.element('#userNumber').should(be.blank).send_keys('1234567890')
    # Команда для скролла при маленьком экране с использованием JS
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    # Остановка в DevTools  - заморозка - setTimeout('debugger', 3000)
    browser.all('[type=checkbox]').element_by(have.value('1')).element('..').click()

    # Календарь
    browser.element('#dateOfBirthInput').click()
    # `class~=class_name` это равно .class - говорит что класс содержит такую надпись, а не строго равно
    # через send_keys(или type)- можем отправлять значения в календарь. которые есть в выпадающем списке
    browser.element('.react-datepicker__year-select').send_keys('1980')
    browser.element('.react-datepicker__month-select').send_keys('January')
    # Решение с f строкой
    browser.element(f'.react-datepicker__day--0{10}').click()

    browser.element('#subjectsInput').type('Physics').press_enter()

    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/picture.jpg'))
    # Выбор города и штата = id который начинается с ... [id^=react-select] а внутри его есть..
    # и далее в них ищем по тексту
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    '''
    Если кнопка не видна - Сабмит - то можно использовать тоже команду JS
    browser.element('#submit').perform(command.js.click)
    '''

    browser.element('#submit').submit()
    time .sleep(3)
