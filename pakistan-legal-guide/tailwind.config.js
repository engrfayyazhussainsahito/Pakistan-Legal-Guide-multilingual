/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        navy: {
          50: '#eef2f8',
          100: '#d9e2f0',
          200: '#b3c4e0',
          300: '#7f9bc6',
          400: '#4f72a8',
          500: '#2f5388',
          600: '#1f3d6b',
          700: '#162f55',
          800: '#10223e',
          900: '#0b1830',
          950: '#070f20',
        },
        teal: {
          50: '#effafa',
          100: '#d3f2f1',
          200: '#a9e4e2',
          300: '#74cdcb',
          400: '#43b0ae',
          500: '#2a9594',
          600: '#1f7a7a',
          700: '#1c6262',
          800: '#1a4e4f',
          900: '#184141',
        },
        sand: {
          50: '#faf8f5',
          100: '#f3efe8',
          200: '#e7e0d3',
          300: '#d5cab6',
          400: '#b9aa8f',
          500: '#9b8c72',
          600: '#7d7059',
          700: '#5f5543',
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        serif: ['"Source Serif 4"', 'Georgia', 'serif'],
        urdu: ['"Noto Nastaliq Urdu"', '"Noto Naskh Arabic"', 'serif'],
        sindhi: ['"Noto Naskh Arabic"', '"Noto Sans Arabic"', 'serif'],
      },
      boxShadow: {
        card: '0 1px 2px rgba(11,24,48,0.06), 0 4px 16px rgba(11,24,48,0.05)',
        lift: '0 2px 4px rgba(11,24,48,0.08), 0 12px 28px rgba(11,24,48,0.10)',
      },
    },
  },
  plugins: [],
}
