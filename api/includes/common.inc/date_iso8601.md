# date_iso8601()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2163–2167 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2163-L2167)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function date_iso8601($date)
```

## Documentation

```text
Returns an ISO8601 formatted date based on the given date.

Callback for use within hook_rdf_mapping() implementations.

@param $date
  A UNIX timestamp.

@return string
  An ISO8601 formatted date.
```

## Code

```php
function date_iso8601($date) {
  // The DATE_ISO8601 constant cannot be used here because it does not match
  // date('c') and produces invalid RDF markup.
  return date('c', $date);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
