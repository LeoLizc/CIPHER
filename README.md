# Cipher Encripter

This script provides a command-line interface for encrypting messages using different cipher techniques. It supports the Caesar cipher and keyword substitution cipher. The encrypted message can be saved to an output file or printed to the console.

## Prerequisites

Make sure you have the following requirements installed before running the script:
- Python (version 3 or above)

## Installation

1. Clone the repository or download the `codifier.py` file.

2. Install the required dependencies by running the following command inside the project folder:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using the following command:

```
python codifier.py [-h] (-m MESSAGE | -f FILE) [-o FILE] [-c [NUM]] [-k KEY]
```

The script accepts the following command-line arguments:

- `-h, --help`: Show the help message and exit.

- `-m MESSAGE, --message MESSAGE`: Specify the message to cipher.

- `-f FILE, --file FILE`: Specify the file containing the message to cipher.

- `-o FILE, --output FILE`: Specify the output file to save the encrypted message. If not provided, the encrypted message will be printed to the console.

- `-c [KEY], --caesar [KEY]`: Use the Caesar cipher with the given key. The key is the number of letters to shift (can be negative). If no key is provided, the default key is 3.

- `-k KEY, --keyword KEY`: Use the keyword substitution cipher with the given key. The key must be a string with no duplicate characters.

### Examples

```
python codifier.py -m "Hello, World!" -c 5 -k OpenAI -o encrypted.txt
```

This command encrypts the message "Hello, World!" using a Caesar cipher with a key of 5 and a keyword substitution cipher with the key "OpenAI". The encrypted message is saved to the file `encrypted.txt`.

```
python codifier.py -f input.txt -k secret
```

This command reads the message from the file `input.txt` and encrypts it using a keyword substitution cipher with the key "secret". The encrypted message is printed to the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
