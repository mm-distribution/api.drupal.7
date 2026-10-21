# fix_gpc_magic()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1258–1268 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1258-L1268)

## Signature

```php
function fix_gpc_magic()
```

## Documentation

```text
Fixes double-escaping caused by "magic quotes" in some PHP installations.

@see _fix_gpc_magic()
@see _fix_gpc_magic_files()
```

## Code

```php
function fix_gpc_magic() {
  static $fixed = FALSE;
  if (!$fixed && ini_get('magic_quotes_gpc')) {
    array_walk($_GET, '_fix_gpc_magic');
    array_walk($_POST, '_fix_gpc_magic');
    array_walk($_COOKIE, '_fix_gpc_magic');
    array_walk($_REQUEST, '_fix_gpc_magic');
    array_walk($_FILES, '_fix_gpc_magic_files');
  }
  $fixed = TRUE;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
