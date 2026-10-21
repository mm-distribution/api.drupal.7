# _password_crypt()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 152–189 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L152-L189)

## Signature

```php
function _password_crypt($algo, $password, $setting)
```

## Documentation

```text
Hash a password using a secure stretched hash.

By using a salt and repeated hashing the password is "stretched". Its
security is increased because it becomes much more computationally costly
for an attacker to try to break the hash by brute-force computation of the
hashes of a large number of plain-text words or strings to find a match.

@param $algo
  The string name of a hashing algorithm usable by hash(), like 'sha256'.
@param $password
  Plain-text password up to 512 bytes (128 to 512 UTF-8 characters) to hash.
@param $setting
  An existing hash or the output of _password_generate_salt().  Must be
  at least 12 characters (the settings and salt).

@return
  A string containing the hashed password (and salt) or FALSE on failure.
  The return string will be truncated at DRUPAL_HASH_LENGTH characters max.
```

## Code

```php
function _password_crypt($algo, $password, $setting) {
  // Prevent DoS attacks by refusing to hash large passwords.
  if (strlen($password) > 512) {
    return FALSE;
  }
  // The first 12 characters of an existing hash are its setting string.
  $setting = substr($setting, 0, 12);

  if ($setting[0] != '$' || $setting[2] != '$') {
    return FALSE;
  }
  $count_log2 = _password_get_count_log2($setting);
  // Hashes may be imported from elsewhere, so we allow != DRUPAL_HASH_COUNT
  if ($count_log2 < DRUPAL_MIN_HASH_COUNT || $count_log2 > DRUPAL_MAX_HASH_COUNT) {
    return FALSE;
  }
  $salt = substr($setting, 4, 8);
  // Hashes must have an 8 character salt.
  if (strlen($salt) != 8) {
    return FALSE;
  }

  // Convert the base 2 logarithm into an integer.
  $count = 1 << $count_log2;

  // We rely on the hash() function being available in PHP 5.2+.
  $hash = hash($algo, $salt . $password, TRUE);
  do {
    $hash = hash($algo, $hash . $password, TRUE);
  } while (--$count);

  $len = strlen($hash);
  $output =  $setting . _password_base64_encode($hash, $len);
  // _password_base64_encode() of a 16 byte MD5 will always be 22 characters.
  // _password_base64_encode() of a 64 byte sha512 will always be 86 characters.
  $expected = 12 + ceil((8 * $len) / 6);
  return (strlen($output) == $expected) ? substr($output, 0, DRUPAL_HASH_LENGTH) : FALSE;
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
