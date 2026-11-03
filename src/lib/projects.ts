import { getCollection, type CollectionEntry } from 'astro:content';

export type Project = CollectionEntry<'projects'>;

export async function getProjects() {
  const all = (await getCollection('projects')).sort((a, b) => a.data.order - b.data.order);
  return {
    all,
    featured: all.filter((p) => p.data.featured),
    archive: all.filter((p) => !p.data.featured),
  };
}

export const statusLabel: Record<Project['data']['status'], string> = {
  live: 'Live',
  'in-development': 'In development',
  offline: 'Offline',
  ongoing: 'Ongoing',
};

export const poster = (p: Project) => p.data.video?.replace(/loop\.mp4$/, 'poster.jpg');

export const hostOf = (url: string) => new URL(url).host.replace(/^www\./, '');

export const site = {
  name: 'gdev',
  url: 'https://gdev.bm',
  author: 'Gabriel Jones',
  email: 'gdev.bm@icloud.com',
  description:
    'gdev is a small studio in Bermuda by Gabriel Jones, making browser games and real-time graphics: Mare, a survival horror game on the Moon, and Reef, a live WebGPU coral reef.',
  social: {
    x: 'https://x.com/gabe_bda',
    github: 'https://github.com/gabriel-jones',
    linkedin: 'https://www.linkedin.com/company/gdev-bm',
  },
};
