# 📚 Digital Library Flask App 🚀

### 🎓 A Masterschool Project Applying Flask & SQL Principles 🐍🗃️

Welcome to the **Digital Library**, a web application to manage a personal digital book archive!  
You can 📖 add books, ✍️ manage authors, 🔍 search, 🔃 sort, and ❌ delete entries – all through a user-friendly Flask interface!

---

## 🧩 Table of Contents

- 🌟 Features
- 🛠️ Technologies
- 🚀 Installation
- 🧪 Usage
- 🧱 Project Structure
- ✅ Testing
- 🤝 Contributing
- 📄 License
- 🙌 Acknowledgments

---

## 🌟 Features

✨ **Manage Authors & Books**  
📥 Add authors and books with relevant details  
🔍 Searchable list of books  
🔃 Sort books by title or author  
🗑️ Delete books (and automatically remove authors with no books left)

---

## 🛠️ Technologies

- ⚙️ Python 3
- 🔥 Flask
- 🧮 SQLAlchemy & Flask-SQLAlchemy
- 🗂️ SQLite
- 🖼️ Jinja2 (Template Engine)
- 💻 Codio (Cloud-based Development Environment)

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Elmundo93/SQL-Flask-Libary.git
cd SQL-Flask-Libary

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python3 app.py
```

---

## 🧪 Usage

📂 Open your browser at: [http://localhost:5002](http://localhost:5002)  
🔧 Use the form to add authors and books  
🔍 Search the library with keywords  
↕️ Sort by title or author  
🗑️ Delete entries directly from the homepage

---

## 🧱 Project Structure

```
📁 SQL-Flask-Libary/
├── app.py              # Main Flask application
├── data_models.py      # SQLAlchemy models for authors and books
├── data/               # SQLite database storage
└── templates/          # Jinja2 HTML templates
```

---

## ✅ Testing

1. Open the terminal in Codio  
2. Start the app with `python3 app.py`  
4. Test all features: Add ✅ Search ✅ Sort ✅ Delete ✅

---

## 🤝 Contributing

Pull requests are welcome!  
1. Fork the project  
2. Create a branch (`git checkout -b feature/your-feature`)  
3. Commit your changes  
4. Open a pull request

---

## 📄 License

MIT License – free to use and extend 👐

---

## 🙌 Acknowledgments

- 🎓 **Masterschool** – for the inspiring learning environment  
- 🧑‍💻 **Flask & SQLAlchemy Communities** – for great documentation and support  

---

🚀 Happy Coding and Library Building!
