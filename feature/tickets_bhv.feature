Feature: Checking registration
Scenario: Checking registration already registred user
	Given website "https://dev.ticketscloud.org" and click "Зарегистрироваться"
	Then whrite in field name and assert button disabled
	Then whrite in field mobile and assert button disabled
	Then whrite in field email invalid value and assert warning
	Then whrite in field email valid value and assert button disabled
	Then write in feald password invalid value and assert warning
	Then whrite in field valid password
	Then select "Я - Организатор"
	Then push button and wait to get page source
	Then page include text "Пользователь abc_cba07@mail.ru уже существует"

Scenario: Checking registration new user
	Given website "https://dev.ticketscloud.org" and click "Зарегистрироваться"
	Then whrite in field name and assert button disabled
	Then whrite in field mobile and assert button disabled
	Then whrite in field email new email
	Then write in feald password invalid value and assert warning
	Then whrite in field valid password
	Then select "Я - Организатор"
	Then push button and wait to get page source
	Then page include text "Заполните реквизиты"