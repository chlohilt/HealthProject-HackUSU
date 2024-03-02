<script lang="ts">
	import { sendDataToPython } from '$lib/apiService';
	import { onMount } from 'svelte';

	let processedData: any[] = [];

	async function processData() {
		const dataToSend = [1, 2, 3]; // Example data
		try {
			const result = await sendDataToPython(dataToSend);
			processedData = result;
		} catch (error) {
			console.error('Error processing data:', error);
		}
	}

	onMount(() => {
		processData();
	});
</script>

{#each processedData as item}
	<div>{item}</div>
{/each}
