# install_redirect_url()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 666–668 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L666-L668)

## Signature

```php
function install_redirect_url($install_state)
```

## Documentation

```text
Returns the URL that should be redirected to during an installation request.

The output of this function is suitable for sending to install_goto().

@param $install_state
  An array of information about the current installation state.

@return
  The URL to redirect to.

@see install_full_redirect_url()
```

## Code

```php
function install_redirect_url($install_state) {
  return 'install.php?' . drupal_http_build_query($install_state['parameters']);
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
