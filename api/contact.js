export default async function handler(req, res) {
  // Only allow POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, message } = req.body;

  if (!name || !email || !message) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer re_BjQdH31b_AparmU7epzp2zGoryik3tYUK'
      },
      body: JSON.stringify({
        from: 'EduMonitor <onboarding@resend.dev>',
        to: ['chamikade01@gmail.com'],
        reply_to: email,
        subject: `EduMonitor Contact: ${name}`,
        html: `
          <h3>New Contact from EduMonitor Website</h3>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Message:</strong></p>
          <p>${message}</p>
        `
      })
    });

    const data = await response.json();

    if (response.ok) {
      return res.status(200).json({ success: true, message: 'Email sent successfully!' });
    } else {
      return res.status(400).json({ error: data.message || 'Failed to send email' });
    }
  } catch (error) {
    return res.status(500).json({ error: 'Internal server error' });
  }
}
