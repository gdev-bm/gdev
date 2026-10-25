---
title: Reef
year: '2026'
tagline: A real-time Bermuda patch reef, rendered in the browser
summary: An 80 × 50 m slab of beach, lagoon and coral with a full day and night cycle. Orbit it from above, or zoom in and dive under.
order: 2
featured: true
status: live
tags: [WebGPU, Three.js, Blender]
cover: ../../assets/projects/reef/cover.jpg
video: /media/reef/loop.mp4
gallery:
  - { src: ../../assets/projects/reef/day.jpg, alt: The reef diorama from above at midday }
  - { src: ../../assets/projects/reef/close.jpg, alt: Waves breaking over the reef, seen up close }
  - { src: ../../assets/projects/reef/under.jpg, alt: Underwater among the corals, with light rays from the surface }
  - { src: ../../assets/projects/reef/night.jpg, alt: The reef underwater at night }
links:
  play: https://reef.gdev.bm
  source: https://github.com/gabriel-jones/reef
requires: WebGPU (Chrome, Edge or Safari 18+)
---

Reef is a diorama of a Bermuda patch reef, rendered live with three.js on WebGPU. The sun follows its true path at Bermuda's latitude, and a full moon, stars and bioluminescence take over at night.

- **Ocean.** FFT waves in three cascades, computed on the GPU, with foam, refraction, sky reflection and caustics projected onto the seabed.
- **Underwater.** Distance fog, god rays, marine snow, and bioluminescent sparks in the wakes of fish at night.
- **Reef.** Rocks, corals, gorgonians and seagrass, scattered by density rules and settled onto the real surface.
- **Fauna.** Schools of reef fish and bait balls steer as boids. Barracuda hunt the bait, and a turtle surfaces to breathe.
- **Sound.** Surf, wind, gulls, crickets and snapping shrimp, all synthesized live with Web Audio. There are no sample files.

Every model is built by a Python script running in Blender. There is no hand modelling and no AI-generated art.
