# overlay_deliver_empty_page()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 592–596 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L592-L596)
- **Module/theme:** overlay

## Signature

```php
function overlay_deliver_empty_page()
```

## Documentation

```text
Prints an empty page.

This function is used to print out a bare minimum empty page which still has
the scripts and styles necessary in order to trigger the overlay to close.
```

## Code

```php
function overlay_deliver_empty_page() {
  $empty_page = '<html><head><title></title>' . drupal_get_css() . drupal_get_js() . '</head><body class="overlay"></body></html>';
  print $empty_page;
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
