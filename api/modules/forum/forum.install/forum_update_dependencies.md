# forum_update_dependencies()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 246–256 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L246-L256)
- **Module/theme:** forum
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function forum_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function forum_update_dependencies() {
  $dependencies['forum'][7003] = array(
    // Forum update 7003 uses field API update functions, so must run after
    // Field API has been enabled.
    'system' => 7020,
    // Forum update 7003 relies on updated taxonomy module schema. Ensure it
    // runs after all taxonomy updates.
    'taxonomy' => 7010,
  );
  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
