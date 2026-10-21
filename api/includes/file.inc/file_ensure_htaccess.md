# file_ensure_htaccess()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 466–472 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L466-L472)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_ensure_htaccess()
```

## Documentation

```text
Creates a .htaccess file in each Drupal files directory if it is missing.
```

## Code

```php
function file_ensure_htaccess() {
  file_create_htaccess('public://', FALSE);
  if (variable_get('file_private_path', FALSE)) {
    file_create_htaccess('private://', TRUE);
  }
  file_create_htaccess('temporary://', TRUE);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
