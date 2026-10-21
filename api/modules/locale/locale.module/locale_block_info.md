# locale_block_info()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 1021–1033 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L1021-L1033)
- **Module/theme:** locale
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function locale_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function locale_block_info() {
  include_once DRUPAL_ROOT . '/includes/language.inc';
  $block = array();
  $info = language_types_info();
  foreach (language_types_configurable(FALSE) as $type) {
    $block[$type] = array(
      'info' => t('Language switcher (@type)', array('@type' => $info[$type]['name'])),
      // Not worth caching.
      'cache' => DRUPAL_NO_CACHE,
    );
  }
  return $block;
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
