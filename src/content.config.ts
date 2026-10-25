import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const projects = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/projects' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      year: z.string(),
      tagline: z.string(),
      summary: z.string(),
      order: z.number(),
      featured: z.boolean().default(false),
      status: z.enum(['live', 'in-development', 'offline', 'ongoing']).default('live'),
      tags: z.array(z.string()).default([]),
      cover: image(),
      coverFit: z.enum(['cover', 'contain']).default('cover'),
      logo: image().optional(),
      video: z.string().optional(),
      gallery: z.array(z.object({ src: image(), alt: z.string() })).default([]),
      links: z
        .object({
          play: z.url().optional(),
          site: z.url().optional(),
          source: z.url().optional(),
        })
        .default({}),
      requires: z.string().optional(),
    }),
});

export const collections = { projects };
