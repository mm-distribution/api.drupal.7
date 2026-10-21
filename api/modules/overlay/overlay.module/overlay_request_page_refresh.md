# overlay_request_page_refresh()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 980–982 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L980-L982)
- **Module/theme:** overlay

## Signature

```php
function overlay_request_page_refresh()
```

## Documentation

```text
Requests that the entire parent window is reloaded when the overlay closes.

@see overlay_trigger_refresh()
```

## Code

```php
function overlay_request_page_refresh() {
  $_SESSION['overlay_refresh_parent'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
