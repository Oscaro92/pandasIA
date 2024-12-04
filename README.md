# pandas IA
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) ![PandasAI](https://img.shields.io/badge/PandasAI-150458?style=flat&logo=pandas&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)

A chat for your data in natural language.

## 🔧 Installation

Clone the repository
```shell
git clone https://github.com/Oscaro92/pandasIA.git
cd pandasIA
```

Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

Install dependencies
```shell
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file with the following variables:
```
OPENAI_API_KEY=<your_api_key>
```

## 🚀 Usage

Load & save documents from Google drive  
```shell
python chat.py
```

## 📁 Project Structure

```
mail-agent/
├── agent.py            # Agent 
├── chat.py             # Chat
├── requirements.txt    # Dependencies
├── .env                # Environment variables
└── README.md           # Documentation
```

## 📝 License

This project is licensed under the MIT License.