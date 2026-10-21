# install_goto()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1041–1047 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1041-L1047)

## Signature

```php
function install_goto($path)
```

## Documentation

```text
Sends the user to a different installer page.

This issues an on-site HTTP redirect. Messages (and errors) are erased.

@param $path
  An installer path.
```

## Code

```php
function install_goto($path) {
  global $base_url;
  include_once DRUPAL_ROOT . '/includes/common.inc';
  header('Location: ' . $base_url . '/' . $path);
  header('Cache-Control: no-cache'); // Not a permanent redirect.
  drupal_exit();
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
