# Stage Override Risk Matrix

Low risk:
- draft visual exploration;
- static HTML sandbox;
- documentation reordering;
- low-risk mock data.

Medium risk:
- frontend before backend;
- package experiment;
- imported frontend gap analysis;
- skipped Figma with substitute visual baseline.

High risk:
- backend/API change after frontend starts;
- skipping tests;
- production env changes;
- payment/auth/location integration changes;
- release blocker waiver.

Critical:
- exposing secrets;
- bypassing security/privacy review silently;
- production release with unresolved critical blocker;
- treating draft/RAG/unapproved artifact as truth.
