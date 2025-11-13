// Helper for constructing API endpoints used by the React app
export function getApiBase() {
  const name = process.env.REACT_APP_CODESPACE_NAME;
  if (name) {
    return `https://${name}-8000.app.github.dev/api`;
  }
  // Fallback to localhost for local development
  return 'http://localhost:8000/api';
}

export function getApiEndpoint(resourceName) {
  const base = getApiBase();
  const endpoint = `${base}/${resourceName}/`;
  // Expose for debugging in the browser console when imported
  console.log(`API endpoint for ${resourceName}:`, endpoint);
  return endpoint;
}
