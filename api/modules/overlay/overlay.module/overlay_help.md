# overlay_help()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 11–19 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L11-L19)
- **Module/theme:** overlay
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function overlay_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function overlay_help($path, $arg) {
  switch ($path) {
    case 'admin/help#overlay':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Overlay module makes the administration pages on your site display in a JavaScript overlay of the page you were viewing when you clicked the administrative link, instead of replacing the page in your browser window. Use the close link on the overlay to return to the page you were viewing when you clicked the link. For more information, see the online handbook entry for <a href="@overlay">Overlay module</a>.', array('@overlay' => 'http://drupal.org/documentation/modules/overlay')) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
