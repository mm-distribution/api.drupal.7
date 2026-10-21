# drupal_random_bytes()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2325–2394 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2325-L2394)

## Signature

```php
function drupal_random_bytes($count)
```

## Documentation

```text
Returns a string of highly randomized bytes (over the full 8-bit range).

On PHP 7 and later, this function is a wrapper around the built-in PHP
function random_bytes(). If that function does not exist or cannot find an
appropriate source of randomness, this function is better than simply calling
mt_rand() or any other built-in PHP function because it can return a long
string of bytes (compared to < 4 bytes normally from mt_rand()) and uses the
best available pseudo-random source.

@param int $count
  The number of characters (bytes) to return in the string.

@return string
  A randomly generated string.
```

## Code

```php
function drupal_random_bytes($count)  {
  if (function_exists('random_bytes')) {
    try {
      return random_bytes($count);
    }
    catch (Exception $e) {
      // An appropriate source of randomness could not be found. Fall back to a
      // less secure implementation.
    }
  }

  // $random_state does not use drupal_static as it stores random bytes.
  static $random_state, $bytes, $has_openssl;

  $missing_bytes = $count - strlen((string) $bytes);

  if ($missing_bytes > 0) {
    // PHP versions prior 5.3.4 experienced openssl_random_pseudo_bytes()
    // locking on Windows and rendered it unusable.
    if (!isset($has_openssl)) {
      $has_openssl = version_compare(PHP_VERSION, '5.3.4', '>=') && function_exists('openssl_random_pseudo_bytes');
    }

    // openssl_random_pseudo_bytes() will find entropy in a system-dependent
    // way.
    if ($has_openssl) {
      $bytes .= openssl_random_pseudo_bytes($missing_bytes);
    }

    // Else, read directly from /dev/urandom, which is available on many *nix
    // systems and is considered cryptographically secure.
    elseif ($fh = @fopen('/dev/urandom', 'rb')) {
      // PHP only performs buffered reads, so in reality it will always read
      // at least 4096 bytes. Thus, it costs nothing extra to read and store
      // that much so as to speed any additional invocations.
      $bytes .= fread($fh, max(4096, $missing_bytes));
      fclose($fh);
    }

    // If we couldn't get enough entropy, this simple hash-based PRNG will
    // generate a good set of pseudo-random bytes on any system.
    // Note that it may be important that our $random_state is passed
    // through hash() prior to being rolled into $output, that the two hash()
    // invocations are different, and that the extra input into the first one -
    // the microtime() - is prepended rather than appended. This is to avoid
    // directly leaking $random_state via the $output stream, which could
    // allow for trivial prediction of further "random" numbers.
    if (strlen((string) $bytes) < $count) {
      // Initialize on the first call. The contents of $_SERVER includes a mix of
      // user-specific and system information that varies a little with each page.
      if (!isset($random_state)) {
        $random_state = print_r($_SERVER, TRUE);
        if (function_exists('getmypid')) {
          // Further initialize with the somewhat random PHP process ID.
          $random_state .= getmypid();
        }
        $bytes = '';
      }

      do {
        $random_state = hash('sha256', microtime() . mt_rand() . $random_state);
        $bytes .= hash('sha256', mt_rand() . $random_state, TRUE);
      }
      while (strlen($bytes) < $count);
    }
  }
  $output = substr($bytes, 0, $count);
  $bytes = substr($bytes, $count);
  return $output;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
