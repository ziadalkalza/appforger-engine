# Integration Type Classifier

Classify every requested third-party integration before generating a pack. The classification decides required files, approvals, security review, and tests.

## Types

### Design/tooling
Examples: Figma, Rive, LottieFiles, Illustrator, design-system repos.
Required sections: setup, import/export, asset licensing, design baseline, native/web mapping, approval workflow.

### Backend/platform
Examples: Firebase, Supabase, AWS, DigitalOcean, Render, Vercel, Netlify.
Required sections: setup, secrets, deployment, security, environment, validation.

### Payment/billing
Examples: Stripe, RevenueCat, PayPal.
Required sections: cost/risk, secrets, backend validation, frontend UX, webhooks or purchase validation, refund/cancel flows, test mode.

### Maps/location
Examples: Google Maps, Mapbox, Apple MapKit.
Required sections: API key policy, location permissions, privacy review, cost/quota review, mobile/web implementation, geolocation testing.

### Messaging/notifications
Examples: Twilio, SendGrid, Firebase Cloud Messaging, OneSignal.
Required sections: secrets, templates, rate limits, privacy, opt-in/opt-out, delivery tests.

### Analytics/monitoring
Examples: Sentry, PostHog, Mixpanel, Amplitude.
Required sections: event taxonomy, PII policy, sampling, consent, environment config, validation.

### Auth/identity
Examples: Auth0, Clerk, Firebase Auth, Apple Sign-In, Google Sign-In.
Required sections: identity model, OAuth setup, redirect/callback rules, mobile/web differences, token/session security.

### Storage/media
Examples: S3, Cloudflare R2, Supabase Storage, Cloudinary.
Required sections: buckets, permissions, signed URLs, file size/type rules, privacy, lifecycle/retention.

## Multi-type integrations

If an integration belongs to multiple types, include all required sections. Example: Firebase may be backend/platform + auth + storage + notifications.
