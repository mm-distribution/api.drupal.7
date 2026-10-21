# _drupal_invalid_token_set_form_error()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1137–1140 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1137-L1140)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _drupal_invalid_token_set_form_error()
```

## Documentation

```text
Helper function to call form_set_error() if there is a token error.
```

## Code

```php
function _drupal_invalid_token_set_form_error() {
  // Setting this error will cause the form to fail validation.
  form_set_error('form_token', t('The form has become outdated. Press the back button, copy any unsaved work in the form, and then reload the page.'));
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
