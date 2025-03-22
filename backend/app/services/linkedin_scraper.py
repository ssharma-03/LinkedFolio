from pyppeteer import launch
from typing import Dict, Any
import logging

class LinkedInScraper:
    def __init__(self):
        self.browser = None
        self.page = None

    async def init(self):
        """Initialize the browser"""
        self.browser = await launch(headless=True)
        self.page = await self.browser.newPage()

    async def close(self):
        """Close the browser"""
        if self.browser:
            await self.browser.close()

    async def scrape_profile(self, profile_url: str) -> Dict[str, Any]:
        """
        Scrape LinkedIn profile data
        Args:
            profile_url: URL of the LinkedIn profile
        Returns:
            Dictionary containing profile data
        """
        try:
            if not self.browser:
                await self.init()

            await self.page.goto(profile_url, waitUntil='networkidle0')
            
            # Extract basic profile information
            profile_data = await self.page.evaluate('''
                () => {
                    const data = {};
                    
                    // Basic info
                    data.name = document.querySelector('h1')?.innerText;
                    data.headline = document.querySelector('.text-body-medium')?.innerText;
                    
                    // Experience
                    data.experience = Array.from(document.querySelectorAll('#experience-section li'))
                        .map(exp => ({
                            title: exp.querySelector('h3')?.innerText,
                            company: exp.querySelector('p')?.innerText,
                            duration: exp.querySelector('.date-range')?.innerText,
                            description: exp.querySelector('.description')?.innerText
                        }));
                    
                    // Education
                    data.education = Array.from(document.querySelectorAll('#education-section li'))
                        .map(edu => ({
                            school: edu.querySelector('h3')?.innerText,
                            degree: edu.querySelector('.degree-name')?.innerText,
                            field: edu.querySelector('.field-of-study')?.innerText,
                            duration: edu.querySelector('.date-range')?.innerText
                        }));
                    
                    return data;
                }
            ''')
            
            return profile_data

        except Exception as e:
            logging.error(f"Error scraping LinkedIn profile: {str(e)}")
            raise e 