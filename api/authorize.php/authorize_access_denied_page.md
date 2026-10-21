# authorize_access_denied_page()

- **Type:** Function
- **File:** [`authorize.php`](_file.md), lines 41–46 · [local source](../../source/authorize.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/authorize.php#L41-L46)

## Signature

```php
function authorize_access_denied_page()
```

## Documentation

```text
Renders a 403 access denied page for authorize.php.
```

## Code

```php
function authorize_access_denied_page() {
  drupal_add_http_header('Status', '403 Forbidden');
  watchdog('access denied', 'authorize.php', NULL, WATCHDOG_WARNING);
  drupal_set_title('Access denied');
  return t('You are not allowed to access this page.');
}
```

---
_Drupal 7.103 · [authorize.php](https://github.com/drupal/drupal/blob/7.103/authorize.php) · Licensed GPL-2.0-or-later (see LICENSE)._
