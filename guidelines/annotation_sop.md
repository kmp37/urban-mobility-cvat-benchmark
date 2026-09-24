# Standard Operating Procedure (SOP): Urban Object Detection & Segmentation

## 1. Class Definitions & Labeling Boundaries
* **vehicle**: Includes passenger cars, commercial vans, buses, and freight trucks[cite: 4].
  * *Boundary Standard*: Bounding box must enclose the entire chassis, wheels, side mirrors, and roof racks[cite: 4]. Bounding box padding must not exceed 2 pixels of ambient background[cite: 4].
* **pedestrian**: Any visible human figure on walkways, bike lanes, or roadways[cite: 4].
  * *Boundary Standard*: Drawn from top of head/hat to bottom of footwear[cite: 4]. When occluded, bound only the contiguous visible mass[cite: 4].
* **traffic_sign**: Regulatory, warning, and guide signs[cite: 4].
  * *Boundary Standard*: Tight bounding box or polygon along sign perimeter; do not enclose support poles unless explicitly instructed[cite: 4].

## 2. Occlusion & Truncation Rules
* Any object with >15% and <80% visual obstruction must be tagged with `occluded: true`[cite: 4].
* Objects with >80% occlusion must be discarded unless contextual cues clearly indicate functional presence[cite: 4].
* Truncation: For objects clipped by camera frame borders, bound strictly to image boundaries; do not extrapolate off-canvas geometry[cite: 4].

## 3. Quality Assurance & Agreement Benchmarks
* Target Intersection-over-Union (IoU): >= 0.92 on vehicle bounding boxes; >= 0.88 on complex pedestrian polygon boundaries[cite: 4].
* Zero-tolerance for unlabeled foreground vehicles within primary 50-meter camera focal plane[cite: 4].