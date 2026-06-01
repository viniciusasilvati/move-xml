# move-xml

A small Python utility that watches a source directory and moves all `.xml` files to a destination directory every 10 minutes.

## Project structure

- `main.py` — main script that reads configuration and moves XML files.
- `config.json` — JSON config file defining source and destination directories.
- `README.md` — project documentation.

## Requirements

- Python 3.8 or newer

## Configuration

Edit `config.json` to set the paths for the shared drive and local drive:

```json
{
    "diretorio": {
        "drive_compartilhado": "C:\\Teste1",
        "drive_local": "C:\\Teste2"
    }
}
```

- `drive_compartilhado`: directory where XML files are read from.
- `drive_local`: directory where XML files are moved to.

## Usage

Run the script from the project folder:

```bash
python main.py
```

The script will:

1. load `config.json`
2. scan the source directory for `.xml` files
3. move each XML file to the destination directory if it does not already exist there
4. print a status message for each file
5. wait 10 minutes and repeat

## Behavior

- Only files ending with `.xml` (case-insensitive) are processed.
- Existing files at the destination are not overwritten.
- Errors while moving individual files are caught and printed.
- The script runs continuously until stopped.

## Notes

- Ensure both source and destination directories exist and the script has permission to access them.
- This project is intended for simple file-moving automation; it does not currently support subdirectory recursion or file deletion.

## License

This project is provided as-is, with no warranty.

