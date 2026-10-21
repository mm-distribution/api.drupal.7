# rdf_modules_installed()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 352–364 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L352-L364)
- **Module/theme:** rdf
- **Implements:** [hook_modules_installed()](../../system/system.api.php/hook_modules_installed.md)

## Signature

```php
function rdf_modules_installed($modules)
```

## Documentation

```text
Implements hook_modules_installed().

Checks if the installed modules have any RDF mapping definitions to declare
and stores them in the rdf_mapping table.

While both default entity mappings and specific bundle mappings can be
defined in hook_rdf_mapping(), default entity mappings are not stored in the
database. Only overridden mappings are stored in the database. The default
entity mappings can be overriden by specific bundle mappings which are
stored in the database and can be altered via the RDF CRUD mapping API.
```

## Code

```php
function rdf_modules_installed($modules) {
  foreach ($modules as $module) {
    $function = $module . '_rdf_mapping';
    if (function_exists($function)) {
      foreach ($function() as $mapping) {
        // Only the bundle mappings are saved in the database.
        if ($mapping['bundle'] !== RDF_DEFAULT_BUNDLE) {
          rdf_mapping_save($mapping);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
