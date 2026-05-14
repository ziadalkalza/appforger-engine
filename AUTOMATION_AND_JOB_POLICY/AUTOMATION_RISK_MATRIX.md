# Automation Risk Matrix

| Risk | Examples | Default behavior |
|---|---|---|
| Low | validation, draft reports, context pack generation | may run at Level 2+ |
| Medium | registry updates, candidate imports, prepare commit | needs packet/config approval |
| High | integration activation, package addition, staging deploy | explicit approval |
| Critical | production publish, data deletion, live payments, release blocker waiver | explicit high-risk override |
