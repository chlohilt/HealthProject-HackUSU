<script lang="ts">
	import { onMount } from 'svelte';
	interface Question {
		id: number;
		text: string;
	}

	let questions: Question[] = [];
	let answers: { [key: number]: number } = {};

	onMount(async () => {
		const response = await fetch('http://localhost:5700/get-questions');
		questions = await response.json();
		questions.forEach((question) => {
			answers[question.id] = 5; // Default rating
		});
	});

	async function submitAnswers(): Promise<void> {
		const response = await fetch('http://localhost:5700/calculate-percentage', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ answers })
		});
		console.log(answers);
		const result = await response.json();
		alert(`Your score is: ${result.percentage}%`);
	}
</script>

<form on:submit|preventDefault={submitAnswers}>
	{#each questions as { id, text }}
		<div>
			<label for={id.toString()}>{text}</label>
			<input type="range" min="1" max="10" bind:value={answers[id]} id={id.toString()} />
			<span>{answers[id]}</span>
		</div>
	{/each}
	<button type="submit">Submit</button>
</form>

<!-- <script lang="ts">
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
 -->
