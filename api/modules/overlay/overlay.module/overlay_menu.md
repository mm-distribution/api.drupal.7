# overlay_menu()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 24–39 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L24-L39)
- **Module/theme:** overlay
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function overlay_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function overlay_menu() {
  $items['overlay-ajax/%'] = array(
    'title' => '',
    'page callback' => 'overlay_ajax_render_region',
    'page arguments' => array(1),
    'access arguments' => array('access overlay'),
    'type' => MENU_CALLBACK,
  );
  $items['overlay/dismiss-message'] = array(
    'title' => '',
    'page callback' => 'overlay_user_dismiss_message',
    'access arguments' => array('access overlay'),
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
