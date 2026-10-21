# taxonomy_update_dependencies()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 253–262 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L253-L262)
- **Module/theme:** taxonomy
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function taxonomy_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function taxonomy_update_dependencies() {
  // taxonomy_update_7004() migrates taxonomy term data to fields and therefore
  // must run after all Field modules have been enabled, which happens in
  // system_update_7027().
  $dependencies['taxonomy'][7004] = array(
    'system' => 7027,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
