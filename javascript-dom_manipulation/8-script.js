// Fetch data from the provided URL using the Fetch API
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    document.getElementById('hello').innerText = data.hello;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
