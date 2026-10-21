# search_form_submit()

- **Type:** Function
- **File:** [`modules/search/search.pages.inc`](_file.md), lines 151–159 · [local source](../../../../source/modules/search/search.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc#L151-L159)
- **Module/theme:** search

## Signature

```php
function search_form_submit($form, &$form_state)
```

## Documentation

```text
Process a search form submission.
```

## Code

```php
function search_form_submit($form, &$form_state) {
  $keys = $form_state['values']['processed_keys'];
  if ($keys == '') {
    form_set_error('keys', t('Please enter some keywords.'));
    // Fall through to the form redirect.
  }

  $form_state['redirect'] = $form_state['action'] . '/' . $keys;
}
```

---
_Drupal 7.103 · [modules/search/search.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
