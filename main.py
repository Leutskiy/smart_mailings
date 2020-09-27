import os
import json
import click
import appconfig


from varname import nameof
from typing import List


BUCKET = appconfig.cfg.folder


@click.command()
@click.argument('directory', nargs=1, type=click.Path(exists=False))
@click.option('--priority', '-p', default=3)
def run(directory: str, priority: int) -> None:
    """
    The method for starting of the Service Uploader.

    """

    file_paths = []
    metadata = {}

    # забрать все пути к файлам из директории
    all_file_paths_in_directory = get_files_from_dir(directory)
    file_paths.extend(all_file_paths_in_directory)

    print(file_paths)

    # метаданные
    # сформировать словарь
    # прокинуть данные в json
    priority_key = nameof(priority)
    metadata[priority_key] = priority

    metadata_file_path = os.path.join(BUCKET, "metadata.txt")
    with open(metadata_file_path, 'w') as metadata_writer:
        json.dump(obj=metadata, fp=metadata_writer)


def get_files_from_dir(directory: str) -> List[str]:
    if directory is None:
        raise ValueError(f"The {nameof(directory)} param should not be None")

    all_files_in_dir = []
    for root, dirs, files in os.walk(directory):
        for _file in files:
            if _file.startswith('metadata'):
                continue

            full_file_name = os.path.join(root, _file)
            all_files_in_dir.append(full_file_name)

    return all_files_in_dir


if __name__ == "__main__":
    run()
