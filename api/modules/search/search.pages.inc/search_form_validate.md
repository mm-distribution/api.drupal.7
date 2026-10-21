# search_form_validate()

- **Type:** Function
- **File:** [`modules/search/search.pages.inc`](_file.md), lines 144–146 · [local source](../../../../source/modules/search/search.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc#L144-L146)
- **Module/theme:** search

## Signature

```php
function search_form_validate($form, &$form_state)
```

## Documentation

```text
As the search form collates keys from other modules hooked in via
hook_form_alter, the validation takes place in _submit.
search_form_validate() is used solely to set the 'processed_keys' form
value for the basic search form.
```

## Code

```php
function search_form_validate($form, &$form_state) {
  form_set_value($form['basic']['processed_keys'], trim($form_state['values']['keys']), $form_state);
}
```

---
_Drupal 7.103 · [modules/search/search.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
