rebuild-viewer:
	cd viewer && npx vite build
	rm -rf docs/
	mv viewer/dist docs/
