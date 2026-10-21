# check_url()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1495–1497 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1495-L1497)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function check_url($uri)
```

## Documentation

```text
Strips dangerous protocols from a URI and encodes it for output to HTML.

@param $uri
  A plain-text URI that might contain dangerous protocols.

@return
  A URI stripped of dangerous protocols and encoded for output to an HTML
  attribute value. Because it is already encoded, it should not be set as a
  value within a $attributes array passed to drupal_attributes(), because
  drupal_attributes() expects those values to be plain-text strings. To pass
  a filtered URI to drupal_attributes(), call
  drupal_strip_dangerous_protocols() instead.

@see drupal_strip_dangerous_protocols()
```

## Code

```php
function check_url($uri) {
  return check_plain(drupal_strip_dangerous_protocols($uri));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
