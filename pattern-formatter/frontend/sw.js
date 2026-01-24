const CACHE_NAME = 'afrodocs-static-v7';
const ASSETS = [
  './',
  './?source=pwa',
  './index.html',
  './manifest.webmanifest',
  './logo/logo.png',
  './logo/logo-48x48.png',
  './logo/logo-72x72.png',
  './logo/logo-96x96.png',
  './logo/logo-128x128.png',
  './logo/logo-144x144.png',
  './logo/logo-152x152.png',
  './logo/logo-192x192.png',
  './logo/logo-384x384.png',
  './logo/logo-512x512.png'
];

// Enable navigation preload if supported
self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      // Delete old caches
      const keys = await caches.keys();
      await Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key)));
      
      // Enable navigation preload if supported
      if ('navigationPreload' in self.registration) {
        await self.registration.navigationPreload.enable();
      }
      
      await self.clients.claim();
    })()
  );
});

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

const shouldHandleRequest = (request) =>
  request.method === 'GET' && request.url.startsWith(self.location.origin);

const isNavigationRequest = (request) =>
  request.mode === 'navigate' ||
  (request.destination === 'document' && request.headers.get('accept')?.includes('text/html'));

const networkFirst = async (request) => {
  try {
    const response = await fetch(request);
    const cache = await caches.open(CACHE_NAME);
    cache.put(request, response.clone());
    return response;
  } catch (error) {
    const cached = await caches.match(request);
    if (cached) return cached;
    throw error;
  }
};

const staleWhileRevalidate = async (request) => {
  const cached = await caches.match(request);
  const fetchPromise = fetch(request)
    .then((response) => {
      if (response && response.ok) {
        return caches.open(CACHE_NAME).then((cache) => {
          cache.put(request, response.clone());
          return response;
        });
      }
      return response;
    })
    .catch(() => undefined);

  return cached || (await fetchPromise);
};

self.addEventListener('fetch', (event) => {
  if (!shouldHandleRequest(event.request)) return;

  if (isNavigationRequest(event.request)) {
    event.respondWith(networkFirst(event.request));
    return;
  }

  event.respondWith(staleWhileRevalidate(event.request));
});
