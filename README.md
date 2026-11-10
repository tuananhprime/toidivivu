# Description:
This project developed a website to provide information about flights along with services offered by the airline. Additionally, customers can book tickets on the website.

## Customer Features

- View general information and details about flights.
- Search for flights.
- Book tickets (without requiring online payment integration).
- Cancel tickets within the allowed cancellation period.
- Track information about booked flights.
## Admin Features

- Post information (introductions, promotions, announcements, news) about the airline.
- Enter data for aircraft (registration number, manufacturer, seat information).
- Enter data for flights (flight number, aircraft, departure location, destination, departure time).
- View and manage customer bookings.
- Reschedule flight departure times (delay flights) if necessary.

## Technologies used: 

- Django, Python, MySql, HTML, CSS, Javascript, Bootstrap, Swiper

## Demo Video:  
- https://drive.google.com/file/d/1g-27N6oNJbGLwiqBXTjpsu9saOTO4DKm/view?usp=sharing


## Vercel UI demo

Import this repository into Vercel using the Django framework preset.
`vercel.json` enables `VERCEL_DEMO=True`; the build creates a fresh SQLite
schema without copying local accounts or bookings. Vercel automatically
collects and serves static assets. The deployed database is read-only and
POST requests are disabled, so registration and booking are unavailable.
For local development, keep `USE_SQLITE=True` in `.env`.
