# drupal_access_denied()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 750–752 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L750-L752)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_access_denied()
```

## Documentation

```text
Delivers an "access denied" error to the browser.

Page callback functions wanting to report an "access denied" message should
return MENU_ACCESS_DENIED instead of calling drupal_access_denied(). However,
functions that are invoked in contexts where that return value might not
bubble up to menu_execute_active_handler() should call
drupal_access_denied().
```

## Code

```php
function drupal_access_denied() {
  drupal_deliver_page(MENU_ACCESS_DENIED);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
