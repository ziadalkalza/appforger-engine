# Test Run Commands Template

Commands must be project-specific and stored in project-control or repo docs after initialization.

## Backend FastAPI
- test: `pytest`

## iOS
- build: `xcodebuild -scheme <Scheme> -destination 'platform=iOS Simulator,name=<Device>' build`
- test: `xcodebuild test -scheme <Scheme> -destination 'platform=iOS Simulator,name=<Device>'`

## Android
- build: `./gradlew assembleDebug`
- unit: `./gradlew testDebugUnitTest`
- ui: `./gradlew connectedDebugAndroidTest`

## Web
- build: `npm run build`
- unit: `npm test`
- e2e: `npx playwright test`
- lint: `npm run lint`

If a command cannot be run in the current environment, record why and mark evidence as missing or manual.
