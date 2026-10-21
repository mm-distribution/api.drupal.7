# book_entity_info_alter()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 248–256 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L248-L256)
- **Module/theme:** book
- **Implements:** [hook_entity_info_alter()](../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function book_entity_info_alter(&$info)
```

## Documentation

```text
Implements hook_entity_info_alter().
```

## Code

```php
function book_entity_info_alter(&$info) {
  // Add the 'Print' view mode for nodes.
  $info['node']['view modes'] += array(
    'print' => array(
      'label' => t('Print'),
      'custom settings' => FALSE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
