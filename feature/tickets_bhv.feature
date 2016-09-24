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
	Then click button "Индивидуальный предприниматель" in Personal Area
	Then write in field "ФИО ПОЛНОСТЬЮ" and assert filling important fields
	Then write in field "АДРЕС РЕГИСТРАЦИИ" and assert filling important fields
	Then write in field "ОГРНИП" and assert filling important fields
	Then write in field "ИНН" and assert filling important fields
	Then choose value of "ХОЧУ ПОЛУЧАТЬ ПЛАТЕЖИ"
	Then choose value of "СИСТЕМА НАЛОГООБЛАЖЕНИЯ"
	Then write in field "НАЗВАНИЕ БАНКА" and assert filling important fields
	Then write in field "БИК" and assert filling important fields
	Then write in field "КОРР.СЧЕТ" and assert filling important fields
	Then write in field "РАСЧЕТНЫЙ СЧЕТ" and assert filling important fields
	Then click on "Согласен с Лицензионным договором"
	Then click submit
	Then click button "Организатор" in Personal Area
	Then write in field "НАЗВАНИЕ БРЕНДА"
	Then choose acquiring
	Then write in feald "ИМЯ"
	Then write in feald "ДОЛЖНОСТЬ" and fields validity checking
	Then checking field "EMAIL" for checking valid values
	Then checking field "ТЕЛЕФОН" for checking valid values
	Then checking field "CC_EMAIL" for checking valid values
	Then checking field "CC_ТЕЛЕФОН" for checking valid values and submit
	