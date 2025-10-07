# Flask Calculator API

A lightweight **Flask REST API** for performing basic mathematical operations — **addition**, **subtraction**, **multiplication**, **division**, and **square**.  
Built with simplicity and learning in mind, this project helps you understand how to create and test RESTful APIs using **Flask**.

---

## 🚀 Features

- ➕ **Add two numbers**
- ➖ **Subtract two numbers**
- ✖️ **Multiply two numbers**
- ➗ **Divide two numbers (with zero-check)**
- 🔲 **Square a single number**
- ✅ Includes basic **error handling** for invalid or missing inputs

---

## 🧱 Tech Stack

- **Python 3.x**
- **Flask** (for building REST APIs)
- **JSON** (for input/output data format)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/flask-math-api.git
cd flask-math-api
```

### 2. Install Flask
```bash
pip install flask
```


### 3. Run the application
```bash
python app.py
```


Once the server starts, the API will be available at:

http://127.0.0.1:5000/

## 📡 API Endpoints
| Method | Endpoint | Description | Required Fields |
|--------|----------|-------------|-----------------|
| POST | `/add` | Add two numbers | `num1`, `num2` |
| POST | `/subtract` | Subtract two numbers | `num1`, `num2` |
| POST | `/multiply` | Multiply two numbers | `num1`, `num2` |
| POST | `/divide` | Divide two numbers | `num1`, `num2` |
| POST | `/square` | Find the square of a number | `num` |
| GET | `/` | Welcome route showing available endpoints | — |

## 🧪 Example API Requests
### ➕ POST /add

Request Body (JSON):
```json
{
  "num1": 10,
  "num2": 5
}
```
Response:

```json
{
  "operation": "addition",
  "result": 15.0
}
```

➗ POST /divide (Example with Error)
Request Body (JSON):

```json
{
  "num1": 10,
  "num2": 0
}
```
Response:

```json
{
  "error": "Division by zero is not allowed."
}
```

## 🧰 Testing the API with Postman

You can easily test this API using Postman:

1. Open Postman and click on **New → HTTP Request**.
2. Set the method to **POST**.
3. Enter the desired endpoint, for example:
http://127.0.0.1:5000/add

4. Go to the **Body** tab → select **raw** → choose **JSON** from the dropdown.
5. Enter your JSON data, for example:
```json
{
  "num1": 8,
  "num2": 4
}
```
Click Send — you'll receive a JSON response like:

```json
{
  "operation": "addition",
  "result": 12.0
}
```
Repeat the same for /subtract, /multiply, /divide, or /square by changing the endpoint and body accordingly.

⚠️ Error Handling
The API gracefully handles:

- Missing or invalid fields

- Non-numeric input

- Division by zero

- Invalid JSON format

- Example Error Response:

```json
{
  "error": "Invalid input. Please provide valid JSON with 'num1' and 'num2'."
}
```