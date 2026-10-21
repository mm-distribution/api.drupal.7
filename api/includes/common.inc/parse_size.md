# parse_size()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1961–1971 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1961-L1971)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function parse_size($size)
```

## Documentation

```text
Parses a given byte count.

@param $size
  A size expressed as a number of bytes with optional SI or IEC binary unit
  prefix (e.g. 2, 3K, 5MB, 10G, 6GiB, 8 bytes, 9mbytes).

@return
  An integer representation of the size in bytes.
```

## Code

```php
function parse_size($size) {
  $unit = preg_replace('/[^bkmgtpezy]/i', '', $size); // Remove the non-unit characters from the size.
  $size = (float) preg_replace('/[^0-9\.]/', '', $size); // Remove the non-numeric characters from the size.
  if ($unit) {
    // Find the position of the unit in the ordered string which is the power of magnitude to multiply a kilobyte by.
    return round($size * pow(DRUPAL_KILOBYTE, stripos('bkmgtpezy', $unit[0])));
  }
  else {
    return round($size);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
