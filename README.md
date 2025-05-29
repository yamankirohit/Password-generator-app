# 🔐 Password Generator App using Streamlit

A simple and interactive **Password Generator Web App** built using **Python** and **Streamlit**. This tool allows users to generate secure passwords based on desired length and strength.

---

## ✨ Features

### ✅ User-Friendly Web Interface

* Built with Streamlit for quick and clean UI.
* No need to use terminal or command-line tools.

### 🔑 Password Strength Options

Users can select from three levels of password strength:

* **Weak**: Uses only lowercase letters.
* **Medium**: Uses lowercase + uppercase + digits.
* **Strong**: Uses lowercase + uppercase + digits + special characters.

### 🔢 Adjustable Password Length

* Users can choose password length between **4 and 50 characters**.
* Ensures secure minimum length of 4 characters.

### ✨ Smart Character Inclusion

* Automatically ensures at least one character from each category based on the selected strength.
* Password is shuffled for maximum randomness.

### ⬇️ One-Click Password Generation

* Simply click the "Generate Password" button and get your secure password instantly.

---

## 📚 How to Run the App

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/password-generator-app.git
cd password-generator-app
```

### 2. Install Requirements

Make sure Python is installed (Python 3.7+ recommended).

```bash
pip install streamlit
```

### 3. Run the Streamlit App

```bash
streamlit run pass.py
```

### 4. Open in Your Browser

The app will launch automatically or you can visit:

```
http://localhost:8503
```

---

## 💡 Example

* Strength: **Strong**
* Length: **16**
* Output: `qT#4lz@3P1x&W8am`

---

## 🚀 Future Enhancements

* [ ] Copy to clipboard button
* [ ] Exclude similar characters (like l and 1, O and 0)
* [ ] Save password history
* [ ] Password visibility toggle

---

## 💼 License

This project is open-source and available under the MIT License.

---

## 👥 Author

Created by \ Rohith. Feel free to reach out or contribute!
