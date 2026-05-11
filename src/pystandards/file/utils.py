from typing import Union
from pathlib import Path


def is_filename_valid_for_file_extension(
    filename: str,
    file_extension_enum_class: Union['FileExtension', 'TextFileExtension', 'AudioFileExtension', 'ImageFileExtension', 'VideoFileExtension', 'SubtitleFileExtension'] 
):
    """
    Check if the `filename` provided is valid for
    the also given `file_extension_enum_class`.
    """
    if not isinstance(filename, str):
        raise Exception('The "filename" provided is not a str.')

    extension = Path(filename).suffix.removeprefix('.')

    return (
        False
        if extension == '' else
        file_extension_enum_class.is_valid(extension.replace('.', ''))
    )