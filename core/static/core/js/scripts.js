document.getElementById('create-report-btn').addEventListener('click', function() {
    var button = this;
    if (button.dataset.status === 'open') {
        window.open(button.dataset.reportUrl, '_blank');
        return;
    }
    button.innerText = 'Wait...';
    fetch('{% url "generate_ydata_html" %}')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                alert('Error creating report: ' + data.error);
                button.innerText = 'Create report';
            } else {
                button.dataset.reportUrl = data.report_url;
                button.dataset.status = 'open';
                button.innerText = 'Open report';
            }
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            button.innerText = 'Create report';
        });
});

