# LinkedFolio – AI-Powered LinkedIn to Portfolio Generator

Transform your LinkedIn profile or PDF resume into a stunning portfolio website with LinkedFolio.

## 🚀 Features

- **Automated Portfolio Generation**: Convert LinkedIn profiles or PDF resumes into professional portfolios
- **AI-Powered Processing**: Enhanced content generation and optimization using LLMs
- **Dynamic & Customizable**: Multiple themes and customization options
- **SEO-Friendly**: Server-side rendered pages for optimal search engine visibility
- **Easy Deployment**: Host directly on Vercel/GitHub or download for self-hosting
- **Secure Data Management**: Powered by Supabase for reliable data storage

## 🛠️ Tech Stack

- **Frontend**: Next.js 14 (React 18)
- **Backend**: FastAPI (Python)
- **Database**: Supabase (PostgreSQL)
- **Data Extraction**: 
  - LinkedIn: Puppeteer
  - PDF: pdf.js / PyMuPDF
- **AI Processing**: LLM Integration
- **Styling**: Tailwind CSS
- **Authentication**: Supabase Auth

## 📁 Project Structure

```
linkedfolio/
├── frontend/                # Next.js frontend application
│   ├── app/                # App router components
│   ├── components/         # Reusable React components
│   ├── lib/               # Utility functions and helpers
│   └── themes/            # Portfolio themes
├── backend/                # FastAPI backend application
│   ├── app/               # Main application code
│   ├── services/          # Business logic services
│   └── utils/             # Helper utilities
└── shared/                # Shared types and utilities
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- Python 3.9+
- Supabase Account
- OpenAI API Key (for AI features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/linkedfolio.git
cd linkedfolio
```

2. Frontend Setup:
```bash
cd frontend
npm install
cp .env.example .env.local
# Configure your environment variables
npm run dev
```

3. Backend Setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Configure your environment variables
uvicorn app.main:app --reload
```

4. Set up your Supabase project and configure environment variables.

## 📝 Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend (.env)
```
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
OPENAI_API_KEY=your_openai_api_key
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 