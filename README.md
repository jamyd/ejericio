/* ───────── CSS Custom Properties (variables) ───────── */
:root {
  --spacing-base: 8px;
  --spacing-md: calc(var(--spacing-base) * 2);       /* 16px */
  --spacing-lg: calc(var(--spacing-base) * 3);       /* 24px */
  --card-min-width: 220px;
  --card-img-height: 220px;
  --border-radius: 12px;
  --badge-border-radius: 6px;
  --shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
  --color-alive: #16a34a;
  --color-dead: #b91c1c;
  --color-unknown: #6b7280;
  --font-size-base: 1rem;
  --font-size-sm: calc(var(--font-size-base) * 0.875);  /* 0.875rem */
  --font-size-lg: calc(var(--font-size-base) * 1.1);    /* 1.1rem   */
}

/* ───────── Layout ───────── */
.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: var(--spacing-lg);
}

h1 {
  margin-bottom: var(--spacing-lg);
  text-align: center;
  font-size: calc(var(--font-size-base) * 2);   /* 2rem  =  font-size-base × 2 */
  letter-spacing: 0.02em;
}

/* ───────── Status messages ───────── */
.message {
  text-align: center;
  font-size: var(--font-size-lg);
}

.error {
  color: var(--color-dead);
}

/* ───────── Card grid ───────── */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(var(--card-min-width), 1fr));
  gap: var(--spacing-md);
}

/* ───────── Individual card ───────── */
.card {
  background: #ffffff;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(calc(var(--spacing-base) * -0.5));  /* −4px */
  box-shadow: 0 calc(var(--spacing-base) + 4px) 24px rgba(0, 0, 0, 0.14);
}

.card img {
  width: 100%;
  height: var(--card-img-height);
  object-fit: cover;
  display: block;
}

.card-body {
  padding: var(--spacing-md);
}

.card h2 {
  margin: 0 0 var(--spacing-base);
  font-size: var(--font-size-lg);
}

.card p {
  margin: calc(var(--spacing-base) / 2) 0;   /* 4px = base ÷ 2 */
  font-size: var(--font-size-sm);
  color: #374151;
}

/* ───────── Status badge ───────── */
.badge {
  display: inline-block;
  padding: calc(var(--spacing-base) * 0.25) calc(var(--spacing-base) * 0.75);
  border-radius: var(--badge-border-radius);
  font-size: var(--font-size-sm);
  font-weight: 600;
  color: #ffffff;
}

/* API values: 'Alive' | 'Dead' | 'unknown' (lowercase per Rick and Morty API spec) */
.badge--alive   { background-color: var(--color-alive);   }
.badge--dead    { background-color: var(--color-dead);    }
.badge--unknown { background-color: var(--color-unknown); }
