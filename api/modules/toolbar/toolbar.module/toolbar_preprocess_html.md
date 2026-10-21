# toolbar_preprocess_html()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 148–155 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L148-L155)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_preprocess_html(&$vars)
```

## Documentation

```text
Implements hook_preprocess_html().

Add some page classes, so global page theming can adjust to the toolbar.
```

## Code

```php
function toolbar_preprocess_html(&$vars) {
  if (isset($vars['page']['page_top']['toolbar']) && user_access('access toolbar')) {
    $vars['classes_array'][] = 'toolbar';
    if (!_toolbar_is_collapsed()) {
      $vars['classes_array'][] = 'toolbar-drawer';
    }
  }
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
