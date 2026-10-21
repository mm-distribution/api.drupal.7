# install_already_done_error()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1362–1367 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1362-L1367)

## Signature

```php
function install_already_done_error()
```

## Documentation

```text
Indicates that Drupal has already been installed.
```

## Code

```php
function install_already_done_error() {
  global $base_url;

  drupal_set_title(st('Drupal already installed'));
  return st('<ul><li>To start over, you must empty your existing database.</li><li>To install to a different database, edit the appropriate <em>settings.php</em> file in the <em>sites</em> folder.</li><li>To upgrade an existing installation, proceed to the <a href="@base-url/update.php">update script</a>.</li><li>View your <a href="@base-url">existing site</a>.</li></ul>', array('@base-url' => $base_url));
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
