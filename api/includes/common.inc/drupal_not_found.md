# drupal_not_found()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 737–739 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L737-L739)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_not_found()
```

## Documentation

```text
Delivers a "page not found" error to the browser.

Page callback functions wanting to report a "page not found" message should
return MENU_NOT_FOUND instead of calling drupal_not_found(). However,
functions that are invoked in contexts where that return value might not
bubble up to menu_execute_active_handler() should call drupal_not_found().
```

## Code

```php
function drupal_not_found() {
  drupal_deliver_page(MENU_NOT_FOUND);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
