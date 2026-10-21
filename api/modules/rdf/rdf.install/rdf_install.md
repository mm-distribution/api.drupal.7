# rdf_install()

- **Type:** Function
- **File:** [`modules/rdf/rdf.install`](_file.md), lines 44–49 · [local source](../../../../source/modules/rdf/rdf.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.install#L44-L49)
- **Module/theme:** rdf
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function rdf_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function rdf_install() {
  // Collect any RDF mappings that were declared by modules installed before
  // this one.
  $modules = module_implements('rdf_mapping');
  rdf_modules_installed($modules);
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.install](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.install) · Licensed GPL-2.0-or-later (see LICENSE)._
