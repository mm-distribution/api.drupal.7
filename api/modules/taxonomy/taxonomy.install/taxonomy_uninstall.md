# taxonomy_uninstall()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 11–20 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L11-L20)
- **Module/theme:** taxonomy
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function taxonomy_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function taxonomy_uninstall() {
  // Remove variables.
  variable_del('taxonomy_override_selector');
  variable_del('taxonomy_terms_per_page_admin');
  // Remove taxonomy_term bundles.
  $vocabularies = db_query("SELECT machine_name FROM {taxonomy_vocabulary}")->fetchCol();
  foreach ($vocabularies as $vocabulary) {
    field_attach_delete_bundle('taxonomy_term', $vocabulary);
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
