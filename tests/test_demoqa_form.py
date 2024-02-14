import pytest
from selene import browser, have, be, by
from selene.core import command
import os

# @pytest.mark.skip
def test_demoqa_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).send_keys('Ivan')
    browser.element('#lastName').should(be.blank).send_keys('Ivanov')
    browser.element('#userEmail').should(be.blank).send_keys('Ivanov@test.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').should(be.blank).send_keys('1234567890')
    # browser.element('#dateOfBirthInput').perform(command.js.set_value('10 Jan 1980'))
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').click().element(by.text("1980")).click()
    browser.element('.react-datepicker__month-select').click().element(by.text("January")).click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element("[placeholder='Current Address']").perform(command.js.scroll_into_view)

    browser.element("[class='custom-control custom-checkbox custom-control-inline']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/picture.jpg'))
    browser.element('#currentAddress').send_keys('111999, St Hall avenue 34')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').submit()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(have.exact_texts(
        'Ivan Ivanov',
        'Ivanov@test.com',
        'Male',
        '1234567890',
        '10 January,1980',
        'Physics',
        'Sports',
        'picture.jpg',
        '111999, St Hall avenue 34',
        'NCR Delhi',
    ))
    browser.element('#closeLargeModal').double_click()

