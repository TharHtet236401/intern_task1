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
            "https://picsum.photos/600/400",
            "https://source.unsplash.com/random/800x600",
            "https://source.unsplash.com/random/900x600",
            "https://source.unsplash.com/random/800x500",
            "https://source.unsplash.com/random/700x500",
            "https://source.unsplash.com/random/600x400"
        ]

        submissions = []
        for i in range(num_entries):
            # Randomly choose category with 60% text, 40% images
            category = random.choice(['TEXT'] * 6 + ['IMAGE_URL'] * 4)
            
            # Generate content based on category
            if category == 'TEXT':
                prefix = random.choice(text_prefixes)
                content = f"{prefix} {fake.paragraph(nb_sentences=2)}"
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
        
        # Count entries by category
        text_count = sum(1 for s in submissions if s.category == 'TEXT')
        image_count = sum(1 for s in submissions if s.category == 'IMAGE_URL')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {num_entries} mock submissions\n'
                f'Text entries: {text_count}\n'
                f'Image entries: {image_count}'
            )
        ) 