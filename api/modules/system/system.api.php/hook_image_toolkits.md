# hook_image_toolkits()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1928–1939 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1928-L1939)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_toolkits()
```

## Documentation

```text
Define image toolkits provided by this module.

The file which includes each toolkit's functions must be included in this
hook.

The toolkit's functions must be named image_toolkitname_operation().
where the operation may be:
  - 'load': Required. See image_gd_load() for usage.
  - 'save': Required. See image_gd_save() for usage.
  - 'settings': Optional. See image_gd_settings() for usage.
  - 'resize': Optional. See image_gd_resize() for usage.
  - 'rotate': Optional. See image_gd_rotate() for usage.
  - 'crop': Optional. See image_gd_crop() for usage.
  - 'desaturate': Optional. See image_gd_desaturate() for usage.

@return
  An array with the toolkit name as keys and sub-arrays with these keys:
    - 'title': A string with the toolkit's title.
    - 'available': A Boolean value to indicate that the toolkit is operating
      properly, e.g. all required libraries exist.

@see system_image_toolkits()
```

## Code

```php
function hook_image_toolkits() {
  return array(
    'working' => array(
      'title' => t('A toolkit that works.'),
      'available' => TRUE,
    ),
    'broken' => array(
      'title' => t('A toolkit that is "broken" and will not be listed.'),
      'available' => FALSE,
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_toolkits()".

- [image_test_image_toolkits()](../../simpletest/tests/image_test.module/image_test_image_toolkits.md) — `modules/simpletest/tests/image_test.module`
- [system_image_toolkits()](../system.module/system_image_toolkits.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
