# Code registry

- **Topic id:** `registry`
- **Defined in:** [`includes/registry.inc`](../includes/registry.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc#L8)

## Documentation

```text
@defgroup registry Code registry
@{
The code registry engine.

Drupal maintains an internal registry of all interfaces or classes in the
system, allowing it to lazy-load code files as needed (reducing the amount
of code that must be parsed on each request).
```

## Members (derived, 10)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_registry_check_code()](../includes/bootstrap.inc/_registry_check_code.md) (function) — Checks for a resource in the registry.
- [_registry_parse_file()](../includes/registry.inc/_registry_parse_file.md) (function) — Parse a file and save its interface and class listings.
- [_registry_parse_files()](../includes/registry.inc/_registry_parse_files.md) (function) — Parse all changed files and save their interface and class listings.
- [_registry_update()](../includes/registry.inc/_registry_update.md) (function) — Does the work for registry_update().
- [drupal_autoload_class()](../includes/bootstrap.inc/drupal_autoload_class.md) (function) — Confirms that a class is available.
- [drupal_autoload_interface()](../includes/bootstrap.inc/drupal_autoload_interface.md) (function) — Confirms that an interface is available.
- [drupal_autoload_trait()](../includes/bootstrap.inc/drupal_autoload_trait.md) (function) — Confirms that a trait is available.
- [registry_get_parsed_files()](../includes/registry.inc/registry_get_parsed_files.md) (function) — Return the list of files in registry_file
- [registry_rebuild()](../includes/bootstrap.inc/registry_rebuild.md) (function) — Rescans all enabled modules and rebuilds the registry.
- [registry_update()](../includes/bootstrap.inc/registry_update.md) (function) — Updates the registry based on the latest files listed in the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
