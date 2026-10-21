# file_default_scheme()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 263–265 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L263-L265)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_default_scheme()
```

## Documentation

```text
Gets the default file stream implementation.

@return
  'public', 'private' or any other file scheme defined as the default.
```

## Code

```php
function file_default_scheme() {
  return variable_get('file_default_scheme', 'public');
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
