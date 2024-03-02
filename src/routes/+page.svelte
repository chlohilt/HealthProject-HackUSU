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
	<div
		transition:fade={{ duration: 300 }}
		class="flex flex-col items-center gap-10 mx-10 text-center justify-center mt-28"
	>
		<div class="flex flex-col items-center gap-2">
			<h1
				class="h1 font-redHat !not-italic drop-shadow-4xl
"
			>
				Welcome Wellness Wizard!
			</h1>
			<h3 class="h3 font-redHat !not-italic">(In Training)</h3>
		</div>
		<img src="/wand.svg" alt="Wizard" class="h-16 w-auto animate-bounce" />
		<h3 class="h3 font-redHat !not-italic">
			Let's check the probability of you developing Type 2 Diabetes.
		</h3>
		<button on:click={fetchQuestions} class="btn variant-filled-primary btn-lg font-redHat"
			>Answer Health Questions</button
		>
	</div>
{:else if $stage === 1}
	<h2 class="h2 text-center m-10 font-redHat !not-italic drop-shadow-4xl">
		Type 2 Diabetes Predictive Questions
	</h2>

	<form
		on:submit|preventDefault={submitAnswers}
		transition:fade={{ duration: 300 }}
		class="flex flex-col gap-5 m-10 items-center"
	>
		{#each questions as { id, text, type }}
			<div class="w-5/6 md:w-2/3">
				{#if type === 'centile'}
					<label for={id.toString()} class="mb-2 font-redHat font-medium">{text}</label>
					<input
						type="range"
						min="1"
						max="100"
						bind:value={answers[id]}
						id={id.toString()}
						class="rounded-full"
					/>
					<span>{answers[id]}</span>
				{:else if type === 'yesOrNo'}
					<label for={id.toString()} class="mb-2 font-redHat font-medium">{text}</label>
					<select bind:value={answers[id]} id={id.toString()} class="select w-28">
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
			<h1 class="h1 font-redHat">Results</h1>
			<h2 class="h2 font-redHat">You are {percentage}% likely to get type 2 diabetes</h2>
		</div>
	</div>
{/if}
