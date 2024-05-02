#!/bin/bash
celery -A mybook.mybook_site worker -E --concurrency=10