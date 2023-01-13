from PIL import Image
import click
import os
__version__='0.0.1'

def add_string_to_filename(file_path:str, string:str, extension:str=None, add_to_front=True):
    # Get the directory, base name and extension
    dirname, filename = os.path.split(file_path)
    base_name, file_extension = os.path.splitext(filename)
    if extension is not None:
        file_extension = '.' + extension
    
    # Add the string to the front or end of the base name
    if add_to_front:
        new_base_name = string + base_name
    else:
        new_base_name = base_name + string
    
    # Rebuild the file path with the modified base name
    new_filename = new_base_name + file_extension
    new_file_path = os.path.join(dirname, new_filename)
    
    return new_file_path


def convert_to_ico(image_file):
    output_file_name = add_string_to_filename(image_file,'','ico')
    img = Image.open(image_file)
    img.save(output_file_name)
    

@click.command()
@click.option('-i', '--input-file',
              type=click.Path(file_okay=True, dir_okay=False),
              prompt=True,
              help='Input log file')
@click.version_option(__version__)
def cli(input_file):
    output_cleaned_log_file_name = convert_to_ico(input_file)
    
if __name__ == "__main__":
    '''
        Usage: path/to/python3 log_parser.py [OPTIONS] COMMAND [ARGS]...
    '''
    cli()