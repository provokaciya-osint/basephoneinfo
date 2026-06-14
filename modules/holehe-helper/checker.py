import asyncio
import httpx
from holehe.core import get_functions, import_submodules

modules = import_submodules("holehe.modules")


async def check_email(email: str) -> list[dict]:
	async with httpx.AsyncClient() as client:
		results = []
		tasks = []

		for func in get_functions(modules):
			tasks.append(func(email, client, results))

		await asyncio.gather(*tasks, return_exceptions=True)

	return results


def run(email: str) -> list[dict]:
	return asyncio.run(check_email(email))
