from selene import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_submit_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('enchik')
    browser.element('#lastName').type('enchikov')
    browser.element('#userEmail').type('ivanov@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('88005553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('option[value="6"]').click()
    browser.element('option[value="1992"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').type('English').press_tab()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').type("/home/pimenov/PycharmProjects/demoqa-test/tests/nebo.jpg")
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    browser.element('#currentAddress').type('Novosibirsk')
    browser.element('#state input').type('Rajasthan').press_tab()
    browser.element('#city input').type('Jaiselmer').press_tab()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody').should(have.exact_texts(
        'enchik enchikov',
        'ivanov@gmail.com',
        'Male',
        '88005553535',
        '27 July,1992',
        'English',
        'Music',
        'nebo.jpg',
        'Novosibirsk',
        'Rajasthan Jaiselmer',
    ))
