# image_update_dependencies()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 166–173 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L166-L173)
- **Module/theme:** image
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function image_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function image_update_dependencies() {
  $dependencies['image'][7002] = array(
    // Image update 7002 uses field API functions, so must run after
    // Field API has been enabled.
    'system' => 7020,
  );
  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
