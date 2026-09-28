export function ArrowRight({ className = "" }: { className?: string }) {
  return (
    <svg
      className={className}
      width="14"
      height="14"
      viewBox="0 0 14 14"
      fill="none"
      aria-hidden="true"
    >
      <path d="M1 7h11M7 1.5 12.5 7 7 12.5" stroke="currentColor" strokeWidth="1.6" />
    </svg>
  );
}

export function ArrowUpRight({ className = "" }: { className?: string }) {
  return (
    <svg
      className={className}
      width="14"
      height="14"
      viewBox="0 0 14 14"
      fill="none"
      aria-hidden="true"
    >
      <path d="M3 11 11 3M4.5 2.5H11.5V9.5" stroke="currentColor" strokeWidth="1.6" />
    </svg>
  );
}

export function LinkedinIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z" />
    </svg>
  );
}

export function MailIcon({ size = 16 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      aria-hidden="true"
    >
      <rect x="3" y="5" width="18" height="14" rx="1" />
      <path d="m3 7 9 6 9-6" />
    </svg>
  );
}

export function InstagramIcon({ size = 16 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      aria-hidden="true"
    >
      <rect x="3" y="3" width="18" height="18" rx="5" />
      <circle cx="12" cy="12" r="4.2" />
      <circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none" />
    </svg>
  );
}

export function XIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M4 3h3.6l4.55 6.1L17.1 3H20l-6.35 8.02L20.4 21h-3.6l-4.9-6.52L6.6 21H3.7l6.75-8.55L4 3z" />
    </svg>
  );
}

export function TiktokIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M16.5 3c.4 2.1 1.8 3.6 4 3.9v3c-1.5 0-2.9-.4-4-1.2v6.4c0 3.4-2.6 6-6 6-3.3 0-6-2.7-6-6s2.7-6 6-6c.4 0 .8 0 1.1.1v3.1a2.9 2.9 0 1 0 2 2.8V3h2.9z" />
    </svg>
  );
}

export function FacebookIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M14.5 21v-7.6h2.6l.4-3h-3V8.4c0-.87.24-1.46 1.5-1.46H17.6V4.28C17.32 4.24 16.36 4.16 15.24 4.16c-2.33 0-3.93 1.42-3.93 4.03v2.25H8.7v3h2.6V21h3.2z" />
    </svg>
  );
}

export function LinkIcon({ size = 16 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      aria-hidden="true"
    >
      <path d="M9.5 14.5 14.5 9.5" />
      <path d="M11 6.5 12.3 5.2a3.6 3.6 0 0 1 5.1 5.1L16 11.6" />
      <path d="M13 17.5 11.7 18.8a3.6 3.6 0 0 1-5.1-5.1L8 12.4" />
    </svg>
  );
}