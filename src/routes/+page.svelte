<script lang="ts">
	import { fade } from 'svelte/transition';
	import { writable } from 'svelte/store';

	interface Question {
		id: number;
		text: string;
		type: 'centile' | 'yesOrNo';
	}

	let stage = writable(0); // 0: welcome, 1: questions, 2: result
	let questions: Question[] = [];
	let answers: { [key: number]: number } = {};
	let percentage: number;

	async function fetchQuestions() {
		const response = await fetch('http://localhost:5700/get-questions');
		questions = await response.json();
		console.log(questions);
		questions.forEach((question) => {
			answers[question.id] = 5; // Default rating
		});
		stage.set(1); // Move to questions stage
	}

	async function submitAnswers() {
		const response = await fetch('http://localhost:5700/calculate-percentage', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ answers })
		});
		const result = await response.json();
		percentage = result.percentage;
		stage.set(2); // Move to result stage
	}
</script>

{#if $stage === 0}
	<div transition:fade={{ duration: 300 }} class="flex flex-col items-center gap-5 m-10">
		<h1 class="h1">Welcome Fit Friend!</h1>
		<h2 class="h2">Let's check the probability of you developing diabetes type 2</h2>
		<button on:click={fetchQuestions} class="btn variant-filled-primary btn-lg">Next</button>
	</div>
{:else if $stage === 1}
	<h1 class="h1 text-center m-10">Type 2 Diabetes Predictive Questions</h1>

	<form
		on:submit|preventDefault={submitAnswers}
		transition:fade={{ duration: 300 }}
		class="flex flex-col gap-5 m-10 items-center"
	>
		{#each questions as { id, text, type }}
			<div class="w-5/6 md:w-2/3">
				{#if type === 'centile'}
					<label for={id.toString()}>{text}</label>
					<input type="range" min="1" max="100" bind:value={answers[id]} id={id.toString()} />
					<span>{answers[id]}</span>
				{:else if type === 'yesOrNo'}
					<label for={id.toString()}>{text}</label>
					<select bind:value={answers[id]} id={id.toString()} class="select">
						<option value="1">Yes</option>
						<option value="0">No</option>
					</select>
				{/if}
			</div>
		{/each}
		<button type="submit" class="btn variant-filled-primary btn-lg w-60">Submit</button>
	</form>
{:else if $stage === 2}
	<div transition:fade={{ duration: 300 }}>
		<div class="flex flex-col items-center gap-5 m-10">
			<h1 class="h1">Results</h1>
			<h2 class="h2">You are {percentage}% likely to get type 2 diabetes</h2>
		</div>
	</div>
{/if}
