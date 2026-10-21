# drupal_is_front_page()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 284–299 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L284-L299)

## Signature

```php
function drupal_is_front_page()
```

## Documentation

```text
Check if the current page is the front page.

@return
  Boolean value: TRUE if the current page is the front page; FALSE if otherwise.
```

## Code

```php
function drupal_is_front_page() {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['is_front_page'] = &drupal_static(__FUNCTION__);
  }
  $is_front_page = &$drupal_static_fast['is_front_page'];

  if (!isset($is_front_page)) {
    // As drupal_path_initialize updates $_GET['q'] with the 'site_frontpage' path,
    // we can check it against the 'site_frontpage' variable.
    $is_front_page = ($_GET['q'] == variable_get('site_frontpage', 'node'));
  }

  return $is_front_page;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
