from typing import Dict, Any, List
import groq
import os
import logging
from dotenv import load_dotenv

load_dotenv()

class AIProcessor:
    def __init__(self):
        groq.api_key = os.getenv("GROQ_API_KEY")
        if not groq.api_key:
            raise ValueError("Groq API key not found in environment variables")
        self.model = "llama-70b-v3-versetile"

    async def enhance_profile(self, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance profile data using AI processing
        Args:
            profile_data: Raw profile data from LinkedIn or PDF
        Returns:
            Enhanced profile data with AI-generated content
        """
        try:
            enhanced_data = profile_data.copy()
            
            # Enhance summary
            if "summary" in profile_data:
                enhanced_data["enhanced_summary"] = await self._generate_professional_summary(
                    profile_data["summary"]
                )
            
            # Extract and enhance skills
            if "experience" in profile_data:
                enhanced_data["extracted_skills"] = await self._extract_skills(
                    profile_data["experience"]
                )
            
            # Generate SEO keywords
            enhanced_data["seo_keywords"] = await self._generate_seo_keywords(profile_data)
            
            return enhanced_data
            
        except Exception as e:
            logging.error(f"Error in AI processing: {str(e)}")
            raise e

    async def _generate_professional_summary(self, raw_summary: str) -> str:
        """Generate an enhanced professional summary"""
        try:
            prompt = f"""As a professional resume writer, enhance the following summary while maintaining accuracy and professionalism:

{raw_summary}

Please provide a concise, impactful professional summary that highlights key achievements and skills."""

            response = await groq.Completion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional resume writer focused on creating impactful summaries."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error generating summary: {str(e)}")
            return raw_summary

    async def _extract_skills(self, experience: str) -> List[str]:
        """Extract skills from experience description"""
        try:
            prompt = f"""Extract both technical and soft skills from the following professional experience. Return them as a comma-separated list:

{experience}

Focus on identifying:
1. Technical skills (programming languages, tools, platforms)
2. Soft skills (leadership, communication, project management)
3. Domain expertise (industry-specific knowledge)"""

            response = await groq.Completion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a skilled ATS (Applicant Tracking System) analyzer that extracts relevant skills from professional experiences."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=300
            )
            skills = response.choices[0].message.content.split(",")
            return [skill.strip() for skill in skills]
        except Exception as e:
            logging.error(f"Error extracting skills: {str(e)}")
            return []

    async def _generate_seo_keywords(self, profile_data: Dict[str, Any]) -> List[str]:
        """Generate SEO-friendly keywords from profile data"""
        try:
            profile_text = str(profile_data)
            prompt = f"""Generate SEO-friendly keywords from the following professional profile data. Focus on:
1. Job titles and roles
2. Industry-specific terms
3. Technical skills and tools
4. Professional certifications
5. Key achievements

Profile data:
{profile_text}

Return as a comma-separated list of relevant keywords."""

            response = await groq.Completion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an SEO expert specializing in professional profile optimization."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            keywords = response.choices[0].message.content.split(",")
            return [keyword.strip() for keyword in keywords]
        except Exception as e:
            logging.error(f"Error generating SEO keywords: {str(e)}")
            return [] 