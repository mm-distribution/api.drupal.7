# toolbar_page_build()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 124–130 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L124-L130)
- **Module/theme:** toolbar
- **Implements:** [hook_page_build()](../../system/system.api.php/hook_page_build.md)

## Signature

```php
function toolbar_page_build(&$page)
```

## Documentation

```text
Implements hook_page_build().

Add admin toolbar to the page_top region automatically.
```

## Code

```php
function toolbar_page_build(&$page) {
  $page['page_top']['toolbar'] = array(
    '#pre_render' => array('toolbar_pre_render'),
    '#access' => user_access('access toolbar'),
    'toolbar_drawer' => array(),
  );
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
