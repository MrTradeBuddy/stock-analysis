// Fetch company list and populate datalist
window.addEventListener('DOMContentLoaded', () => {
  fetch('/get_companies')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById('companies');
      list.innerHTML = '';  // clear old options
      data.companies.forEach(name => {
        const opt = document.createElement('option');
        opt.value = name;
        list.appendChild(opt);
      });
    })
    .catch(err => console.error('Failed to load companies:', err));
});
