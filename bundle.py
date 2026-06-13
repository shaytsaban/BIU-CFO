#!/usr/bin/env python3
"""Run this script to create a self-contained version of the presentation.
Usage: python3 bundle.py
Output: index_bundled.html (single file, all images embedded)
"""
import base64

with open('index.html', 'r') as f:
    html = f.read()

images = [
    'assets/finance_4_hero.png',
    'assets/fighter_jet_supermarket.png',
    'assets/cfo_command_center.png',
    'assets/sports_car_control.png',
    'assets/ai_agent_worker.png',
    'assets/stage_finale.png',
]

for path in images:
    try:
        with open(path, 'rb') as img:
            b64 = base64.b64encode(img.read()).decode('utf-8')
            data_uri = f'data:image/png;base64,{b64}'
            html = html.replace(f'src="{path}"', f'src="{data_uri}"')
            html = html.replace(f"url('{path}')", f"url('{data_uri}')")
    except FileNotFoundError:
        print(f"Warning: {path} not found, skipping.")

with open('index_bundled.html', 'w') as f:
    f.write(html)

print(f"Created index_bundled.html ({len(html)//1024:,} KB)")
