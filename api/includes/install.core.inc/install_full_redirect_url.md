# install_full_redirect_url()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 681–684 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L681-L684)

## Signature

```php
function install_full_redirect_url($install_state)
```

## Documentation

```text
Returns the complete URL redirected to during an installation request.

@param $install_state
  An array of information about the current installation state.

@return
  The complete URL to redirect to.

@see install_redirect_url()
```

## Code

```php
function install_full_redirect_url($install_state) {
  global $base_url;
  return $base_url . '/' . install_redirect_url($install_state);
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
