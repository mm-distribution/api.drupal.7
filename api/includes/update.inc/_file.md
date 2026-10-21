# includes/update.inc

- **Source:** [local](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · 1490 lines

## File documentation

```text
@file
Drupal database update API.

This file contains functions to perform database updates for a Drupal
installation. It is included and used extensively by update.php.
```

## Functions (derived index)

- [update_fix_compatibility()](update_fix_compatibility.md) — Disable any items in the {system} table that are not core compatible.
- [update_check_incompatibility()](update_check_incompatibility.md) — Tests the compatibility of a module or theme.
- [update_prepare_d7_bootstrap()](update_prepare_d7_bootstrap.md) — Performs extra steps required to bootstrap when using a Drupal 6 database.
- [update_fix_d7_block_deltas()](update_fix_d7_block_deltas.md) — A helper function that modules can use to assist with the transformation from numeric block deltas to string block deltas during the 6.x -> 7.x upgrade.
- [update_fix_d7_requirements()](update_fix_d7_requirements.md) — Perform Drupal 6.x to 7.x updates that are required for update.php to function properly.
- [update_fix_d7_install_profile()](update_fix_d7_install_profile.md) — Register the currently installed profile in the system table.
- [update_parse_db_url()](update_parse_db_url.md) — Parse pre-Drupal 7 database connection URLs and return D7 compatible array.
- [update_get_d6_session_name()](update_get_d6_session_name.md) — Constructs a session name compatible with a D6 environment.
- [update_do_one()](update_do_one.md) — Implements callback_batch_operation().
- [update_batch()](update_batch.md) — Starts the database update batch process.
- [update_finished()](update_finished.md) — Implements callback_batch_finished().
- [update_get_update_list()](update_get_update_list.md) — Returns a list of all the pending database updates.
- [update_resolve_dependencies()](update_resolve_dependencies.md) — Resolves dependencies in a set of module updates, and orders them correctly.
- [update_get_update_function_list()](update_get_update_function_list.md) — Returns an organized list of update functions for a set of modules.
- [update_build_dependency_graph()](update_build_dependency_graph.md) — Constructs a graph which encodes the dependencies between module updates.
- [update_is_missing()](update_is_missing.md) — Determines if a module update is missing or unavailable.
- [update_already_performed()](update_already_performed.md) — Determines if a module update has already been performed.
- [update_retrieve_dependencies()](update_retrieve_dependencies.md) — Invokes hook_update_dependencies() in all installed modules.

## Classes and interfaces (derived index)

- [DrupalUpdateException](DrupalUpdateException.md)

## Constants

### REQUIRED_D6_SCHEMA_VERSION

- Line 19

```php
define('REQUIRED_D6_SCHEMA_VERSION', '6055');
```

```text
Minimum schema version of Drupal 6 required for upgrade to Drupal 7.

Upgrades from Drupal 6 to Drupal 7 require that Drupal 6 be running
the most recent version, or the upgrade could fail. We can't easily
check the Drupal 6 version once the update process has begun, so instead
we check the schema version of system.module in the system table.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
