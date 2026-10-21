# _block_custom_theme()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 198–202 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L198-L202)
- **Module/theme:** block

## Signature

```php
function _block_custom_theme($theme = NULL)
```

## Documentation

```text
Theme callback for the block configuration pages.

@param $theme
  The theme whose blocks are being configured. If not set, the default theme
  is assumed.

@return
  The theme that should be used for the block configuration page, or NULL
  to indicate that the default theme should be used.
```

## Code

```php
function _block_custom_theme($theme = NULL) {
  // We return exactly what was passed in, to guarantee that the page will
  // always be displayed using the theme whose blocks are being configured.
  return $theme;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
