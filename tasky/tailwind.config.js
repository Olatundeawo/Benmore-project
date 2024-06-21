/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './task/templates/**/*.html',
    './task/static/src/**/*.js',
    './task/static/src/**/*.css',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('daisyui'),
  ],
}

