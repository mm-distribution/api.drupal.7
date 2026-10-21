# _openid_dh_rand()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 530–567 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L530-L567)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_rand($stop)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_rand($stop) {
  $duplicate_cache = &drupal_static(__FUNCTION__, array());

  // Used as the key for the duplicate cache
  $rbytes = _openid_dh_long_to_binary($stop);

  if (isset($duplicate_cache[$rbytes])) {
    list($duplicate, $nbytes) = $duplicate_cache[$rbytes];
  }
  else {
    if ($rbytes[0] == "\x00") {
      $nbytes = strlen($rbytes) - 1;
    }
    else {
      $nbytes = strlen($rbytes);
    }

    $mxrand = _openid_math_pow(256, $nbytes);

    // If we get a number less than this, then it is in the
    // duplicated range.
    $duplicate = _openid_math_mod($mxrand, $stop);

    if (count($duplicate_cache) > 10) {
      $duplicate_cache = array();
    }

    $duplicate_cache[$rbytes] = array($duplicate, $nbytes);
  }

  do {
    $bytes = "\x00" . drupal_random_bytes($nbytes);
    $n = _openid_dh_binary_to_long($bytes);
    // Keep looping if this value is in the low duplicated range.
  } while (_openid_math_cmp($n, $duplicate) < 0);

  return _openid_math_mod($n, $stop);
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
