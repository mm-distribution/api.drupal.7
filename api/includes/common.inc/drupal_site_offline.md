# drupal_site_offline()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 725–727 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L725-L727)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_site_offline()
```

## Documentation

```text
Delivers a "site is under maintenance" message to the browser.

Page callback functions wanting to report a "site offline" message should
return MENU_SITE_OFFLINE instead of calling drupal_site_offline(). However,
functions that are invoked in contexts where that return value might not
bubble up to menu_execute_active_handler() should call drupal_site_offline().
```

## Code

```php
function drupal_site_offline() {
  drupal_deliver_page(MENU_SITE_OFFLINE);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
