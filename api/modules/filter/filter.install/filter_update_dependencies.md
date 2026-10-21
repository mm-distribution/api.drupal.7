# filter_update_dependencies()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 154–163 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L154-L163)
- **Module/theme:** filter
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function filter_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function filter_update_dependencies() {
  // filter_update_7005() migrates role permissions and therefore must run
  // after the {role} and {role_permission} tables are properly set up, which
  // happens in user_update_7007().
  $dependencies['filter'][7005] = array(
    'user' => 7007,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
