# overlay_batch_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 288–297 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L288-L297)
- **Module/theme:** overlay
- **Implements:** [hook_batch_alter()](../../system/system.api.php/hook_batch_alter.md)

## Signature

```php
function overlay_batch_alter(&$batch)
```

## Documentation

```text
Implements hook_batch_alter().

If the current page request is inside the overlay, add ?render=overlay to
the success callback URL, so that it appears correctly within the overlay.

@see overlay_get_mode()
```

## Code

```php
function overlay_batch_alter(&$batch) {
  if (overlay_get_mode() == 'child') {
    if (isset($batch['url_options']['query'])) {
      $batch['url_options']['query']['render'] = 'overlay';
    }
    else {
      $batch['url_options']['query'] = array('render' => 'overlay');
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
