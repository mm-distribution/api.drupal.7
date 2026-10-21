# overlay_page_delivery_callback_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 580–584 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L580-L584)
- **Module/theme:** overlay
- **Implements:** [hook_page_delivery_callback_alter()](../../system/system.api.php/hook_page_delivery_callback_alter.md)

## Signature

```php
function overlay_page_delivery_callback_alter(&$callback)
```

## Documentation

```text
Implements hook_page_delivery_callback_alter().
```

## Code

```php
function overlay_page_delivery_callback_alter(&$callback) {
  if (overlay_display_empty_page()) {
    $callback = 'overlay_deliver_empty_page';
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
