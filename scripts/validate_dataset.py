"""
Dataset Quality Audit Script
Validates COCO annotation integrity: checks bounding box dimensions, category distribution, and zero-area anomalies.
"""
import json
import os

def audit_coco(annotation_path):
    if not os.path.exists(annotation_path):
        print(f"File not found: {annotation_path}")
        return

    with open(annotation_path, 'r') as f:
        data = json.load(f)

    images = {img['id']: img for img in data.get('images', [])}
    annotations = data.get('annotations', [])
    categories = {cat['id']: cat['name'] for cat in data.get('categories', [])}

    print(f"--- COCO Dataset Audit ---")
    print(f"Total Images: {len(images)}")
    print(f"Total Annotations: {len(annotations)}")
    print(f"Categories: {list(categories.values())}")

    invalid_boxes = 0
    cat_counts = {name: 0 for name in categories.values()}

    for ann in annotations:
        bbox = ann.get('bbox', [])
        if len(bbox) != 4 or bbox[2] <= 0 or bbox[3] <= 0:
            invalid_boxes += 1
            continue
        cat_name = categories.get(ann['category_id'], 'Unknown')
        cat_counts[cat_name] = cat_counts.get(cat_name, 0) + 1

    print("\nAnnotation Distribution:")
    for cat, count in cat_counts.items():
        print(f" - {cat}: {count}")

    print(f"\nAudit Result: {'PASSED' if invalid_boxes == 0 else 'FAILED'}")
    if invalid_boxes > 0:
        print(f"Warning: Found {invalid_boxes} degenerate/zero-area bounding boxes.")

if __name__ == "__main__":
    audit_coco("data/annotations_coco/instances_default.json")