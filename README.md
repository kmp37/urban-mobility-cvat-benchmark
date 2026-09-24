# Urban Mobility: Multi-Class 2D Bounding Box & Polygon Annotation Benchmark

A reproducible, high-precision computer vision annotation benchmark developed using CVAT (Computer Vision Annotation Tool). Demonstrates real-world edge-case management, strict SOP adherence, and automated dataset quality verification for autonomous systems and urban robotics[cite: 4].

---

## 1. Project Overview & Scope
* **Target Application:** Autonomous vehicle obstacle detection and pedestrian safety monitoring[cite: 4].
* **Volume:** Curated high-density urban traffic frames featuring diverse daylight conditions, partial occlusions, and multi-scale object distributions[cite: 4].
* **Classes Labeled:** `vehicle` (subtype attributes: car, bus, truck, motorcycle), `pedestrian` (posture: standing, walking, riding), `traffic_sign`[cite: 4].
* **Geometry Formats:** 2D Bounding Boxes (Object Detection) and Multi-point Polygons (Instance Segmentation)[cite: 4].

---

## 2. Data Formats Provided
* **MS COCO 1.0 JSON:** Full instance schema exported at `data/annotations_coco/instances_default.json` with segmentation masks and normalized coordinates[cite: 4].
* **Ultralytics YOLO 1.1:** Coordinate `.txt` files matched to frame IDs with accompanying `data.yaml` configuration[cite: 4].

---

## 3. Quality Assurance & Edge-Case Protocols
* **Tight Boundary Constraints:** Sub-pixel inspection at 300% zoom ensures zero background margin bleed[cite: 4].
* **Occlusion Flagging:** Strict enforcement of SOP rule for targets with 15%–80% occlusion[cite: 4].
* **Automated Audit:** Built-in Python script validates zero-area bounding boxes and JSON schema compliance[cite: 4].