<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<a href="/"><strong class="text-xl uppercase">WELLNESS WIZARD</strong></a>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<p class="font-redHat font-semibold hidden md:block">Contributors:</p>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://www.linkedin.com/in/chloe-hilton-720016204/"
					target="_blank"
					rel="noreferrer"
				>
					Chloe
				</a>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://www.linkedin.com/in/eden-barlow-675a212b7/"
					target="_blank"
					rel="noreferrer"
				>
					Eden
				</a>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://savcode.co"
					target="_blank"
					rel="noreferrer"
				>
					Sav
				</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
</AppShell>
