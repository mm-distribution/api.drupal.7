# rdf_modules_uninstalled()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 369–371 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L369-L371)
- **Module/theme:** rdf
- **Implements:** [hook_modules_uninstalled()](../../system/system.api.php/hook_modules_uninstalled.md)

## Signature

```php
function rdf_modules_uninstalled($modules)
```

## Documentation

```text
Implements hook_modules_uninstalled().
```

## Code

```php
function rdf_modules_uninstalled($modules) {
  // @todo Remove RDF mappings of uninstalled modules.
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
