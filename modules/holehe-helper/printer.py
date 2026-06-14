def print_results(results: list[dict]):
	found   = [r for r in results if r.get("exists")]
	limited = [r for r in results if r.get("ratelimit")]

	print(f"\nНайдено: {len(found)} аккаунтов\n")

	for r in found:
		name     = r["name"]
		domain   = r["domain"]
		recovery = r.get("emailrecovery")
		phone    = r.get("phoneNumber")

		print(f"[+] {name} ({domain})")

		if recovery:
			print(f" recovery: {recovery}")

		if phone:
			print(f" phone:	{phone}")

	if limited:
		print("\n[!] Rate limit:")

		for r in limited:
			print(f" - {r['name']}")
