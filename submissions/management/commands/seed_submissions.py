from django.core.management.base import BaseCommand
from submissions.models import Submission
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with mock submission entries'

    def handle(self, *args, **options):
        fake = Faker()
        
        # Clear existing entries
        Submission.objects.all().delete()
        
        # Generate 75 submissions (random number between 50-100)
        num_entries = random.randint(50, 100)
        
        # Lists for generating realistic content
        text_contents = [
            "Project proposal for Q2",
            "Meeting minutes from team sync",
            "Customer feedback summary",
            "Product requirements document",
            "Weekly progress report",
            "Research findings",
            "Bug report analysis",
            "Feature specification",
            "User interview notes",
            "Market analysis report"
        ]
        
        image_urls = [
            "https://example.com/images/chart1.png",
            "https://example.com/images/diagram2.png",
            "https://example.com/images/screenshot3.png",
            "https://example.com/images/graph4.png",
            "https://example.com/images/photo5.jpg"
        ]

        submissions = []
        for i in range(num_entries):
            # Randomly choose category
            category = random.choice(['TEXT', 'IMAGE_URL'])
            
            # Generate content based on category
            if category == 'TEXT':
                content = random.choice(text_contents) + f" {fake.sentence()}"
            else:
                content = random.choice(image_urls)

            # Random date within last 30 days
            created_at = datetime.now() - timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )
            
            submission = Submission(
                content=content,
                category=category,
                is_reviewed=random.choice([True, False]),
                created_at=created_at,
                updated_at=created_at
            )
            submissions.append(submission)

        # Bulk create all submissions
        Submission.objects.bulk_create(submissions)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {num_entries} mock submissions')
        ) 