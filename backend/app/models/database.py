from typing import Optional, List, Dict, Any
from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

class Portfolio(BaseModel):
    id: str
    user_id: str
    title: str
    description: Optional[str]
    theme: str
    is_public: bool
    custom_domain: Optional[str]
    seo_keywords: List[str]
    created_at: datetime
    updated_at: datetime

class ProfileData(BaseModel):
    id: str
    portfolio_id: str
    source_type: str  # "linkedin" or "pdf"
    raw_data: Dict[str, Any]
    enhanced_data: Optional[Dict[str, Any]]
    created_at: datetime
    updated_at: datetime

class Theme(BaseModel):
    id: str
    name: str
    description: str
    preview_image: str
    is_premium: bool
    created_at: datetime
    updated_at: datetime

# SQL for creating tables in Supabase:
"""
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Portfolios table
CREATE TABLE portfolios (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    theme TEXT NOT NULL,
    is_public BOOLEAN DEFAULT false,
    custom_domain TEXT UNIQUE,
    seo_keywords TEXT[] DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Profile data table
CREATE TABLE profile_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    portfolio_id UUID REFERENCES portfolios(id) ON DELETE CASCADE,
    source_type TEXT NOT NULL,
    raw_data JSONB NOT NULL,
    enhanced_data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Themes table
CREATE TABLE themes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    preview_image TEXT NOT NULL,
    is_premium BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Add indexes
CREATE INDEX idx_portfolios_user_id ON portfolios(user_id);
CREATE INDEX idx_profile_data_portfolio_id ON profile_data(portfolio_id);
""" 