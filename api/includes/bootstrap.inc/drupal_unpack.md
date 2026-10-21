# drupal_unpack()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1713–1722 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1713-L1722)

## Signature

```php
function drupal_unpack($obj, $field = 'data')
```

## Documentation

```text
Unserializes and appends elements from a serialized string.

@param $obj
  The object to which the elements are appended.
@param $field
  The attribute of $obj whose value should be unserialized.
```

## Code

```php
function drupal_unpack($obj, $field = 'data') {
  if ($obj->$field && $data = unserialize($obj->$field)) {
    foreach ($data as $key => $value) {
      if (!empty($key) && !isset($obj->$key)) {
        $obj->$key = $value;
      }
    }
  }
  return $obj;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
