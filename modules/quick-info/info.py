from dataclasses import dataclass

from phonenumbers import parse, geocoder, carrier, number_type, timezone, PhoneNumberType

TYPE_NAMES: dict[PhoneNumberType, str] = {
	PhoneNumberType.MOBILE: "Мобильный",
	PhoneNumberType.FIXED_LINE: "Стационарный",
	PhoneNumberType.FIXED_LINE_OR_MOBILE: "Стационарный или мобильный",
	PhoneNumberType.TOLL_FREE: "Бесплатный",
	PhoneNumberType.PREMIUM_RATE: "Премиум",
	PhoneNumberType.VOIP: "VoIP",
	PhoneNumberType.UNKNOWN: "Неизвестен",
}


@dataclass
class PhoneInfo:
	geo: str
	carrier: str
	type: str
	timezones: tuple[str, ...]


def get_info(number: str) -> PhoneInfo:
	parsed = parse(number)
	ntype = number_type(parsed)
	return PhoneInfo(
		geo=geocoder.description_for_number(parsed, "ru"),
		carrier=carrier.name_for_number(parsed, "ru"),
		type=TYPE_NAMES.get(ntype, "Неизвестен"),
		timezones=timezone.time_zones_for_number(parsed),
	)
