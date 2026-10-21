# toolbar_pre_render()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 138–141 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L138-L141)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_pre_render($toolbar)
```

## Documentation

```text
Prerender function for the toolbar.

Since building the toolbar takes some time, it is done just prior to
rendering to ensure that it is built only if it will be displayed.
```

## Code

```php
function toolbar_pre_render($toolbar) {
  $toolbar = array_merge($toolbar, toolbar_view());
  return $toolbar;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
