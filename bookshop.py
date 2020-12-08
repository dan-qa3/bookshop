from selenium import webdriver #pip install selenium
import random
import time
import fire #pip install fire
import colorama #pip install colorama
from colorama import Fore, Back, Style 
colorama.init()

start_time = time.time()
driver = webdriver.Firefox() # Firefox, Chrome
count_s = 0;
count_f = 0;
count_b = 0;
driver.get("http://www.sharelane.com/cgi-bin/main.py")
print(driver.title)

# ---------- REGISTRATION ----------
def registration(debug = ''):
	global count_s, count_f
	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	driver.get("http://www.sharelane.com/cgi-bin/register.py")
	
	driver.find_element_by_xpath("//input[@name='zip_code']").send_keys("12345")
	driver.find_element_by_xpath("//input[@value='Continue']").click()

	driver.find_element_by_xpath("//input[@name='first_name']").send_keys("qwerty")

	randint = str(random.randint(1, 999999) + random.randint(1, 999999))
	driver.find_element_by_xpath("//input[@name='email']").send_keys("qwerty" + randint +"@gmail.com")

	password = '123456';
	driver.find_element_by_xpath("//input[@name='password1']").send_keys(password)
	driver.find_element_by_xpath("//input[@name='password2']").send_keys(password)
	driver.find_element_by_xpath("//input[@value='Register']").click()

	confirmation_message = driver.find_element_by_css_selector(".confirmation_message");

	
	if(confirmation_message.text == 'Account is created!'):
		if(debug == ''):
			count_s += 1
			print('')
			print('Registration: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('')
			print('Registration: Failed')
# ---------- END REGISTRATION ----------


# ---------- LOGIN ----------
def login(debug = ''):
	global count_s, count_f
	reg_email = driver.find_element_by_css_selector(".form_all_underline > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > b:nth-child(1)")
	reg_pass = driver.find_element_by_css_selector(".form_all_underline > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
	list  = [reg_email.text, reg_pass.text];

	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	driver.find_element_by_xpath("//input[@name='email']").send_keys(list[0])
	driver.find_element_by_xpath("//input[@name='password']").send_keys(list[1])
	driver.find_element_by_xpath("//input[@value='Login']").click()

	#------get cookie------
	cookies_list = driver.get_cookies()
	cookies_dict = {}
	for cookie in cookies_list:
		cookies_dict[cookie['name']] = cookie['value']
	#----------------------

	if(cookies_dict['email'] == '"' + list[0] + '"'):
		if(debug == ''):
			count_s += 1
			print('')
			print('Login: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('')
			print('Login: Failed')
# ---------- END LOGIN ----------


# ---------- SEARCHING BY AUTHOR ----------				
def searching_by_author(num, debug = ''):		
	global count_s, count_f
	print('')
	print('searching by author testing...')
	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	
	count_books = 0 
	i = 1;
	while(i <= num):
		name_author = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > p:nth-child(1) > b:nth-child(1)').text
		driver.find_element_by_css_selector(".form_all_underline > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(1) > input:nth-child(1)").send_keys(name_author)
		driver.find_element_by_xpath("//input[@value='Search']").click()
		
		try:
			name_author1 = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(1) > b:nth-child(1)').text
			print(name_author + ' - ' + name_author1)
			if(name_author == name_author1):
				count_books = count_books + 1
			else: 
				print('Error')
		except:
			print(Fore.RED + "Match wasn't found" + Style.RESET_ALL)
		
		i += 1
		driver.get("http://www.sharelane.com/cgi-bin/main.py")
		
	print('---' + str(count_books) + ' matches of ' + str(num) + '---') #checkout
	
	if(count_books == (i - 1)):
		if(debug == ''):
			count_s += 1
			print('Searching by author: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('Searching by author: Failed')	
# ---------- END SEARCHING BY AUTHOR ----------


# ---------- SEARCHING BY TITLE ----------
def searching_by_title(num, debug = ''):
	global count_s, count_f
	print('')
	print('searching by title testing...')
	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	
	count_books = 0 
	i = 1;
	while(i <= num):
		name_book = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > a:nth-child(1)').text
		driver.find_element_by_css_selector(".form_all_underline > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(1) > input:nth-child(1)").send_keys(name_book)
		driver.find_element_by_xpath("//input[@value='Search']").click()
		name_book1 = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(2)').text
		
		if(name_book == name_book1):
			count_books = count_books + 1
			print(name_book + ' - ' + name_book1)
		else:
			print(Fore.RED + (name_book + ' - ' + name_book1) + Style.RESET_ALL)
		i += 1
		
		driver.get("http://www.sharelane.com/cgi-bin/main.py")
		
	print('---' + str(count_books) + ' matches of ' + str(num) + '---') #checkout
	
	if(count_books == (i - 1)):
		if(debug == ''):
			count_s += 1
			print('Searching by title: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('Searching by title: Failed')
# ---------- END SEARCHING BY TITLE ----------


# ---------- ADDING TO CART ----------
def adding_one_book_to_cart(debug = ''):
	global count_s, count_f
	def _add_one_book():
		global name_book1, name_book2
		driver.get("http://www.sharelane.com/cgi-bin/main.py")
		driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > a:nth-child(1)').click()
		name_book1 = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(1) > b:nth-child(1)').text
		driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(2) > a:nth-child(1)').click()
		driver.get("http://www.sharelane.com/cgi-bin/shopping_cart.py")
		name_book2 = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)').text
	
	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	
	cookies = driver.get_cookies() # returns list of dicts
	login_status = False
	if cookies:
		login_status = True
	
	if login_status:
		_add_one_book()
	else:
		registration()
		login()
		_add_one_book()
		
	if(name_book1 == name_book2):
		if(debug == ''):
			count_s += 1
			print('')
			print('Adding to cart one book: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('')
			print('Adding to cart one book: Failed')
# ---------- END ADDING TO CART ----------


# ---------- ADDING TO CART SEVERAL BOOKS ----------
def adding_multiple_items_to_cart():
	global count_b
	count_b += 1
	print('')
	print('Adding multiple items to cart: Blocked')
# ---------- END ADDING TO CART ----------


# ---------- UPDATE CART ----------
def update_cart(amount, debug = ''):
	global count_s, count_f
	driver.get("http://www.sharelane.com/cgi-bin/shopping_cart.py")
	am = driver.find_element_by_xpath("//input[@name='q']")
	am.clear()
	am.send_keys(amount)
	driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
	amount1 = driver.find_element_by_xpath("//input[@name='q']").get_attribute("value")

	if(int(amount1) == int(amount)):
		if(debug == ''):
			count_s += 1
			print('')
			print('Update cart: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('')
			print('Update cart: Failed')
# ---------- END ADDING TO CART ----------


# ---------- CLEAR CART ----------
def clear_cart():
	global count_s, count_f, count_b
	driver.get("http://www.sharelane.com/cgi-bin/shopping_cart.py")
	count_b += 1
	print('')
	print('Clear cart: Blocked')
# ---------- END CLEAR CART ----------


# ---------- CHECKOUT ----------
def checkout(debug = ''):
	global count_s, count_f
	driver.get("https://www.sharelane.com/cgi-bin/get_credit_card.py?type=1")
	credit_card_number = driver.find_element_by_css_selector('body > center:nth-child(1) > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > center:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1) > b:nth-child(1)').text
	#print(credit_card_number)
	
	driver.get("http://www.sharelane.com/cgi-bin/shopping_cart.py")
	driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > form:nth-child(1) > input:nth-child(1)').click()
	driver.find_element_by_name("card_number").send_keys(credit_card_number)
	
	driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(4) > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(2) > input:nth-child(1)').click()
	
	msg = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > p:nth-child(1) > font:nth-child(1) > b:nth-child(1)')

	if(msg):
		if(debug == ''):
			count_s += 1
			print('')
			print('Checkout: Successful')
	else:
		if(debug == ''):
			count_f += 1
			print('')
			print('Checkout: Failed')
# ---------- END CHECKOUT ----------


# ---------- LOGOUT ----------
def logout(debug = ''):
	global count_s, count_f
	driver.get("http://www.sharelane.com/cgi-bin/main.py")
	
	cookies = driver.get_cookies() # returns list of dicts
	if cookies:
		driver.find_element_by_css_selector('tr.grey_bg:nth-child(3) > td:nth-child(1) > a:nth-child(1)').click()
		count_s += 1
		if(debug == ''):
			print('')
			print('Logout: Successful')
	else:
		count_f += 1
		if(debug == ''):
			print('')
			print('Logout: Failed')
# ---------- END LOGOUT ----------


# ---------- DISCOUNT TEST ----------
def discount(num1, num2):
	registration('n')
	login('n')
	adding_one_book_to_cart('n')
	am = driver.find_element_by_xpath("//input[@name='q']")
	am.clear()
	
	print('')
	print('Scanning for bugs in discount...')
	#i = num1
	while(num1 <= num2):
		driver.get("http://www.sharelane.com/cgi-bin/shopping_cart.py")
		am = driver.find_element_by_xpath("//input[@name='q']")
		am.clear()
		am.send_keys(num1)
		driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
		quantity = driver.find_element_by_xpath("//input[@name='q']").get_attribute("value")
		discount = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5) > p:nth-child(1) > b:nth-child(1)').text
		c = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(7)').text
		price = driver.find_element_by_css_selector('.form_all_underline > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)').text
		first = (int(quantity) * float(price))
		second = (int(quantity) * (float(price) * int(discount))/100)
		exp_total = str( first - second )
		#print(str(quantity) + ' - ' + str(discount) + ' % --- ' + str( first - second ) + ' - ' + str(c))
		
		if(int(quantity) == 1):
			print('quantity '+ str(quantity) + ' -- ' + 'discount ' + str(discount) + ' % --- ' + 'expected total ' + exp_total + ' --- ' +'actual total ' + str(c))
		elif(int(quantity) > 1 and int(quantity) < 10):
			print('quantity '+ str(quantity) + ' -- ' + 'discount ' + str(discount) + ' % --- ' + 'expected total ' + exp_total + ' -- ' +'actual total ' + str(c))
		elif(int(quantity) == 10 and float(exp_total) < 100):
			print('quantity '+ str(quantity) + ' - ' + 'discount ' + str(discount) + ' % --- ' + 'expected total ' + exp_total + ' -- ' +'actual total ' + str(c))
		else:
			print('quantity '+ str(quantity) + ' - ' + 'discount ' + str(discount) + ' % --- ' + 'expected total ' + exp_total + ' - ' +'actual total ' + str(c))
		num1 += 1
#------------END DISCOUNT TEST-----------

#------------PRINT TOTAL-----------
def print_total():
	print('')
	print('-------------------------------------------')
	print('TOTAL: Successful ' + str(count_s) + ', Failed ' + str(count_f) + ', Blocked ' + str(count_b))
	print('-------------------------------------------')
	#print('')
	#print("--- %s seconds ---" % (time.time() - start_time))

	t = time.time() - start_time
	print("-------------- "+ str(round(t, 1)) +" seconds --------------")
	print('-------------------------------------------')
#------------END PRINT TOTAL-----------


# ---------- FULL TEST ----------
def full_test():
	registration()
	login()
	searching_by_author(5)
	searching_by_title(20)
	adding_one_book_to_cart()
	adding_multiple_items_to_cart()
	update_cart(5)
	checkout()
	clear_cart()
	logout()
	
	print_total()
#--------------------------------
	

if __name__ == '__main__':
	fire.Fire()
