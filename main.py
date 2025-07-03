import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Обработка CSV файла с фильтрацией и агрегацией.'
    )
    parser.add_argument(
        '--file',
        type=str,
        required=True,
        help='Путь к CSV файлу'
    )
    parser.add_argument(
        '--where',
        type=str,
        help='Условие фильтрации в формате column<operator>value, например price>100'
    )
    parser.add_argument(
        '--aggregate',
        type=str,
        help='Агрегация в формате column=operation, например rating=avg'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    if args.where and args.aggregate:
        pass
        #TODO команду фильтрации и агрегации

    if args.where:
        pass
        #TODO команду фильтрации

    if args.aggregate:
        pass
        #TODO команду агрегации

    if not args.where and not args.aggregate:
        pass
        #TODO вьюкоманда или исключение

if __name__ == '__main__':
    main()