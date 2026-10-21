# system_date_time_lookup()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2219–2227 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2219-L2227)
- **Module/theme:** system

## Signature

```php
function system_date_time_lookup()
```

## Documentation

```text
Return the date for a given format string via Ajax.
```

## Code

```php
function system_date_time_lookup() {
  // This callback is protected with a CSRF token because user input from the
  // query string is reflected in the output.
  if (!isset($_GET['token']) || !drupal_valid_token($_GET['token'], 'admin/config/regional/date-time/formats/lookup')) {
    return MENU_ACCESS_DENIED;
  }
  $result = format_date(REQUEST_TIME, 'custom', $_GET['format']);
  drupal_json_output($result);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
