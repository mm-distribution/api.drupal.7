# _password_base64_encode()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 56–81 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L56-L81)

## Signature

```php
function _password_base64_encode($input, $count)
```

## Documentation

```text
Encodes bytes into printable base 64 using the *nix standard from crypt().

@param $input
  The string containing bytes to encode.
@param $count
  The number of characters (bytes) to encode.

@return
  Encoded string
```

## Code

```php
function _password_base64_encode($input, $count) {
  $output = '';
  $i = 0;
  $itoa64 = _password_itoa64();
  do {
    $value = ord($input[$i++]);
    $output .= $itoa64[$value & 0x3f];
    if ($i < $count) {
      $value |= ord($input[$i]) << 8;
    }
    $output .= $itoa64[($value >> 6) & 0x3f];
    if ($i++ >= $count) {
      break;
    }
    if ($i < $count) {
      $value |= ord($input[$i]) << 16;
    }
    $output .= $itoa64[($value >> 12) & 0x3f];
    if ($i++ >= $count) {
      break;
    }
    $output .= $itoa64[($value >> 18) & 0x3f];
  } while ($i < $count);

  return $output;
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
