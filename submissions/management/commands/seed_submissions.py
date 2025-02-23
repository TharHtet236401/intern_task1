from django.core.management.base import BaseCommand
from submissions.models import Submission
from faker import Faker
import random
from datetime import datetime, timedelta

#i had no idea how to generate the fake data so i used AI composer and generate the fake data .Then, i reseach and try to understand the code and make some changes.
class Command(BaseCommand):
    help = 'Seeds the database with mock submission entries'

    def handle(self, *args, **options):
        try:
            fake = Faker()
            
            # Clear existing entries
            Submission.objects.all().delete()
            
            # Fixed number of entries
            num_entries = 50
            
            # Lists for generating realistic content
            text_prefixes = [
                "Project update:",
                "Meeting summary:",
                "Customer feedback:",
                "Bug report:",
                "Feature request:",
                "Documentation:",
                "Research notes:",
                "Team discussion:",
                "Product review:",
                "Analysis report:"
            ]
            
            image_urls = [
                "https://picsum.photos/800/600",
                "https://picsum.photos/900/600",
                "https://picsum.photos/800/500",
                "https://picsum.photos/700/500",
                "https://picsum.photos/600/400"
            ]

            # Generate dates within the last 90 days
            end_date = datetime.now()
            start_date = end_date - timedelta(days=90)
            
            submissions = []
            for i in range(num_entries):
                # Generate random date between start_date and end_date
                random_date = fake.date_time_between(
                    start_date=start_date,
                    end_date=end_date
                )
                
                # Randomly choose category with 60% text, 40% images
                category = random.choice(['TEXT'] * 6 + ['IMAGE_URL'] * 4)
                
                # Generate content based on category
                if category == 'TEXT':
                    prefix = random.choice(text_prefixes)
                    content = f"{prefix} {fake.paragraph(nb_sentences=2)}"
                else:
                    content = random.choice(image_urls)
                
                submission = Submission(
                    content=content,
                    category=category,
                    is_reviewed=random.choice([True, False]),
                    created_at=random_date,
                    updated_at=random_date
                )
                submissions.append(submission)

            # Bulk create all submissions
            Submission.objects.bulk_create(submissions)
            
            # Count entries by category
            text_count = sum(1 for s in submissions if s.category == 'TEXT')
            image_count = sum(1 for s in submissions if s.category == 'IMAGE_URL')
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created {num_entries} mock submissions\n'
                    f'Text entries: {text_count}\n'
                    f'Image entries: {image_count}\n'
                    f'Date range: {start_date.date()} to {end_date.date()}'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating mock submissions: {str(e)}')
            ) 