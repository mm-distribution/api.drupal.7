# toolbar_theme()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 39–52 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L39-L52)
- **Module/theme:** toolbar
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function toolbar_theme($existing, $type, $theme, $path)
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function toolbar_theme($existing, $type, $theme, $path) {
  $items['toolbar'] = array(
    'render element' => 'toolbar',
    'template' => 'toolbar',
    'path' => drupal_get_path('module', 'toolbar'),
  );
  $items['toolbar_toggle'] = array(
    'variables' => array(
      'collapsed' => NULL,
      'attributes' => array(),
    ),
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
