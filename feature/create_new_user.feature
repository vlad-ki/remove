Feature: Register process

	Scenario: Start the register process
		Given the website "https://stage.ticketscloud.org/#/"
		When I click on the register button
		Then I see the account register page

	Scenario: Checking warning with invalid data in form
		Given invalid registration data
		When I enter invalid data in registration form
		Then I see warning
		And registration button is disabled 

	Scenario: Registration already registred user
		Given data of already registred user
		When I enter data in regisration form
		And select "i-am-org" in user group
		And click on the submit button 
		Then I see warning with text "Пользователь abc_cba07@mail.ru уже существует"

	Scenario: Registration with valid data
		Given valid registration data
		When I enter valid data in the registratio form
		And select "i-am-org" in user group
		And click on the submit button
		Then I see the page of Personal Aria 

	Scenario: Checking empty fields for warnings (ip)
		Given the page of requisites filling
		When check that the felds are empty
		And the "license_agreement" is't check
		And I click on the submit button
		Then I see warnings

	Scenario: Cheching fealds for valid re expression (ip)
		Given the page of requisites filling
		When I check the re expression in fields
		Then it's OK

	Scenario: Can not save with invalid data (ip)
		Given the page of requisites filling
		And invalid data
		When I enter invalid data in the fields
		And I click on the submit button
		Then I see warnings

	Scenario: Save requisites with valid data (ip)
		Given the page of requisites filling
		And valid requisites data
		When I enter valid requisites data in the field
		And check NDS with sistem of taxation
		And check "I agree with the EULA"
		And I click on the submit button
		Then I see "Создание профиля компании"

