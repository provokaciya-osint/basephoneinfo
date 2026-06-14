from info import PhoneInfo

def print_info(info: PhoneInfo) -> None:
	tz = ", ".join(info.timezones) if info.timezones else "—"
	print(
		f"Регион:	   {info.geo or '—'}\n"
		f"Оператор:	 {info.carrier or '—'}\n"
		f"Тип:		  {info.type}\n"
		f"Часовой пояс: {tz}"
	)
