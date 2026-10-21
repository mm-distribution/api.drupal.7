# includes/password.inc

- **Source:** [local](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · 292 lines

## File documentation

```text
@file
Secure password hashing functions for user authentication.

Based on the Portable PHP password hashing framework.
@see http://www.openwall.com/phpass/

An alternative or custom version of this password hashing API may be
used by setting the variable password_inc to the name of the PHP file
containing replacement user_hash_password(), user_check_password(), and
user_needs_new_hash() functions.
```

## Functions (derived index)

- [_password_itoa64()](_password_itoa64.md) — Returns a string for mapping an int to the corresponding base 64 character.
- [_password_base64_encode()](_password_base64_encode.md) — Encodes bytes into printable base 64 using the *nix standard from crypt().
- [_password_generate_salt()](_password_generate_salt.md) — Generates a random base 64-encoded salt prefixed with settings for the hash.
- [_password_enforce_log2_boundaries()](_password_enforce_log2_boundaries.md) — Ensures that $count_log2 is within set bounds.
- [_password_crypt()](_password_crypt.md) — Hash a password using a secure stretched hash.
- [_password_get_count_log2()](_password_get_count_log2.md) — Parse the log2 iteration count from a stored hash or setting string.
- [user_hash_password()](user_hash_password.md) — Hash a password using a secure hash.
- [user_check_password()](user_check_password.md) — Check whether a plain text password matches a stored hashed password.
- [user_needs_new_hash()](user_needs_new_hash.md) — Check whether a user's hashed password needs to be replaced with a new hash.

## Constants

### DRUPAL_HASH_COUNT

- Line 21

```php
define('DRUPAL_HASH_COUNT', 15);
```

```text
The standard log2 number of iterations for password stretching. This should
increase by 1 every Drupal version in order to counteract increases in the
speed and power of computers available to crack the hashes.
```

### DRUPAL_MIN_HASH_COUNT

- Line 26

```php
define('DRUPAL_MIN_HASH_COUNT', 7);
```

```text
The minimum allowed log2 number of iterations for password stretching.
```

### DRUPAL_MAX_HASH_COUNT

- Line 31

```php
define('DRUPAL_MAX_HASH_COUNT', 30);
```

```text
The maximum allowed log2 number of iterations for password stretching.
```

### DRUPAL_HASH_LENGTH

- Line 36

```php
define('DRUPAL_HASH_LENGTH', 55);
```

```text
The expected (and maximum) number of characters in a hashed password.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
