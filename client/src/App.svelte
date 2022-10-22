<script>
	let message = '';
	let src = '';
	
	async function getName() {
		let thisMessage = message;
		let res = await fetch(`./message?name=${message}`);
		let message_received = await res.text();
		if (res.ok && thisMessage == message) {
			src = message_received;
		}
	}
</script>

<main>
	<h1>Received Message: {src}!</h1>
	<input type="text" placeholder="enter your name" bind:value={message} />
<button on:click={getName}>Send Message</button></main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>