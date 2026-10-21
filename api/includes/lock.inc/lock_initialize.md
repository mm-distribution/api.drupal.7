# lock_initialize()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 86–90 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L86-L90)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_initialize()
```

## Documentation

```text
Initialize the locking system.
```

## Code

```php
function lock_initialize() {
  global $locks;

  $locks = array();
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
