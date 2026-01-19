Offline Vendor Files

If your browser cannot reach external CDNs (e.g., `unpkg`, `cdnjs`, `fonts.googleapis.com`) the app will show a banner informing you that resources failed to load and will attempt to load local copies from `/vendor`.

To make the app work offline or in restricted networks, download the following files and place them in `frontend/vendor/`:

- https://unpkg.com/react-dom@18/umd/react-dom.development.js -> vendor/react-dom.development.js
- https://unpkg.com/@babel/standalone/babel.min.js -> vendor/babel.min.js
- https://cdnjs.cloudflare.com/ajax/libs/lucide/0.263.1/lucide.min.css -> vendor/lucide.min.css

Optional (recommended):
- Download `react.development.js` if you prefer a local copy of React
- You may also host `tailwind` css locally or prefer to keep CDN if available

After placing the files in `frontend/vendor/`, reload the page and the app will load the local copies automatically when CDN access is unavailable.

Note: Including these vendor files in the repo is fine for internal deployments; ensure you comply with the respective licenses when distributing.
