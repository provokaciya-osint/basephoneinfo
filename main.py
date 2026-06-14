from modules import loader

loader.load_all()

def show_main_menu():
    modules = loader.all_modules()
    print("\n=== BASEPHONEINFO ===")
    print("Доступные модули:\n")
    for i, (name, entry) in enumerate(modules.items(), 1):
        meta = entry["meta"]
        print(f"  {i}. {meta.get('name', name)} — {meta.get('description', '')}")
    print("\n  0. Выход")
    return modules

def main():
    while True:
        modules = show_main_menu()
        names = list(modules.keys())

        choice = input("\n>>> ").strip()

        if choice == "0":
            print("Выход.")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(names):
            name = names[int(choice) - 1]
            module = loader.get(name)
            print()
            module.main()
            input("\nНажмите Enter для возврата...")
        else:
            print("Неверный выбор.")

try:
    main()
except (EOFError, KeyboardInterrupt):
    pass
