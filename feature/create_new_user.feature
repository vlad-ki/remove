Feature: Register process

	Scenario: Start the register process
		Given the website "https://stage.ticketscloud.org/#/"
		When I click on the register button
		Then I see the account register page

	Scenario: Checking warning with invalid data in form
		Given invalid data
		When I enter invalid data
		Then I see warning
		And registration button is disabled 

		