# base_path()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2987–2989 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2987-L2989)

## Signature

```php
function base_path()
```

## Documentation

```text
Returns the base URL path (i.e., directory) of the Drupal installation.

base_path() adds a "/" to the beginning and end of the returned path if the
path is not empty. At the very least, this will return "/".

Examples:
- http://example.com returns "/" because the path is empty.
- http://example.com/drupal/folder returns "/drupal/folder/".
```

## Code

```php
function base_path() {
  return $GLOBALS['base_path'];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
