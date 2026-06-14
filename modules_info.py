from modules import loader

loader.load_all()

for name, entry in loader.all_modules().items():
    meta = entry["meta"]
    funcs = entry["functions"]

    print(
        f"Модуль: {meta['name']}",
        f"Версия: {meta['version']}",
        f"Описание: {meta['description']}",
        f"Автор: {meta['author']}",
        sep="\n"
    )

    if funcs:
        print("Функции:")
        for func in funcs:
            print(f"  {func['name']} — {func['description']}")

    print()
