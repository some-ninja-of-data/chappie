
import React, { useState } from 'react';
import axios from 'axios';

function FileUploadForm() {
	const [file, setFile] = useState(null);
	const [filePath, setFilePath] = useState('');

	const handleFileChange = (e) => {
	setFile(e.target.files[0]);
	};

	const handleFilePathChange = (e) => {
	setFilePath(e.target.value);
	};

	const handleSubmit = async (e) => {
	e.preventDefault();
	const formData = new FormData();

	if (file) {
		formData.append('file', file);
	} else if (filePath) {
		formData.append('file_path', filePath);
	} else {
		alert('Please provide a file or a file path.');
		return;
	}

	try {
		const response = await axios.post('http://localhost:8000/process-file/', formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
		});
		console.log(response.data);
	} catch (error) {
		console.error('Error processing file:', error);
	}
	};

	return (
	<form onSubmit={handleSubmit}>
		<h1>Process CSV File</h1>
		<div>
		<label>Upload File:</label>
		<input type="file" onChange={handleFileChange} />
		</div>
		<div>
		<label>Or Enter File Path:</label>
		<input type="text" value={filePath} onChange={handleFilePathChange} placeholder="A:\\path\\to\\file.csv.gz" />
		</div>
		<button type="submit">Submit</button>
	</form>
	);
}

export default FileUploadForm;


