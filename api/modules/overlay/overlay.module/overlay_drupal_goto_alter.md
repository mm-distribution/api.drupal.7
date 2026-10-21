# overlay_drupal_goto_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 255–278 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L255-L278)
- **Module/theme:** overlay
- **Implements:** [hook_drupal_goto_alter()](../../system/system.api.php/hook_drupal_goto_alter.md)

## Signature

```php
function overlay_drupal_goto_alter(&$path, &$options, &$http_response_code)
```

## Documentation

```text
Implements hook_drupal_goto_alter().
```

## Code

```php
function overlay_drupal_goto_alter(&$path, &$options, &$http_response_code) {
  if (overlay_get_mode() == 'child') {
    // The authorize.php script bootstraps Drupal to a very low level, where
    // the PHP code that is necessary to close the overlay properly will not be
    // loaded. Therefore, if we are redirecting to authorize.php inside the
    // overlay, instead redirect back to the current page with instructions to
    // close the overlay there before redirecting to the final destination; see
    // overlay_init().
    if ($path == system_authorized_get_url() || $path == system_authorized_batch_processing_url()) {
      $_SESSION['overlay_close_dialog'] = array($path, $options);
      $path = current_path();
      $options = drupal_get_query_parameters();
    }

    // If the current page request is inside the overlay, add ?render=overlay
    // to the new path, so that it appears correctly inside the overlay.
    if (isset($options['query'])) {
      $options['query'] += array('render' => 'overlay');
    }
    else {
      $options['query'] = array('render' => 'overlay');
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
