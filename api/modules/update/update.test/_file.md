# modules/update/update.test

- **Source:** [local](../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · 855 lines
- **Module/theme:** update

## File documentation

```text
@file
This file contains tests for the Update Manager module.

The overarching methodology of these tests is we need to compare a given
state of installed modules and themes (e.g., version, project grouping,
timestamps, etc) against a current state of what the release history XML
files we fetch say is available. We have dummy XML files (in the
modules/update/tests directory) that describe various scenarios of what's
available for different test projects, and we have dummy .info file data
(specified via hook_system_info_alter() in the update_test helper module)
describing what's currently installed. Each test case defines a set of
projects to install, their current state (via the 'update_test_system_info'
variable) and the desired available update data (via the
'update_test_xml_map' variable), and then performs a series of assertions
that the report matches our expectations given the specific initial state and
availability scenario.
```

## Classes and interfaces (derived index)

- [UpdateTestHelper](UpdateTestHelper.md) — Defines some shared functions used by all update tests.
- [UpdateCoreTestCase](UpdateCoreTestCase.md) — Tests behavior related to discovering and listing updates to Drupal core.
- [UpdateTestContribCase](UpdateTestContribCase.md) — Tests behavior related to handling updates to contributed modules and themes.
- [UpdateTestUploadCase](UpdateTestUploadCase.md) — Tests project upload and extract functionality.
- [UpdateCoreUnitTestCase](UpdateCoreUnitTestCase.md) — Tests update functionality unrelated to the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
