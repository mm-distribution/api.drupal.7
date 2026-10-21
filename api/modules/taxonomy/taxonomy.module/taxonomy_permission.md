# taxonomy_permission()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 67–86 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L67-L86)
- **Module/theme:** taxonomy
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function taxonomy_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function taxonomy_permission() {
  $permissions = array(
    'administer taxonomy' => array(
      'title' => t('Administer vocabularies and terms'),
    ),
  );
  foreach (taxonomy_get_vocabularies() as $vocabulary) {
    $permissions += array(
      'edit terms in ' . $vocabulary->vid => array(
        'title' => t('Edit terms in %vocabulary', array('%vocabulary' => $vocabulary->name)),
      ),
    );
    $permissions += array(
       'delete terms in ' . $vocabulary->vid => array(
         'title' => t('Delete terms from %vocabulary', array('%vocabulary' => $vocabulary->name)),
      ),
    );
  }
  return $permissions;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
