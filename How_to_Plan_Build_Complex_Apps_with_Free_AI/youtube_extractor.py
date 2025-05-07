#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube Tutorial Extractor

A simple application to extract information from YouTube videos and prepare template files
for AI-assisted development based on the BMAD methodology.
"""

import os
import re
import sys
import urllib.request
import urllib.parse
import json
import shutil
from datetime import datetime


class YouTubeExtractor:
    """A class to extract information from YouTube videos and prepare templates."""

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.templates_dir = os.path.join(os.path.dirname(self.base_dir), 'docs')

    def clean_filename(self, filename):
        """Clean a string to be used as a filename."""
        # Replace spaces with underscores and remove special characters
        cleaned = re.sub(r'[^\w\s-]', '', filename)
        cleaned = re.sub(r'[\s]+', '_', cleaned)
        return cleaned

    def get_video_info(self, video_url):
        """Extract basic information about a YouTube video."""
        # Extract video ID from URL
        query = urllib.parse.urlparse(video_url)
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                params = urllib.parse.parse_qs(query.query)
                if 'v' in params:
                    video_id = params['v'][0]
                else:
                    raise ValueError("Invalid YouTube URL: Video ID not found")
            else:
                raise ValueError("Invalid YouTube URL: Not a /watch path")
        elif query.hostname in ('youtu.be'):
            video_id = query.path[1:]
        else:
            raise ValueError("Invalid YouTube URL: Not a YouTube domain")

        # Use YouTube's oEmbed API to get video info
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        
        try:
            with urllib.request.urlopen(oembed_url) as response:
                data = json.loads(response.read().decode())
                return {
                    'title': data.get('title', 'Unknown Title'),
                    'author_name': data.get('author_name', 'Unknown Channel'),
                    'video_id': video_id,
                    'url': video_url
                }
        except Exception as e:
            print(f"Error fetching video info: {e}")
            # Fallback to minimal info
            return {
                'title': "Unknown Title",
                'author_name': "Unknown Channel",
                'video_id': video_id,
                'url': video_url
            }

    def create_project_folder(self, video_info):
        """Create a project folder for the video extraction."""
        folder_name = self.clean_filename(video_info['title'])
        project_path = os.path.join(os.path.dirname(self.base_dir), folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            print(f"Created project folder: {project_path}")
        else:
            print(f"Project folder already exists: {project_path}")
        
        return project_path

    def copy_template_files(self, project_path, video_info):
        """Copy and customize template files for the project."""
        # Copy extraction template
        template_path = os.path.join(self.templates_dir, 'youtube_tutorial_extraction_template.md')
        target_path = os.path.join(project_path, 'extraction_template.md')
        
        if os.path.exists(template_path):
            with open(template_path, 'r') as f:
                template_content = f.read()
            
            # Customize the template with video info
            template_content = template_content.replace("- **Video Title**: ", f"- **Video Title**: {video_info['title']}")
            template_content = template_content.replace("- **Channel Name**: ", f"- **Channel Name**: {video_info['author_name']}")
            template_content = template_content.replace("- **URL**: ", f"- **URL**: {video_info['url']}")
            template_content = template_content.replace("- **Publication Date**: ", f"- **Publication Date**: {datetime.now().strftime('%Y-%m-%d')}")
            
            with open(target_path, 'w') as f:
                f.write(template_content)
            print(f"Created customized extraction template at: {target_path}")
        else:
            print(f"Warning: Template file not found at {template_path}")
        
        # Copy workflow guide
        workflow_path = os.path.join(self.templates_dir, 'ai_development_workflow.md')
        target_workflow_path = os.path.join(project_path, 'workflow_guide.md')
        
        if os.path.exists(workflow_path):
            with open(workflow_path, 'r') as f:
                workflow_content = f.read()
            
            # Customize the workflow guide
            workflow_title = f"## Workflow Guide for \"{video_info['title']}\""
            workflow_content = workflow_content.replace("## Workflow Guide", workflow_title)
            
            with open(target_workflow_path, 'w') as f:
                f.write(workflow_content)
            print(f"Created customized workflow guide at: {target_workflow_path}")
        else:
            print(f"Warning: Workflow guide not found at {workflow_path}")
            
        # Create a blank example file
        example_path = os.path.join(project_path, 'project_notes.md')
        with open(example_path, 'w') as f:
            f.write(f"# Project Notes for {video_info['title']}\n\n")
            f.write("Use this file to take notes as you follow along with the tutorial.\n\n")
            f.write("## Key Insights\n\n")
            f.write("1. \n")
            f.write("2. \n")
            f.write("3. \n\n")
            f.write("## Questions & Challenges\n\n")
            f.write("- \n")
            f.write("- \n\n")
            f.write("## Implementation Progress\n\n")
            f.write("- [ ] Step 1: \n")
            f.write("- [ ] Step 2: \n")
            f.write("- [ ] Step 3: \n")
        print(f"Created project notes file at: {example_path}")
    
    def create_readme(self, project_path, video_info):
        """Create a README file for the project."""
        readme_path = os.path.join(project_path, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(f"# {video_info['title']}\n\n")
            f.write(f"Tutorial extraction and implementation notes based on [{video_info['title']}]({video_info['url']})\n\n")
            f.write(f"Channel: {video_info['author_name']}\n\n")
            f.write("## Contents\n\n")
            f.write("- [Extraction Template](./extraction_template.md): Detailed breakdown of the tutorial content\n")
            f.write("- [Workflow Guide](./workflow_guide.md): Step-by-step process for implementation\n")
            f.write("- [Project Notes](./project_notes.md): Personal notes and progress tracking\n\n")
            f.write("## Getting Started\n\n")
            f.write("1. Watch the [tutorial video]({})\n".format(video_info['url']))
            f.write("2. Fill out the extraction template as you watch\n")
            f.write("3. Follow the workflow guide to implement the project\n")
            f.write("4. Track your progress in the project notes\n\n")
            f.write("Created on: {}\n".format(datetime.now().strftime("%Y-%m-%d")))
        print(f"Created README at: {readme_path}")

    def process_video(self, video_url):
        """Process a YouTube video and create all necessary files."""
        try:
            # Get video information
            print(f"Extracting information for: {video_url}")
            video_info = self.get_video_info(video_url)
            print(f"Found video: {video_info['title']} by {video_info['author_name']}")
            
            # Create project folder
            project_path = self.create_project_folder(video_info)
            
            # Copy and customize template files
            self.copy_template_files(project_path, video_info)
            
            # Create README
            self.create_readme(project_path, video_info)
            
            print("\nProject setup complete!")
            print(f"Project folder: {project_path}")
            print("Next steps:")
            print("1. Watch the video and fill out the extraction template")
            print("2. Follow the workflow guide to implement the project")
            
            return project_path
            
        except Exception as e:
            print(f"Error processing video: {e}")
            return None


def main():
    """Main function to run the YouTube Tutorial Extractor."""
    print("\n=== YouTube Tutorial Extractor ===\n")
    
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter YouTube video URL: ")
    
    extractor = YouTubeExtractor()
    extractor.process_video(video_url)


if __name__ == "__main__":
    main()
