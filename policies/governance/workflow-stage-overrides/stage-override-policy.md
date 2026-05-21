# Stage Override Policy

A stage override is any intentional change to the normal Appforger lifecycle.

Override types:
- skip: a stage is not needed;
- substitute: a stage is done through another artifact or tool;
- reorder: a stage starts earlier or later than normal;
- import: existing work is brought into Appforger;
- draft: work is explored outside canonical project state;
- waiver: required evidence is deferred or bypassed with risk recorded.

Every override must produce a stage override record and impact report before it affects project-control, baselines, or implementation packets.
