import os
import re
import time
import pprint
import datetime
import multiprocessing

import Selenium


if __name__ == "__main__":
	# Console Message
	info_list = [
		"請輸入登入帳號: ",																	# 0
		"請輸入登入密碼: ",																	# 1
		"請輸入櫃號: ",																		# 2
		"請輸入檔次名稱: ",																	# 3
		"請輸入單品名稱: ",																	# 4
		"請輸入單品價格: ",																	# 5
		"請輸入單品數量: ",																	# 6
		"一級分類(不顯示, 直接填入預設值18): ",													# 7
		"二級分類(不顯示, 直接填入預設值119): ",												# 8
		"請輸入檔次販售數量: ",																# 9
		"請輸入檔次圖片路徑(因為可能有複數, 因此輸入End表示結束, 不然會持續要求輸入直到6次): ",		# 10
		"請輸入檔次介紹(如要換行的地方加\\n): ",													# 11
		"請輸入檔次有效時間起點(格式: 2021/07/04): ",											# 12
		"請輸入檔次有效時間終點(格式: 2021/08/04, 月的數字要>起點, 日的數字要>=起點才不會出錯): ",	# 13
		"請輸入是否開啟宅配選項(Y/N): ",														# 14
		"請輸入是否公開銷售(Y/N): ",															# 15
		"請輸入重複輸入次數: "																	# 16
	]

	web_driver_path = os.path.join(".", "chromedriver")
	web_url = "https://app-counter.skm.com.tw/#/login"

	keyin_list = []
	# Test Data
	keyin_list = [
		# "00022354",
		# "19970305",
		# "7112084",
		# "測試",
		# "單品名稱",
		# "1",
		# "10",
		# "18",
		# "119",
		# "100",
		# ["/Users/garyliang/Downloads/Test1.jpeg", "/Users/garyliang/Downloads/Test2.jpeg"],
		# "檔次介紹\nblablabla",
		# ["2021", "06", "14"],
		# ["2021", "07", "30"],
		# False,
		# False,
		# "2"

		"00022354",
		"19970305",
		"7107314",
		"熱銷商品",
		"鴛鴦鐵板萬用鍋",
		"3990",
		"1",
		"17",
		"113",
		"10",
		["/Users/garyliang/Downloads/Test4.jpg"],
		"",
		["2021", "09", "26"],
		["2021", "10", "01"],
		False,
		False,
		"800"
	]

	def check_number(val: str):
		try:
			int(val)
			print(f"{val}: 數字檢查正確")
		except:
			raise Exception(f"{val}: 含有不是數字的內容")

	# for idx, val in enumerate(info_list):
	# 	if idx == 7:
	# 		keyin_list.append("17")
	# 	elif idx == 8:
	# 		keyin_list.append("113")
	# 	elif idx == 10:
	# 		img_path = []
	# 		keyin = input(val)
	# 		while (keyin.lower() != "end" or len(img_path) == 0) and len(img_path) < 6:
	# 			if keyin not in ["end", ""]:
	# 				img_path.append(keyin)
	# 			if len(img_path) < 6:
	# 				keyin = input(val)
	# 		keyin_list.append(img_path)
	# 	elif idx in [12, 13]:
	# 		keyin = input(val)
	# 		time_list = keyin.split("/")
	# 		assert len(time_list) == 3, "格式不正確, 要為YYYY/MM/DD"
	# 		assert len(time_list[0]) == 4, "格式不正確, 年要4碼"
	# 		assert len(time_list[1]) == 2, "格式不正確, 月要2碼"
	# 		assert len(time_list[2]) == 2, "格式不正確, 日要2碼"
	# 		check_number(time_list[0])
	# 		check_number(time_list[1])
	# 		check_number(time_list[2])
	# 		keyin_list.append(time_list)
	# 	elif idx in [14, 15]:
	# 		keyin = input(val)
	# 		if keyin.lower() == "y":
	# 			keyin_list.append(True)
	# 		else:
	# 			keyin_list.append(False)
	# 	elif idx in [5, 6, 9, 16]:
	# 		keyin = input(val)
	# 		check_number(keyin)
	# 		keyin_list.append(keyin)
	# 	else:
	# 		keyin_list.append(input(val))

	for i in zip(info_list, keyin_list):
		pprint.pprint(i)

	count = 0
	process_num = 3 # multiprocessing.cpu_count()

	pool = multiprocessing.Pool(process_num)

	ts = datetime.datetime.now()

	while count < int(keyin_list[16]):
		res_list = [pool.apply_async(Selenium.selenium_process, args=(keyin_list, web_url)) for i in range(process_num)]

		for res in res_list:
			count = count + 1 if res.get(timeout=30) else count

		print(f"No. {count} Done!")

	pool.close()	# Stop accepting work
	pool.join()		# Wait until all processes finished

	# Selenium.selenium_process(keyin_list, web_url)

	te = datetime.datetime.now()

	print(f"{'Process Starts from': <20} {ts.strftime('%Y/%m/%d %H:%M:%S')}")
	print(f"{'Process Ends at': <20} {te.strftime('%Y/%m/%d %H:%M:%S')}")

	td = (te - ts).total_seconds()
	td_ave = td / (count - 1)

	td = f"{td // 3600:02.0f}:{td % 3600 // 60:02.0f}:{td % 60:02.0f}"					# timedelta string formating
	td_ave = f"{td_ave // 3600:02.0f}:{td_ave % 3600 // 60:02.0f}:{td_ave % 60:02.0f}"	# timedelta string formating

	print(f"{'Time Cost': <20} {td}")
	print(f"{'Average Time Cost': <20} {td_ave} per case")
















