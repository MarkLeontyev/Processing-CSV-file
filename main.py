import argparse
from core.csv_handlers import read_csv
from commands.filter_command import WhereCommand
from commands.aggregate_command import AggregateCommand
from commands.pipeline import CommandPipeline
from tabulate import tabulate

def build_pipeline(args):
    pipeline = CommandPipeline()
    if args.where:
        pipeline.add(WhereCommand(args.where))
    if args.aggregate:
        col, op = args.aggregate.split("=")
        pipeline.add(AggregateCommand(col, op))
    return pipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where", help="Пример: row['age'] > 30")
    parser.add_argument("--aggregate", help="Пример: salary:sum")
    args = parser.parse_args()

    data = read_csv(args.file)
    pipeline = build_pipeline(args)
    result = pipeline.run(data)

    if isinstance(result, list) and result and isinstance(result[0], dict):
        print(tabulate(result, headers="keys", tablefmt="fancy_grid"))
    else:
        print(result)

if __name__ == "__main__":
    main()