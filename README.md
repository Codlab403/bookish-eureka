# Socratic AI Tutor

An AI-powered tutoring app that uses Google's Gemini API to deliver personalized, Socratic-style tutoring sessions.

## 🚀 Features
- Interactive question-driven learning
- Supports any subject or level
- Powered by Google Generative AI (Gemini)
- Built with Streamlit for simplicity and speed

## 🛠️ Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/socratic-tutor.git
cd socratic-tutor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your Gemini API key**

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

4. **Run the app**

```bash
streamlit run main.py
```

## 🌐 Deployment (e.g. Render, Vercel)

### Render Setup
1. Push your code to a GitHub repo
2. Go to [Render.com](https://render.com) → New → Web Service
3. Use the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run main.py --server.port=$PORT`
4. Set environment variable: `GEMINI_API_KEY=your_key`
5. Use a custom domain in Render’s dashboard

## 🔒 Security Note
Avoid committing `.env` files to source code. Add `.env` to your `.gitignore`.

---

Built with ❤️ using Streamlit + Google Gemini
