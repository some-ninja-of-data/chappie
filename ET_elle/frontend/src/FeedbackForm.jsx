
import React, { useState } from 'react';

function FeedbackForm() {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = () => {
    // Send feedback to the server
    console.log('User feedback:', feedback);
  };

  return (
    <div>
      <textarea value={feedback} onChange={(e) => setFeedback(e.target.value)} />
      <button onClick={handleSubmit}>Submit Feedback</button>
    </div>
  );
}

export default FeedbackForm;

