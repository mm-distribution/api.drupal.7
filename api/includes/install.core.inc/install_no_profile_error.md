# install_no_profile_error()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1354–1357 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1354-L1357)

## Signature

```php
function install_no_profile_error()
```

## Documentation

```text
Indicates that there are no profiles available.
```

## Code

```php
function install_no_profile_error() {
  drupal_set_title(st('No profiles available'));
  return st('We were unable to find any installation profiles. Installation profiles tell us what modules to enable and what schema to install in the database. A profile is necessary to continue with the installation process.');
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
