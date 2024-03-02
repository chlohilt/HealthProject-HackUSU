export async function sendDataToPython(data: any): Promise<any> {
	const response = await fetch('http://localhost:5700/api/process-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});

	if (!response.ok) {
		throw new Error('Network response was not ok');
	}

	return response.json();
}
