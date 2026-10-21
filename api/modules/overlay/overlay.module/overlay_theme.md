# overlay_theme()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 69–79 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L69-L79)
- **Module/theme:** overlay
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function overlay_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function overlay_theme() {
  return array(
    'overlay' => array(
      'render element' => 'page',
      'template' => 'overlay',
    ),
    'overlay_disable_message' => array(
      'render element' => 'element',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
