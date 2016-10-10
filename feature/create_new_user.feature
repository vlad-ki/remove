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
		And id of the fields
			|id       |
			|addr     |
			|ogrnip   |
			|inn      |
			|bank_name|
			|bik      |
			|ks       |
			|rs       |
		When check that the felds are empty
		And the "license_agreement" is't check
		And I click on the submit button
		Then I see warnings

	Scenario: Cheching fealds for valid re expression (ip)
		Given the page of requisites filling
		When I check the re expression in fields
			|id    |re        |
			|ogrnip|/^\d{15}$/|
        	|inn   |/^\d{12}$/|
        	|bik   |/^\d{9}$/ |
        	|ks    |/^\d{20}$/|
        	|rs    |/^\d{20}$/|
		Then it's OK

	Scenario: Can not save requisites with invalid data (ip)
		Given the page of requisites filling
		And invalid requisites data
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

	Scenario: Checking empty fields for warnings (org)
		Given the page of company profile filling
		And id of the fields
			|id         |
			|title      |
			|cc_name    |
			|cc_position|
		When check that the felds are empty
		And I click on the submit button
		Then I see warnings

	Scenario: Cheching fealds for valid re expression (org)
		Given the page of company profile filling
		When I check the re expression in fields
			|id      |re                                                                                            |
			|email   |/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}/                                            |
        	|phone   |/^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{2})[-. ]*(\d{1})[-. ]*(\d{2})[-. ]*(\d{2})\s*$/|
        	|cc_email|/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}/                                            |
        	|cc_phone|/^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{2})[-. ]*(\d{1})[-. ]*(\d{2})[-. ]*(\d{2})\s*$/|
		Then it's OK

	Scenario: Can not save with invalid data (org)
		Given the page of company profile filling
		And invalid data
		When I enter invalid data in the fields
		And I click on the submit button
		Then I see warnings