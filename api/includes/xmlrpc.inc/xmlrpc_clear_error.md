# xmlrpc_clear_error()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 656–658 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L656-L658)

## Signature

```php
function xmlrpc_clear_error()
```

## Documentation

```text
Clears any previously-saved errors.

@see xmlrpc_error()
```

## Code

```php
function xmlrpc_clear_error() {
  xmlrpc_error(NULL, NULL, TRUE);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
