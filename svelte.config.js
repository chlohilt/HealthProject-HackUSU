import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: ['.svelte'],
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: [vitePreprocess()],

	vite: {
		server: {
			proxy: {
				'/api': {
					target: 'http://localhost:5700',
					changeOrigin: true,
					rewrite: (/** @type {string} */ path) => path.replace(/^\/api/, '')
				}
			}
		}
	}
};
export default config;
