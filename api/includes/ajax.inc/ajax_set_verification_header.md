# ajax_set_verification_header()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 595–608 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L595-L608)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_set_verification_header()
```

## Documentation

```text
Sets a response header for ajax.js to trust the response body.

It is not safe to invoke Ajax commands within user-uploaded files, so this
header protects against those being invoked.

@see Drupal.ajax.options.success()
```

## Code

```php
function ajax_set_verification_header() {
  $added = &drupal_static(__FUNCTION__);

  // User-uploaded files cannot set any response headers, so a custom header is
  // used to indicate to ajax.js that this response is safe. Note that most
  // Ajax requests bound using the Form API will be protected by having the URL
  // flagged as trusted in Drupal.settings, so this header is used only for
  // things like custom markup that gets Ajax behaviors attached.
  if (empty($added)) {
    drupal_add_http_header('X-Drupal-Ajax-Token', '1');
    // Avoid sending the header twice.
    $added = TRUE;
  }
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
