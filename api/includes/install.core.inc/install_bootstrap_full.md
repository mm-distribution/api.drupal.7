# install_bootstrap_full()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1394–1396 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1394-L1396)

## Signature

```php
function install_bootstrap_full(&$install_state)
```

## Documentation

```text
Performs a full bootstrap of Drupal during installation.

@param $install_state
  An array of information about the current installation state.
```

## Code

```php
function install_bootstrap_full(&$install_state) {
  drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
