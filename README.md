# Task Web App
This is a web application built using Django, Tailwind CSS, and jquery. it allow users to manage tasks efficiently.

## Prerequisites
Before you begin, ensure you have the following installed on your machine.

``` bash
Python (>= 3.6)
Node.js (>= 12.x)
npm (Node Package Manager)
Django (>= 3.x)
Tailwind CSS
```

## Setup Instructions
# 1. Clone the Respository
``` bash
git clone https://github.com/Olatundeawo/benmore-project.git
cd benmore-project
```

#2. Create a Virtual Environment
it's a good practise to create a virtual environment to manage your project's dependencies.
```bash
python -m venv venv
source venv/bin/activate # on Windows use `venv\Scripts\activate` 
```

#3.  Install Python Dependencies
install the required python packages using pip.
``` bash
pip install -r requirements.txt
```

#4. Install Node.js Dependencies
Navigate to the directory where your Tailwind CSS configuration is located (usually in the root or static directory).
```bash
npm install
``` 

#5. Configure Tailwind CSS
If not already present, create a Tailwind CSS configuration file.
``` bash
npx tailwindcss init
```
Update the `tailwind.config.js` file to specify the paths to your Django templates and static files:
``` bash
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js',
    './static/css/**/*.css',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

#6. Create Django App
if you haven't already created Django app, you can do so by running:
```bash
django-admin startapp your_app_name
```

#7. Add Tailwind CSS to your Django Project
Include Tailwind CSS in your Django project by creating a tailwind.css file in your static directory (e.g., static/css/tailwind.css) and importing the Tailwind directives:
```bash
@tailwind base;
@tailwind components;
@tailwind utilities;
```

#8. Build Tailwind CSS
```bash
 npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch
```

#9. Add jQuery to your project
add jquery to your base html
```bash
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

#10. Configure Django Settings
In your Django settings (settings.py), add the static files configuration:
```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

#11. Run Database Migrations
Apply the initila migrations to set up your database:
```bash
python manage.py makemigrations
python manage.py migrate
```

#12. Create a Superuser
Create a superuser account to access the Django admin:
```bash
python manage.py createsuperuser
```

#13. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

#14. Access the Application
14. Access the Application
Open your web browser and navigate to http://127.0.0.1:8000 to view the application. You can also access the admin interface at http://127.0.0.1:8000/admin.

##Usage
To include jQuery and Tailwind CSS in your HTML templates, add the following lines in your base template (base.html or similar):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Web App</title>
    <link href="{% static 'css/output.css' %}" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <!-- Your content goes here -->
    {% block content %}{% endblock %}
</body>
</html>

```

## Additional Resources

[Django Documentation](https://docs.djangoproject.com/en/5.0/)
[Tailwind CSS Documentation](https://tailwindcss.com/docs/installation)
[jQuery Documentation](https://jquery.com/)
[Node.js](https://nodejs.org/en)
[Python](https://www.python.org/)

## License

[MIT](https://choosealicense.com/licenses/mit/)