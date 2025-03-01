import requests


def get_random_wikipedia_article():
    url = "https://en.wikipedia.org/wiki/Special:Random"

    response = requests.get(url)

    if response.status_code == 200:
        return response.url
    else:
        return None


def main():
    print("Программа покажет вам случайную статью из Википедии.")

    random_article_url = get_random_wikipedia_article()

    if random_article_url:
        user_input = input(
            f"Ссылка на случайную статью: {random_article_url}\nХотите посмотреть статью? (да/нет): ").strip().lower()

        if user_input == "да":
            print(f"Открываем статью: {random_article_url}")
        else:
            print("Хорошо, до свидания!")
    else:
        print("Не удалось получить случайную статью. Попробуйте позже.")


if __name__ == "__main__":
    main()