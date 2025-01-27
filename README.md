# DeepSeek

DeepSeek is a Python project that interacts with the DeepSeek API to perform various tasks using OpenAI's capabilities.

## Project Structure
deepseek/ ├── bin/ ├── include/ ├── lib/ │ └── python3.9/ │ └── site-packages/ ├── pyvenv.cfg ├── README.md ├── requirements.txt └── scripts/ └── deepseek-r1.py

## Requirements

The project dependencies are listed in the `requirements.txt` file:

- annotated-types==0.7.0
- anyio==4.8.0
- certifi==2024.12.14
- distro==1.9.0
- exceptiongroup==1.2.2
- h11==0.14.0
- httpcore==1.0.7
- httpx==0.28.1
- idna==3.10
- jiter==0.8.2
- openai==1.60.1
- pydantic==2.10.6
- pydantic_core==2.27.2
- python-dotenv==1.0.1
- sniffio==1.3.1
- tqdm==4.67.1
- typing_extensions==4.12.2

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd deepseek
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv deepseek
    source deepseek/bin/activate  # On Windows use `deepseek\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the [scripts](http://_vscodecontentref_/4) directory and add your DeepSeek API key:
    ```sh
    echo "DS_API_KEY=your_api_key_here" > scripts/.env
    ```

## Usage

To run the script, execute the following command:
```sh
python scripts/deepseek-r1.py
