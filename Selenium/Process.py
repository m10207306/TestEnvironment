from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

def process(driver, wait, keyin_list):
	# 登入的緩衝時間
	wait.until(EC.element_to_be_clickable( (By.XPATH, "//img[@src='/img/addProduct.be812c14.svg']") ), 
			   "找不到新增商品按鈕")

	# 按新增商品
	driver.find_element_by_xpath("//img[@src='/img/addProduct.be812c14.svg']").click()

	# 等動態網頁更新
	wait.until(EC.element_to_be_clickable(
					(By.XPATH, 
					 "//input[@id='currentCounter']") ), 
			   "找不到輸入櫃號欄位")

	# 輸入櫃號
	driver.find_element_by_xpath("//input[@class='form-control']").send_keys(keyin_list[2])

	# 等待動態網頁更新
	wait.until(EC.element_to_be_clickable(
					(By.XPATH, 
					 "//div[@class='form-group pt-2 mb-4']/input[@class='form-control']") ), 
			   "找不到檔次名稱")

	# 輸入檔次名稱
	driver.find_element_by_xpath("//div[@class='form-group pt-2 mb-4']/input[@class='form-control']").send_keys(keyin_list[3])
	# 輸入單品名稱
	driver.find_element_by_xpath("//div[@class='form-group pt-4']/input[@id='dddd']").clear()
	driver.find_element_by_xpath("//div[@class='form-group pt-4']/input[@id='dddd']").send_keys(keyin_list[4])
	# 輸入單品價格
	driver.find_element_by_xpath("//div[@class='form-group pt-2']/input[@class='form-control itemPrice']").clear()
	driver.find_element_by_xpath("//div[@class='form-group pt-2']/input[@class='form-control itemPrice']").send_keys(keyin_list[5])
	# 輸入單品數量
	driver.find_element_by_xpath("//div[@class='form-group pt-2']/input[@class='form-control itemQuantity']").send_keys(keyin_list[6])
	# 輸入一級分類
	# value = 17, text = 17 家電
	# value = 18, text = 18 生活居家用品
	# value = 24, text = 24 3C
	# value = 7, text = 07 保養
	# value = 9, text = 09 香水香氛
	# value = 8, text = 其他 - 08 彩妝
	# value = 25, text = 其他 - 25 服務
	# value = 3, text = 其他 - 03 女性配件
	# value = 5, text = 其他 - 05 男性配件
	# value = 4, text = 其他 - 04 女性服飾
	# value = 6, text = 其他 - 06 男性服飾
	# value = 10, text = 其他 - 10 運動配件
	# value = 11, text = 其他 - 11 運動服飾
	# value = 12, text = 其他 - 12 戶外休閒配件
	# value = 16, text = 其他 - 16 兒童服飾
	# value = 15, text = 其他 - 15 兒童配件
	# value = 14, text = 其他 - 14 婦嬰用品
	# value = 19, text = 其他 - 19 食品
	# value = 20, text = 其他 - 20 小吃
	# value = 21, text = 其他 - 21 餐廳
	# value = 22, text = 其他 - 22 飲品/冰品
	# value = 26, text = 其他 - 26 文化藝術
	select1 = driver.find_element_by_xpath("//div[@class='incomplete-box item-box']//div//div//div[@class='form-group pt-2'][1]//select[@class='form-control'][1]")
	class_1 = Select(select1)

	# options = class_1.options
	# for opt in options:
	# 	print(f"value = {opt.get_attribute('value')}, text = {opt.text}")

	class_1.select_by_value(keyin_list[7])

	# 等待動態網頁跑出二級分類
	wait.until(EC.element_to_be_clickable(
					(By.XPATH, 
					 "//div[@class='incomplete-box item-box']//div//div//div[@class='form-group pt-2'][2]//select[@class='form-control'][1]") ), 
			   "找不到二級分類")

	# 輸入二級分類
	# 一級 value = 18 的二級:
	# value = 114, text = 01 客廳用品
	# value = 115, text = 02 廚房用品
	# value = 116, text = 03 餐廳用品
	# value = 117, text = 04 臥室用品
	# value = 118, text = 05 浴室用品
	# value = 119, text = 06 其他用品

	# 一級 value = 17 的二級:
	# value = 109, text = 01 環境家電
	# value = 110, text = 02 廚房家電
	# value = 111, text = 03 生活家電
	# value = 112, text = 04 美容家電
	# value = 113, text = 05 其他家電
	select2 = driver.find_element_by_xpath("//div[@class='incomplete-box item-box']//div//div//div[@class='form-group pt-2'][2]//select[@class='form-control'][1]")
	class_2 = Select(select2)

	# options = class_2.options
	# for opt in options:
	# 	print(f"value = {opt.get_attribute('value')}, text = {opt.text}")

	class_2.select_by_value(keyin_list[8])

	# 輸入檔次販售數量
	driver.find_element_by_xpath("//input[@id='quantity']").send_keys(keyin_list[9])

	# 上傳影像
	for idx, val in enumerate(keyin_list[10]):
		driver.find_element_by_xpath("//input[@id='picFile']").send_keys(val)
		wait.until(EC.element_to_be_clickable(
						(By.XPATH, 
						 f"//div[@class='swiper-wrapper']//div[{idx+1}]") ), 
				   f"上傳第{idx+1}張影像失敗")

	# 輸入檔次介紹
	driver.find_element_by_xpath("//textarea[@id='description']").send_keys(keyin_list[11])

	# 輸入檔次有效時間起點
	driver.find_element_by_xpath("//input[@id='startDate']").send_keys(keyin_list[12][0])
	driver.find_element_by_xpath("//input[@id='startDate']").send_keys(Keys.TAB)
	driver.find_element_by_xpath("//input[@id='startDate']").send_keys(keyin_list[12][1])
	driver.find_element_by_xpath("//input[@id='startDate']").send_keys(keyin_list[12][2])
	driver.find_element_by_xpath("//input[@id='startDate']").send_keys(Keys.TAB)

	# 輸入檔次有效時間終點
	driver.find_element_by_xpath("//input[@id='endDate']").send_keys(keyin_list[13][0])
	driver.find_element_by_xpath("//input[@id='endDate']").send_keys(Keys.TAB)
	driver.find_element_by_xpath("//input[@id='endDate']").send_keys(keyin_list[13][1])
	driver.find_element_by_xpath("//input[@id='endDate']").send_keys(keyin_list[13][2])

	# 選取是否開啟宅配選項
	if keyin_list[14]:
		driver.find_element_by_xpath("//label[@for='cb1']").click()

	# 選取是否公開銷售
	if keyin_list[15]:
		driver.find_element_by_xpath("//label[@for='cb2']").click()

	# 按商品上架
	driver.find_element_by_xpath("//button[@class='btn btn-lg btn-block mb-2 mt-5']").click()

	# 按確定
	wait.until(EC.element_to_be_clickable(
					(By.XPATH, 
					 "//button[@class='btn btn-classic btn-block'][text()=' 確定 ']")), 
			   "找不到確定按鈕")
	driver.find_element_by_xpath("//button[@class='btn btn-classic btn-block'][text()=' 確定 ']").click()

	# 按跳出成功視窗的確定
	wait.until(EC.alert_is_present(), "等不到跳出成功視窗")
	driver.switch_to.alert.accept()
