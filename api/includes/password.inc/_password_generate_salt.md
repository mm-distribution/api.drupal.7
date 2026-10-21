# _password_generate_salt()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 99–109 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L99-L109)

## Signature

```php
function _password_generate_salt($count_log2)
```

## Documentation

```text
Generates a random base 64-encoded salt prefixed with settings for the hash.

Proper use of salts may defeat a number of attacks, including:
 - The ability to try candidate passwords against multiple hashes at once.
 - The ability to use pre-hashed lists of candidate passwords.
 - The ability to determine whether two users have the same (or different)
   password without actually having to guess one of the passwords.

@param $count_log2
  Integer that determines the number of iterations used in the hashing
  process. A larger value is more secure, but takes more time to complete.

@return
  A 12 character string containing the iteration count and a random salt.
```

## Code

```php
function _password_generate_salt($count_log2) {
  $output = '$S$';
  // Ensure that $count_log2 is within set bounds.
  $count_log2 = _password_enforce_log2_boundaries($count_log2);
  // We encode the final log2 iteration count in base 64.
  $itoa64 = _password_itoa64();
  $output .= $itoa64[$count_log2];
  // 6 bytes is the standard salt for a portable phpass hash.
  $output .= _password_base64_encode(drupal_random_bytes(6), 6);
  return $output;
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
